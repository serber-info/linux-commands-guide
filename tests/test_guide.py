"""Catalogue/CLI contracts retained from the original suite after data migration."""
import io
import re
from pathlib import Path

import pytest

from guia_linux import cli
from guia_linux.catalog import load_catalog
from guia_linux.render import Renderer

README = Path(__file__).resolve().parent.parent / 'README.md'
CATALOG = load_catalog()


@pytest.mark.parametrize('name', sorted(CATALOG.tools))
def test_tool_contract(name):
    tool = CATALOG.get(name)
    assert all((tool.title.es, tool.title.en, tool.brief.es, tool.brief.en))
    entries = [e for e in tool.examples if e.kind != 'section']
    assert entries and all(e.text.strip() and e.description.es.strip() and e.description.en.strip() for e in entries)
    assert any(e.quick for e in entries)


@pytest.mark.parametrize('lang', ['es', 'en'])
def test_every_tool_renders_plain_when_piped(lang, monkeypatch):
    monkeypatch.delenv('FORCE_COLOR', raising=False)
    stream = io.StringIO()
    renderer = Renderer(lang, stream)
    for tool in CATALOG.list():
        renderer.tool(tool)
    assert '\033[' not in stream.getvalue()
    assert ('Descripción' if lang == 'es' else 'Description') in stream.getvalue()


def test_readme_lists_every_tool():
    documented = set(re.findall(r'^\| `([^`]+)` \|', README.read_text(), re.M))
    assert documented == set(CATALOG.tools)


def test_search_matches_both_languages():
    assert 'grep' in {t.name for t, _ in CATALOG.search('recursive')}
    assert 'grep' in {t.name for t, _ in CATALOG.search('recursivamente')}


def test_regex_quantifiers_are_correct():
    patterns = [e.text for e in CATALOG.get('regex').examples]
    assert '(word){3}' in patterns and 'word{3}' not in patterns


@pytest.mark.parametrize('env, expected', [
    ({'LANG': 'es_ES.UTF-8'}, 'es'), ({'LANG': 'en_US.UTF-8'}, 'en'),
    ({'LC_ALL': 'es_MX.UTF-8', 'LANG': 'en_US.UTF-8'}, 'es'), ({}, 'en'),
])
def test_default_lang(monkeypatch, env, expected):
    for var in ('LC_ALL', 'LC_MESSAGES', 'LANG', 'LANGUAGE'):
        monkeypatch.delenv(var, raising=False)
    for k, v in env.items():
        monkeypatch.setenv(k, v)
    assert cli.default_lang() == expected


def test_cli(capsys):
    cli.main(['--lang', 'en', 'grep'])
    assert 'GREP Options' in capsys.readouterr().out
    cli.main(['-s', 'port', '--lang', 'en'])
    assert 'Search: port' in capsys.readouterr().out
    with pytest.raises(SystemExit) as exc:
        cli.main(['--lang', 'en', 'notatool'])
    assert exc.value.code == 1 and 'not found' in capsys.readouterr().err
    with pytest.raises(SystemExit):
        cli.main(['--version'])
    assert 'linux-commands-guide' in capsys.readouterr().out
