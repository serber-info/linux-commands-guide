import io

import pytest

from guia_linux import cli
from guia_linux.learning import load_learning, show_learning
from guia_linux.render import Renderer


@pytest.mark.parametrize('mode', ['learn', 'practice'])
@pytest.mark.parametrize('lang', ['es', 'en'])
def test_every_lesson_and_exercise_renders(mode, lang, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    stream = io.StringIO()
    r = Renderer(lang, stream)
    for topic in load_learning(mode):
        show_learning(mode, topic, r)
        show_learning(mode, topic, r, hint=True, solution=True)
    assert stream.getvalue() and not list(tmp_path.iterdir())


def test_hints_and_solutions_are_opt_in(capsys):
    cli.main(['practice', 'grep', '--lang', 'en'])
    out = capsys.readouterr().out
    assert "grep -n 'error'" not in out
    cli.main(['practice', 'grep', '--solution', '--lang', 'en'])
    assert "grep -n 'error'" in capsys.readouterr().out


def test_bad_topic_is_actionable(capsys):
    with pytest.raises(SystemExit) as exc:
        cli.main(['learn', '../../secret', '--lang', 'en'])
    assert exc.value.code == 1 and 'lh learn' in capsys.readouterr().err


@pytest.mark.parametrize('args', [['list', '-s', 'x'], ['learn', 'pipes', '--quick'], ['--hint'], ['grep', 'extra'], ['-s', ' ']])
def test_invalid_combinations(args):
    with pytest.raises(SystemExit) as exc:
        cli.main(args)
    assert exc.value.code == 2


@pytest.mark.parametrize('mode', ['success', 'failure'])
def test_displayed_preparation_is_guarded(tmp_path, mode):
    import subprocess
    fixture_dir = tmp_path / 'fixture'
    fixture_dir.mkdir()
    stream = io.StringIO()
    show_learning('practice', 'grep', Renderer('en', stream))
    text = stream.getvalue()
    start = text.index('  if workdir=')
    end = text.index('  fi', start) + len('  fi')
    setup = text[start:end]
    stub = 'mktemp() { return 1; }\n' if mode == 'failure' else f"mktemp() {{ printf '%s\\n' '{fixture_dir}'; }}\n"
    result = subprocess.run(['/bin/sh', '-c', stub + setup], cwd=tmp_path, capture_output=True, text=True, timeout=5)
    if mode == 'failure':
        assert list(fixture_dir.iterdir()) == []
        assert 'setup failed' in result.stderr
    else:
        assert (fixture_dir / 'ejemplo.log').read_text() == load_learning('practice')['grep']['fixtures']['ejemplo.log']
    assert list(tmp_path.iterdir()) == [fixture_dir]
