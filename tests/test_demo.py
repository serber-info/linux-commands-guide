"""Check the published demo assets without requiring GIF tools in CI."""
import json
import re
from pathlib import Path
import struct

from scripts.record_demo import SCENES

ROOT = Path(__file__).resolve().parents[1]


def test_recording_has_real_scene_output_and_no_private_identifiers():
    rows = [json.loads(line) for line in (ROOT / 'docs/demo.cast').read_text().splitlines()]
    assert rows[0]['version'] == 2
    assert (rows[0]['width'], rows[0]['height']) == (96, 36)
    events = rows[1:]
    assert all(a[0] <= b[0] for a, b in zip(events, events[1:]))
    assert 30 <= events[-1][0] <= 90
    output = ''.join(e[2] for e in events if e[1] == 'o')
    for expected in ('ls reference', 'Búsqueda: espacio disco', 'CHMOD Options',
                     'Conectar comandos con tuberías', 'Practice', 'Find errors in a log', 'Uso de ls'):
        assert expected in output
    assert not re.search(r'/home/(?!demo(?:/|\b))[^/\s\x1b]+', output)
    assert 'Traceback' not in output
    assert 'demo' in output
    for index, (command, _) in enumerate(SCENES):
        assert command.startswith(f"lh --lang {'en' if index % 2 == 0 else 'es'} ")
        assert command in output


def test_gif_is_animated_sized_and_embedded():
    data = (ROOT / 'docs/demo.gif').read_bytes()
    assert data[:6] in (b'GIF87a', b'GIF89a')
    assert struct.unpack('<HH', data[6:10]) == (1062, 766)
    assert data.count(b'\x21\xf9\x04') > 10
    assert b'NETSCAPE2.0' in data
    assert len(data) < 2 * 1024 * 1024
    readme = (ROOT / 'README.md').read_text()
    assert 'src="docs/demo.gif"' in readme and 'previous compact reference' not in readme
    for spanish in ('Aprende Linux', 'Empieza aquí', 'Reproducir', 'Fichas disponibles', ' / fichas', 'Contribuir'):
        assert spanish not in readme
