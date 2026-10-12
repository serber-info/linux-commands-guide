"""Display local lessons and practice plans. Never execute commands or inspect user files."""
import json
import re
import shlex
from functools import lru_cache
from importlib.resources import files

from guia_linux.catalog import _clean, _fields, _strings, _text


@lru_cache(maxsize=2)
def load_learning(mode):
    if mode not in {'learn', 'practice'}:
        raise ValueError('Unknown learning mode')
    directory = 'topics' if mode == 'learn' else 'exercises'
    root = files('guia_linux').joinpath('content').joinpath(directory)
    documents = {}
    for p in sorted(root.iterdir(), key=lambda p: p.name):
        if not p.name.endswith('.json'):
            continue
        data = json.loads(p.read_text(encoding='utf-8'))
        fields = {'name', 'title', 'body', 'commands', 'related', 'sources'} if mode == 'learn' else {'name', 'title', 'task', 'fixtures', 'solution', 'expected', 'hint', 'sources'}
        _fields(data, fields, set(), p.name)
        name = _clean(data['name'], 'name')
        if not re.fullmatch('[a-z0-9-]+', name) or name in documents:
            raise ValueError('Invalid or duplicate topic name')
        _text(data['title'], 'title')
        sources = _strings(data['sources'], 'sources')
        if not sources or any(not s.startswith('https://') for s in sources):
            raise ValueError('HTTPS sources required')
        if mode == 'learn':
            _text(data['body'], 'body')
            _strings(data['commands'], 'commands')
            _strings(data['related'], 'related')
        else:
            _text(data['task'], 'task')
            _text(data['hint'], 'hint')
            _clean(data['solution'], 'solution')
            _clean(data['expected'], 'expected')
            if not isinstance(data['fixtures'], dict) or not data['fixtures']:
                raise ValueError('Exercise fixtures required')
            for path, content in data['fixtures'].items():
                if not re.fullmatch('[A-Za-z0-9][A-Za-z0-9 ._-]*', path) or path in {'.', '..'}:
                    raise ValueError('Fixtures must use plain filenames, never paths')
                _clean(content, 'fixture')
        documents[name] = data
    return documents


def show_learning(mode, topic, renderer, hint=False, solution=False):
    docs = load_learning(mode)
    r = renderer
    if topic is None:
        r.header(r.label('Aprender' if mode == 'learn' else 'Practicar', 'Learn' if mode == 'learn' else 'Practice'))
        for name, doc in docs.items():
            r.paragraph(f"lh {mode} {name} — {doc['title'][r.lang]}")
        if mode == 'learn':
            r.paragraph(r.label('Ruta inicial: navigation → quoting → globs → pipes → redirections → exit-status.',
                                'Start with: navigation → quoting → globs → pipes → redirections → exit-status.'))
        return
    data = docs[topic]
    r.header(data['title'][r.lang])
    if mode == 'learn':
        r.paragraph(data['body'][r.lang])
        r.section(r.label('Ejemplos (lee sus efectos antes de usarlos)', 'Examples (review effects before use)'))
        for command in data['commands']:
            r.line('  ' + command)
        r.paragraph(r.label('Relacionado: ', 'Related: ') + ' · '.join(data['related']))
    else:
        r.paragraph(r.label('lh no ejecuta comandos ni crea archivos. Si quieres practicar, copia la preparación en tu shell. Solo usa el directorio nuevo; no necesitas root.',
                            'lh does not run commands or create files. To practice, copy the setup into your shell. Use only the new directory; root is not needed.'))
        r.section(r.label('Preparación manual (crea archivos de práctica)', 'Manual setup (creates practice files)'))
        r.line('  if workdir=$(mktemp -d -t lh-practice.XXXXXX) && cd "$workdir"; then')
        for filename, content in data['fixtures'].items():
            # printf %s avoids interpreting backslashes/percent signs in fixture content.
            r.line('    printf %s ' + shlex.quote(content) + ' > ' + shlex.quote(filename))
        r.line('  else')
        r.line('    printf "%s\\n" "Practice setup failed / Falló la preparación" >&2')
        r.line('  fi')
        r.section(r.label('Reto', 'Challenge'))
        r.paragraph(data['task'][r.lang])
        r.section(r.label('Resultado esperado (orden o espacios pueden variar)', 'Expected result (order or spacing may vary)'))
        for line in data['expected'].splitlines():
            r.line('  ' + line)
        if hint:
            r.paragraph(data['hint'][r.lang])
        if solution:
            r.section(r.label('Solución', 'Solution'))
            r.line('  ' + data['solution'])
        r.paragraph(f'lh practice {topic} --hint · lh practice {topic} --solution')
        r.paragraph(r.label('Al terminar, sal de esta carpeta con cd ~. lh no la borra automáticamente.',
                            'When finished, leave this folder with cd ~. lh does not delete it automatically.'))
    r.section(r.label('Fuentes', 'Sources'))
    for source in data['sources']:
        r.paragraph(source)
    r.line()
