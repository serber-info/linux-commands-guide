"""Terminal presentation with stream-local colors; never global Color.auto()."""
import shutil
import re
import sys
import textwrap

from shellcolorize import Color, supports_color

CATEGORY_NAMES = {
    'basics': ('Empieza aquí', 'Start here'), 'files': ('Archivos', 'Files'),
    'text': ('Texto y búsqueda', 'Text and search'), 'shell': ('Shell y terminal', 'Shell and terminal'),
    'processes': ('Procesos', 'Processes'), 'system': ('Sistema', 'System'),
    'network': ('Red', 'Network'), 'development': ('Desarrollo', 'Development'),
    'advanced': ('Administración avanzada', 'Advanced administration'),
}
EFFECT_NAMES = {
    'reference': ('Referencia; revisa contexto y permisos', 'Reference; review context and permissions'),
    'write': ('Modifica archivos o estado', 'Changes files or state'),
    'delete': ('Borra o descarta datos; no hay deshacer garantizado', 'Deletes or discards data; no guaranteed undo'),
    'network': ('Genera tráfico o conexiones', 'Generates traffic or connections'),
    'admin': ('Afecta procesos, red o sistema; revisa privilegios', 'Affects processes, networking or system; review privileges'),
    'sensitive': ('Puede exponer datos o reducir protecciones', 'May reveal data or weaken protections'),
}


def safe_text(text):
    """Do not let user-provided control sequences reach the terminal."""
    return ''.join(c if c.isprintable() else repr(c)[1:-1] for c in text)


class Renderer:
    def __init__(self, lang='es', stream=None, width=None):
        self.lang = lang
        self.stream = sys.stdout if stream is None else stream
        self.width = max(24, width if width is not None else shutil.get_terminal_size((100, 24)).columns)
        self.colors = supports_color(self.stream)

    def label(self, es, en):
        return en if self.lang == 'en' else es

    def paint(self, text, *styles):
        return ''.join(styles) + text + Color.RESET if self.colors else text

    def line(self, text=''):
        print(text, file=self.stream)

    def paragraph(self, text, indent='  '):
        for paragraph in text.splitlines():
            self.line(textwrap.fill(paragraph, max(12, self.width - len(indent)), initial_indent=indent,
                                    subsequent_indent=indent, break_long_words=False, break_on_hyphens=False))

    def header(self, title):
        title = safe_text(title)
        inner = min(max(46, len(title) + 6), self.width - 4)
        self.line()
        self.line(self.paint('  ╔' + '═' * inner + '╗', Color.CYAN))
        for line in textwrap.wrap(title, inner - 4, break_long_words=True, break_on_hyphens=False):
            self.line(self.paint('  ║  ' + line.ljust(inner - 4) + '  ║', Color.CYAN))
        self.line(self.paint('  ╚' + '═' * inner + '╝', Color.CYAN))
        self.line()

    def section(self, text):
        self.line()
        self.paragraph('▶ ' + text)

    def example(self, entry, explain=False):
        if entry.kind == 'section':
            self.section(entry.description.in_lang(self.lang))
            return
        desc = entry.description.in_lang(self.lang)
        # Commands are never reflowed: copying must not change their syntax.
        if not explain and self.width >= 96 and len(entry.text) <= 50:
            self.line('  ' + self.paint(entry.text.ljust(50), Color.GREEN) + '  ' + self.paint(desc, Color.DIM))
        else:
            self.line('  ' + self.paint(entry.text, Color.GREEN))
            self.paragraph(desc, '    ')
        if entry.effect != 'reference':
            self.paragraph(self.label('Atención: ', 'Caution: ') + self.label(*EFFECT_NAMES[entry.effect]), '    ')
        if explain and entry.explanation:
            self.paragraph(entry.explanation.in_lang(self.lang), '    ')
        if explain and entry.output:
            self.paragraph(self.label('Salida de ejemplo:', 'Example output:'), '    ')
            for line in entry.output.splitlines():
                self.line('      ' + line)
        if explain:
            self.line()

    def tool(self, tool, quick=False, explain=False):
        self.header(tool.title.in_lang(self.lang))
        if not quick:
            self.paragraph(tool.notes.in_lang(self.lang))
            self.line()
        examples = [e for e in tool.examples if e.quick and e.kind != 'section'][:8] if quick or explain else tool.examples
        if any(re.search(r'<[A-Za-z][A-Za-z0-9_/-]*>', e.text) for e in examples):
            self.paragraph(self.label('Sustituye los valores entre < > y no escribas esos símbolos.',
                                      'Replace values inside < > and omit the angle brackets.'))
        self.paragraph(self.label('Comando · Descripción', 'Command · Description'))
        self.line('  ' + '─' * min(94, self.width - 4))
        for entry in examples:
            self.example(entry, explain)
        self.line()
        if quick:
            self.paragraph(self.label(f'Más: lh {tool.name} --explain · lh {tool.name}',
                                      f'More: lh {tool.name} --explain · lh {tool.name}'))
        if explain:
            if tool.related:
                self.paragraph(self.label('Relacionado: ', 'Related: ') + ' · '.join(tool.related))
            self.paragraph(self.label('Fuentes:', 'Sources:'))
            for source in tool.sources:
                self.paragraph(source)

    def listing(self, tools):
        for category in CATEGORY_NAMES:
            group = [t for t in tools if t.category == category]
            if not group:
                continue
            self.section(self.label(*CATEGORY_NAMES[category]))
            for tool in group:
                if self.width >= 80:
                    self.line('  ' + self.paint(tool.name.ljust(18), Color.GREEN) + tool.brief.in_lang(self.lang))
                else:
                    self.line('  ' + self.paint(tool.name, Color.GREEN))
                    self.paragraph(tool.brief.in_lang(self.lang), '    ')

    def search(self, query, results):
        self.header(self.label('Búsqueda: ', 'Search: ') + query)
        self.paragraph(self.label(f'{len(results)} resultados', f'{len(results)} results'))
        current = None
        for tool, entry in results:
            if current != tool.name:
                self.section(tool.name)
                current = tool.name
            self.example(entry)
        if not results:
            self.paragraph(self.label('Prueba menos palabras o lh list para explorar categorías.',
                                      'Try fewer words or lh list to browse categories.'))
        self.line()
