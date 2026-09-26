import re
from pathlib import Path

import pytest

from shellcolorize import Color

from guia_linux import cli
from guia_linux.tools import TOOLS
from guia_linux.utils import search_all, strip_ansi

README = Path(__file__).resolve().parent.parent / "README.md"


@pytest.mark.parametrize("name", sorted(TOOLS))
def test_tool_module_contract(name):
    module = TOOLS[name]
    for attr in ("TITLE", "TITLE_EN", "BRIEF", "BRIEF_EN"):
        assert getattr(module, attr).strip(), f"{name}.{attr} is empty"
    entries = [e for e in module.COMMANDS if "section" not in e and "category" not in e]
    assert entries, f"{name} has no commands"
    for e in entries:
        shown = e.get("command") or e.get("logfile") or e.get("pattern")
        assert shown and strip_ansi(str(shown)).strip()
        assert e.get("description", "").strip() and e.get("description_en", "").strip(), shown


@pytest.fixture
def piped(monkeypatch):
    monkeypatch.delenv("FORCE_COLOR", raising=False)
    Color.auto()          # what main() does; stdout is captured, so colors are off
    yield
    Color.enable()


@pytest.mark.parametrize("lang", ["es", "en"])
def test_every_tool_renders_plain_when_piped(lang, capsys, piped):
    for module in TOOLS.values():
        module.show(lang)
    out = capsys.readouterr().out
    assert "\033[" not in out
    assert ("Descripción" if lang == "es" else "Description") in out


def test_readme_lists_every_tool():
    documented = set(re.findall(r"^\| `([^`]+)` \|", README.read_text(), re.M))
    assert documented == set(TOOLS)


def test_search_matches_both_languages():
    en = {tool for tool, _ in search_all("recursive", TOOLS)}
    es = {tool for tool, _ in search_all("recursivamente", TOOLS)}
    assert "grep" in en and "grep" in es


def test_regex_quantifiers_are_correct():
    patterns = [strip_ansi(e.get("pattern", "")) for e in TOOLS["regex"].COMMANDS]
    assert "(word){3}" in patterns and "word{3}" not in patterns


@pytest.mark.parametrize("env, expected", [
    ({"LANG": "es_ES.UTF-8"}, "es"), ({"LANG": "en_US.UTF-8"}, "en"),
    ({"LC_ALL": "es_MX.UTF-8", "LANG": "en_US.UTF-8"}, "es"), ({}, "en"),
])
def test_default_lang(monkeypatch, env, expected):
    for var in ("LC_ALL", "LC_MESSAGES", "LANG", "LANGUAGE"):
        monkeypatch.delenv(var, raising=False)
    for k, v in env.items():
        monkeypatch.setenv(k, v)
    assert cli.default_lang() == expected


def test_cli(capsys):
    cli.main(["--lang", "en", "grep"])
    assert "GREP Options" in capsys.readouterr().out
    cli.main(["-s", "port", "--lang", "en"])
    assert "Search: port" in capsys.readouterr().out
    with pytest.raises(SystemExit) as exc:
        cli.main(["--lang", "en", "notatool"])
    assert exc.value.code == 1 and "not found" in capsys.readouterr().err
    with pytest.raises(SystemExit):
        cli.main(["--version"])
    assert "linux-commands-guide" in capsys.readouterr().out
