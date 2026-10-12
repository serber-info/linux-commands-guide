#!/usr/bin/env python3
"""Install this checkout in a user-owned venv, never the system Python.

https://docs.python.org/3/library/venv.html
No cleanup/overwrite fallback: a failed installation remains available for inspection.
"""
import argparse
import json
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
import tempfile
import venv

MARKER = '.lh-install.json'


def reject_symlinks(path):
    for part in (path, *path.parents):
        if part.is_symlink():
            raise ValueError(f'Symlink in installation path: {part}')


def install(argv=None):
    parser = argparse.ArgumentParser(description='Install lh in an isolated user environment / Instala lh sin sudo.')
    parser.add_argument('--prefix', type=Path, default=Path.home() / '.local/share/linux-commands-guide')
    parser.add_argument('--bin-dir', type=Path, default=Path.home() / '.local/bin')
    parser.add_argument('--upgrade', action='store_true', help='Update only an installation managed by this installer')
    parser.add_argument('--dry-run', action='store_true', help='Show paths without changing anything')
    parser.add_argument('--wheelhouse', type=Path, help='Offline installation: directory with project build/dependency wheels')
    args = parser.parse_args(argv)
    if sys.version_info < (3, 9):
        parser.error('Python 3.9+ required / Se requiere Python 3.9+')
    if hasattr(os, 'geteuid') and os.geteuid() == 0:
        parser.error('Do not run with sudo/root / No lo ejecutes con sudo/root')
    source = Path(__file__).resolve().parents[1]
    prefix = args.prefix.expanduser().absolute()
    bin_dir = args.bin_dir.expanduser().absolute()
    launcher = bin_dir / 'lh'
    executable = prefix / 'venv/bin/lh'
    try:
        if any(not c.isprintable() for c in str(prefix) + str(bin_dir)):
            raise ValueError('Control characters are not allowed in installation paths')
        reject_symlinks(prefix)
        reject_symlinks(bin_dir)
        if prefix in {Path('/'), Path.home().absolute()}:
            raise ValueError('Choose a dedicated installation directory / Elige una carpeta exclusiva')
        if prefix == bin_dir or prefix in bin_dir.parents or bin_dir in prefix.parents:
            raise ValueError('Installation and launcher directories must not contain each other')
        if prefix.exists():
            marker = prefix / MARKER
            if not args.upgrade or not marker.is_file() or marker.is_symlink():
                raise ValueError('Destination exists; use --upgrade only for a managed install / El destino ya existe')
            if prefix.stat().st_uid != os.getuid() or json.loads(marker.read_text()) != {'installer': 'linux-commands-guide', 'schema': 1}:
                raise ValueError('Installation ownership cannot be verified')
            reject_symlinks(prefix / 'venv')
            if not (prefix / 'venv/pyvenv.cfg').is_file():
                raise ValueError('Managed virtual environment is missing')
        elif args.upgrade:
            raise ValueError('--upgrade requires an existing managed installation')
        if os.path.lexists(launcher):
            if not args.upgrade or not launcher.is_symlink() or launcher.resolve() != executable.resolve():
                raise ValueError(f'Refusing to overwrite {launcher} / No se sobrescribe un lh existente')
        if args.wheelhouse and not args.wheelhouse.is_dir():
            raise ValueError('Wheelhouse directory does not exist')
        print(f'Source / Origen: {source}\nEnvironment / Entorno: {prefix / "venv"}\nCommand / Comando: {launcher}')
        if args.dry_run:
            print('Dry run: no changes / Simulación: sin cambios')
            return 0
        # Create the dedicated destination exclusively; never reuse an unknown directory.
        if not prefix.exists():
            prefix.mkdir(parents=True, exist_ok=False)
            prefix.chmod(0o700)
            venv.EnvBuilder(with_pip=True).create(prefix / 'venv')
        command = [str(prefix / 'venv/bin/python'), '-m', 'pip', 'install', '--upgrade']
        if args.wheelhouse:
            command += ['--no-index', '--find-links', str(args.wheelhouse.resolve())]
        # Build a clean source snapshot: never package stale build/ or private dotfiles.
        # Source builds can otherwise reuse setuptools' old build/lib modules.
        with tempfile.TemporaryDirectory(prefix='lh-install-source-') as staging:
            staged = Path(staging)
            for name in ('guia_linux', 'scripts', 'docs', 'tests', 'pyproject.toml', 'README.md',
                         'LICENSE', 'MANIFEST.in', 'install.sh', 'helper.py', 'CONTRIBUTING.md', 'CHANGELOG.md'):
                item = source / name
                if item.is_dir():
                    shutil.copytree(item, staged / name, ignore=shutil.ignore_patterns('__pycache__'))
                elif item.is_file():
                    shutil.copy2(item, staged / name)
            # Run outside the source: its generated egg-info can shadow an existing
            # installation and prevent pip from uninstalling old tracked files.
            subprocess.run(command + [str(staged)], check=True, cwd=prefix)
        subprocess.run([str(executable), '--version'], check=True, cwd=prefix)
        (prefix / MARKER).write_text(json.dumps({'installer': 'linux-commands-guide', 'schema': 1}) + '\n')
        bin_dir.mkdir(parents=True, exist_ok=True)
        if not os.path.lexists(launcher):
            launcher.symlink_to(executable)
        print('Installed / Instalado. Try / Prueba: lh ls --quick')
        if str(bin_dir) not in os.environ.get('PATH', '').split(os.pathsep):
            print(f'For this terminal / Para esta terminal:\n  export PATH={shlex.quote(str(bin_dir))}:"$PATH"')
            print('No shell files were edited / No se han modificado archivos de tu shell.')
        return 0
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print(f'Installation stopped / Instalación detenida: {exc}', file=sys.stderr)
        print('Existing files are not removed automatically / No se borran archivos automáticamente.', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(install())
