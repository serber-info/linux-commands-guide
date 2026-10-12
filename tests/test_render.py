import io

import pytest
from shellcolorize import Color

from guia_linux.catalog import load_catalog
from guia_linux.render import Renderer


@pytest.mark.parametrize('width', [24, 40, 80, 120])
def test_headers_fit_and_commands_are_not_rewritten(width, monkeypatch):
    monkeypatch.delenv('FORCE_COLOR', raising=False)
    stream = io.StringIO()
    r = Renderer('en', stream, width)
    tool = load_catalog().get('grep')
    r.tool(tool, quick=True)
    out = stream.getvalue()
    assert '\x1b' not in out
    assert "grep -nF 'error' ejemplo.log" in out
    assert all(len(line) <= width for line in out.splitlines() if '╔' in line or '║' in line or '╚' in line)


def test_color_is_stream_local(monkeypatch):
    monkeypatch.delenv('NO_COLOR', raising=False)
    original = {n: getattr(Color, n) for n in vars(Color) if n.isupper()}
    monkeypatch.setenv('FORCE_COLOR', '1')
    colorful = io.StringIO()
    Renderer('en', colorful).tool(load_catalog().get('ls'))
    assert '\x1b[' in colorful.getvalue()
    monkeypatch.setenv('NO_COLOR', '1')
    plain = io.StringIO()
    Renderer('en', plain).tool(load_catalog().get('ls'))
    assert '\x1b[' not in plain.getvalue()
    assert original == {n: getattr(Color, n) for n in original}


def test_query_control_characters_cannot_clear_terminal(monkeypatch):
    monkeypatch.delenv('FORCE_COLOR', raising=False)
    stream = io.StringIO()
    Renderer('en', stream).search('\x1b[2J\nforged', ())
    assert '\x1b' not in stream.getvalue()
    assert r'\x1b' in stream.getvalue()


def test_quick_is_bounded_and_explanations_have_sources():
    stream = io.StringIO()
    Renderer('es', stream).tool(load_catalog().get('system'), quick=True)
    assert sum('cd ' in line for line in stream.getvalue().splitlines()) <= 8
    stream = io.StringIO()
    Renderer('es', stream).tool(load_catalog().get('grep'), explain=True)
    assert 'número de línea' in stream.getvalue() and 'https://' in stream.getvalue()


def test_placeholders_are_explained_even_in_quick_mode():
    stream = io.StringIO()
    Renderer('en', stream).tool(load_catalog().get('ssh'), quick=True)
    assert 'omit the angle brackets' in stream.getvalue()
