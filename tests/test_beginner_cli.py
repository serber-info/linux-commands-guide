import pytest

from guia_linux import cli


def test_basics_are_addressable(capsys):
    cli.main(["ls", "--lang", "es"])
    assert "ls -lh" in capsys.readouterr().out


def test_quick_reference(capsys):
    cli.main(["grep", "--quick", "--lang", "en"])
    out = capsys.readouterr().out
    assert "grep" in out and "--explain" in out
    assert "grep -P" not in out


def test_explanation(capsys):
    cli.main(["grep", "--explain", "--lang", "es"])
    out = capsys.readouterr().out
    assert "-n" in out and "número de línea" in out


def test_search_with_tool_is_scoped(capsys):
    cli.main(["grep", "-s", "file", "--lang", "en"])
    out = capsys.readouterr().out
    assert "grep" in out and "rsync" not in out


def test_learning_from_terminal(capsys):
    cli.main(["learn", "pipes", "--lang", "es"])
    assert "stdout" in capsys.readouterr().out


def test_practice_does_not_write(capsys, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    cli.main(["practice", "grep", "--lang", "es"])
    assert "ejemplo.log" in capsys.readouterr().out
    assert list(tmp_path.iterdir()) == []


@pytest.mark.parametrize("args", [["grep", "--quick", "--explain"], ["grep", "--category", "files"]])
def test_conflicting_options_are_rejected(args):
    with pytest.raises(SystemExit) as exc:
        cli.main(args)
    assert exc.value.code == 2
