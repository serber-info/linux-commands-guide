"""Record actual CLI output with the reusable PTY recorder and render with agg.

Developer-only tooling, not a runtime dependency. The demo runs in bubblewrap
with a synthetic home, no network and no access to the real /home or /run/user.
https://docs.asciinema.org/manual/asciicast/v2/
https://docs.asciinema.org/manual/agg/usage/
"""
import argparse
import json
import re
from pathlib import Path
import shutil
import subprocess
import tempfile

from scripts.castrec import Session

# Small, read-only real commands. head deliberately previews the long explanation.
SCENES = (
    ('lh --lang en ls --quick', 3),
    ("lh --lang es -s 'espacio disco'", 4),
    ('lh --lang en chmod --explain | head -n 23', 5),
    ('lh --lang es learn pipes', 6),
    ('lh --lang en practice', 5),
    ('lh --lang es ls --quick', 3),
)


def main():
    parser = argparse.ArgumentParser(description='Record a privacy-safe real terminal demo')
    parser.add_argument('--tools', required=True, type=Path, help='venv containing shellcolorize')
    parser.add_argument('--agg', default='agg', help='agg executable (may live under /tmp)')
    parser.add_argument('--output', type=Path, default=Path(__file__).resolve().parents[1] / 'docs/demo.gif')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    tools = args.tools.resolve()
    if not (tools / 'bin/python').is_file():
        parser.error('--tools must be a Python virtual environment')
    if shutil.which('bwrap') is None or shutil.which(args.agg) is None:
        parser.error('Install/provide bwrap and agg as development tools; never runtime dependencies')
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    cast = output.with_suffix('.cast')
    with tempfile.TemporaryDirectory(prefix='lh-demo-home-') as directory:
        home = Path(directory)
        (home / '.local/bin').mkdir(parents=True)
        (home / '.inputrc').write_text('set enable-bracketed-paste off\n')
        wrapper = home / '.local/bin/lh'
        wrapper.write_text('#!/bin/sh\nexec /tmp/tools/bin/python /tmp/app/helper.py "$@"\n')
        wrapper.chmod(0o755)
        sandbox = ['bwrap', '--ro-bind', '/', '/', '--dev', '/dev', '--proc', '/proc',
                   '--tmpfs', '/home', '--tmpfs', '/run/user', '--tmpfs', '/tmp',
                   '--bind', str(home), '/home/demo', '--ro-bind', str(root), '/tmp/app',
                   '--ro-bind', str(tools), '/tmp/tools', '--unshare-pid', '--unshare-uts',
                   '--unshare-net', '--hostname', 'demo', '--chdir', '/home/demo',
                   '--die-with-parent', 'bash', '--noprofile', '--norc', '-i']
        env = {'HOME': '/home/demo', 'USER': 'demo', 'LOGNAME': 'demo', 'SHELL': '/bin/bash',
               'TERM': 'xterm-256color', 'LANG': 'C.UTF-8',
               'PATH': '/home/demo/.local/bin:/tmp/tools/bin:/usr/bin:/bin',
               'PS1': r'\[\e[38;5;244m\]demo\[\e[0m\]:\[\e[1;34m\]\w\[\e[0m\]$ ',
               'INPUTRC': '/home/demo/.inputrc', 'HISTFILE': '/dev/null',
               'PYTHONDONTWRITEBYTECODE': '1', 'FORCE_COLOR': '1'}
        with Session(str(cast), cols=96, rows=36, env=env, cmd=sandbox,
                     title='lh: quick reference, task search, explanations and practice', type_delay=0.04) as session:
            for index, (command, hold) in enumerate(SCENES):
                if index:
                    session.clear()
                session.run(command, pause_after=hold)
        events = [json.loads(line) for line in cast.read_text().splitlines()[1:]]
        transcript = ''.join(e[2] for e in events if e[1] == 'o')
        if ('Traceback' in transcript or re.search(r'/home/(?!demo(?:/|\b))[^/\s\x1b]+', transcript)
                or 'not found' in transcript):
            raise RuntimeError('Demo failed or exposed a private path; do not publish')
    subprocess.run([args.agg, '--theme', 'monokai', '--text-font-family', 'DejaVu Sans Mono',
                    '--font-size', '18', '--line-height', '1.15', '--fps-cap', '12',
                    '--idle-time-limit', '10', '--last-frame-duration', '3', str(cast), str(output)], check=True)
    print(f'Recorded actual terminal output: {cast}\nRendered GIF: {output} ({output.stat().st_size // 1024} KiB)')


if __name__ == '__main__':
    main()
