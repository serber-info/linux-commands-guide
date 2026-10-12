"""Smoke an installed wheel. Run this script from outside the source checkout."""
import os
import shutil
import subprocess
import sys


def main():
    executable = shutil.which('lh')
    if executable is None:
        raise SystemExit('lh not on PATH')
    env = dict(os.environ, NO_COLOR='1')
    env.pop('PYTHONPATH', None)
    cases = [(['--lang', 'en', '--help'], 'Start:'), (['--lang', 'en', 'ls', '--quick'], 'ls -lh'),
             (['--lang', 'es', 'grep', '--explain'], 'número de línea'), (['-s', 'port'], 'port'),
             (['learn', 'pipes', '--lang', 'en'], 'stdout'), (['practice', 'grep', '--lang', 'en'], 'ejemplo.log')]
    for args, expected in cases:
        result = subprocess.run([executable, *args], env=env, capture_output=True, text=True, timeout=10)
        assert result.returncode == 0 and expected in result.stdout, (args, result.stderr)
        assert '\x1b' not in result.stdout
    result = subprocess.run([sys.executable, '-m', 'guia_linux', 'awk'], env=env, capture_output=True, text=True, timeout=10)
    assert result.returncode == 0 and 'awk' in result.stdout and '\x1b' not in result.stdout
    first = subprocess.Popen([executable, '--help'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
    first.stdout.readline()
    first.stdout.close()
    stderr = first.stderr.read()
    code = first.wait(timeout=10)
    assert code in (0, 141) and b'Traceback' not in stderr, (code, stderr)
    print('PASS: installed CLI, package resources, ES/EN, learning, practices and closed pipe')


if __name__ == '__main__':
    main()
