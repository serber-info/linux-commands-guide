import importlib.util
from pathlib import Path
import subprocess
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('lh_installer', ROOT / 'scripts/install.py')
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


def args(tmp_path):
    return ['--prefix', str(tmp_path / 'installation'), '--bin-dir', str(tmp_path / 'bin')]


def test_dry_run_is_read_only(tmp_path):
    assert installer.install(args(tmp_path) + ['--dry-run']) == 0
    assert not list(tmp_path.iterdir())


def test_existing_launcher_is_never_overwritten(tmp_path):
    (tmp_path / 'bin').mkdir()
    launcher = tmp_path / 'bin/lh'
    launcher.write_text('another application')
    assert installer.install(args(tmp_path)) == 1
    assert launcher.read_text() == 'another application'
    assert not (tmp_path / 'installation').exists()


def test_unknown_existing_directory_is_not_reused(tmp_path):
    prefix = tmp_path / 'installation'
    prefix.mkdir()
    marker = prefix / 'personal.txt'
    marker.write_text('keep me')
    assert installer.install(args(tmp_path) + ['--upgrade']) == 1
    assert marker.read_text() == 'keep me'


def test_symlink_install_directory_is_rejected(tmp_path):
    target = tmp_path / 'personal'
    target.mkdir()
    (tmp_path / 'installation').symlink_to(target, target_is_directory=True)
    assert installer.install(args(tmp_path)) == 1
    assert list(target.iterdir()) == []


def test_broken_launcher_symlink_is_also_preserved(tmp_path):
    (tmp_path / 'bin').mkdir()
    link = tmp_path / 'bin/lh'
    link.symlink_to(tmp_path / 'missing')
    assert installer.install(args(tmp_path)) == 1
    assert link.is_symlink() and not (tmp_path / 'installation').exists()


def test_nested_prefix_and_bin_are_rejected(tmp_path):
    assert installer.install(['--prefix', str(tmp_path / 'install'), '--bin-dir', str(tmp_path / 'install/bin')]) == 1
    assert not list(tmp_path.iterdir())


def test_root_is_rejected(tmp_path, monkeypatch):
    monkeypatch.setattr(installer.os, 'geteuid', lambda: 0)
    with pytest.raises(SystemExit) as exc:
        installer.install(args(tmp_path))
    assert exc.value.code == 2 and not list(tmp_path.iterdir())


def test_wrapper_help_works_outside_checkout(tmp_path):
    r = subprocess.run(['/bin/sh', str(ROOT / 'install.sh'), '--help'], cwd=tmp_path, capture_output=True, text=True, timeout=5)
    assert r.returncode == 0 and '--dry-run' in r.stdout


def test_path_controls_are_rejected(tmp_path):
    assert installer.install(['--prefix', str(tmp_path / 'line\nforged'), '--bin-dir', str(tmp_path / 'bin')]) == 1
    assert not list(tmp_path.iterdir())


def test_import_does_not_load_catalogue():
    r = subprocess.run([sys.executable, '-c', 'import sys, guia_linux; assert "guia_linux.cli" not in sys.modules; assert "guia_linux.catalog" not in sys.modules'], cwd=ROOT, capture_output=True, text=True, timeout=5)
    assert r.returncode == 0, r.stderr


def test_source_snapshot_excludes_build_and_pip_runs_outside_it(tmp_path, monkeypatch):
    def fake_create(self, path):
        (path / 'bin').mkdir(parents=True)
        (path / 'bin/lh').write_text('test launcher')
    checked = []
    def fake_run(command, **kwargs):
        if '-m' in command:
            staged = Path(command[-1])
            assert (staged / 'guia_linux/content/tools/ls.json').is_file()
            assert not (staged / 'build').exists() and not (staged / '.git').exists()
            assert not (staged / '.aws').exists() and not (staged / '.codex').exists()
            assert not list((staged / 'guia_linux').rglob('*.pyc'))
            assert kwargs['cwd'] == tmp_path / 'installation'
            checked.append(True)
    monkeypatch.setattr(installer.venv.EnvBuilder, 'create', fake_create)
    monkeypatch.setattr(installer.subprocess, 'run', fake_run)
    assert installer.install(args(tmp_path)) == 0
    assert checked and (tmp_path / 'bin/lh').is_symlink()
