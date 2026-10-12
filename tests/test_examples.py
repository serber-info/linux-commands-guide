"""Execute only explicit, harmless regression examples in temporary directories."""
import shutil
import subprocess

import pytest

from guia_linux.catalog import load_catalog
from guia_linux.learning import load_learning


@pytest.mark.skipif(shutil.which('grep') is None, reason='grep unavailable')
def test_grep_directory_examples(tmp_path):
    (tmp_path / 'ejemplo.txt').write_text('word\n')
    (tmp_path / 'skip.log').write_text('word\n')
    examples = load_catalog().get('grep').examples
    for entry in examples:
        if '--include=' not in entry.text and '--exclude=' not in entry.text:
            continue
        assert 'grep -r ' in entry.text
        # Execute the real displayed example with only the path placeholder substituted.
        import shlex
        argv = shlex.split(entry.text)
        argv[-1] = str(tmp_path)
        result = subprocess.run(argv, capture_output=True, text=True, timeout=5)
        assert result.returncode == 0 and 'ejemplo.txt' in result.stdout and 'skip.log' not in result.stdout


@pytest.mark.skipif(shutil.which('chmod') is None, reason='chmod unavailable')
def test_chmod_umask_is_documented(tmp_path):
    path = tmp_path / 'probe'
    path.touch(mode=0o600)
    # The explicit owner form is independent of the shell's umask.
    subprocess.run(['chmod', 'u+x', str(path)], check=True, timeout=5)
    assert path.stat().st_mode & 0o777 == 0o700
    assert 'umask' in load_catalog().get('chmod').notes.en


def test_xargs_uses_nul_and_no_empty_execution():
    for entry in load_catalog().get('xargs').examples:
        if entry.text.startswith('find ') and '| xargs' in entry.text:
            assert '-print0' in entry.text and 'xargs -0 -r' in entry.text


@pytest.mark.parametrize('topic', sorted(load_learning('practice')))
def test_practice_solutions_with_fixtures(topic, tmp_path):
    data = load_learning('practice')[topic]
    for filename, content in data['fixtures'].items():
        (tmp_path / filename).write_text(content)
    # The executed string is reviewed package content, never user input.
    # Do not generalize this into a command runner for the catalogue.
    result = subprocess.run(['/bin/sh', '-c', data['solution']], cwd=tmp_path,
                            env={'PATH': '/usr/bin:/bin', 'LC_ALL': 'C'}, capture_output=True, text=True, timeout=5)
    assert result.returncode == 0, result.stderr
    assert sorted(line.split() for line in result.stdout.splitlines()) == sorted(line.split() for line in data['expected'].splitlines())
    assert {p.name: p.read_text() for p in tmp_path.iterdir()} == data['fixtures']
