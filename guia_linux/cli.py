#!/usr/bin/env python3
"""Small CLI seam: references and lessons, never a command runner."""
import argparse
import difflib
import os
import sys

from guia_linux import __version__
from guia_linux.catalog import CATEGORIES, load_catalog
from guia_linux.render import Renderer, safe_text


def default_lang() -> str:
    for var in ('LC_ALL', 'LC_MESSAGES', 'LANG', 'LANGUAGE'):
        value = os.environ.get(var)
        if value:
            return 'es' if value.lower().startswith('es') else 'en'
    return 'en'


def _help(r, catalog):
    r.header(r.label('Guía de Comandos Linux', 'Linux Command Reference'))
    r.paragraph(r.label('Empieza: lh ls --quick → lh grep --explain → lh learn pipes',
                        'Start: lh ls --quick → lh grep --explain → lh learn pipes'))
    r.paragraph(r.label('Referencia local. No ejecuta los ejemplos.', 'Offline reference. Examples are not executed.'))
    r.section(r.label('Uso', 'Usage'))
    for line in ('lh <tool> [--quick | --explain]', 'lh -s <words> [--lang es|en]',
                 'lh <tool> -s <words>', 'lh list [--category files]', 'lh learn [topic]',
                 'lh practice [topic] [--hint | --solution]', 'lh --version'):
        r.line('  ' + line)
    r.section(r.label('Ejemplos', 'Examples'))
    for line in ('lh awk', "lh -s 'buscar archivos'", 'lh practice grep', 'lh --lang en ssh'):
        r.line('  ' + line)
    r.listing(catalog.list())
    r.line()


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(prog='lh', add_help=False, allow_abbrev=False)
    parser.add_argument('tool', nargs='?')
    parser.add_argument('topic', nargs='?')
    parser.add_argument('-s', '--search', metavar='WORDS')
    parser.add_argument('--lang', choices=('es', 'en'))
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--quick', action='store_true')
    mode.add_argument('--explain', action='store_true')
    parser.add_argument('--category', choices=CATEGORIES)
    practice_mode = parser.add_mutually_exclusive_group()
    practice_mode.add_argument('--hint', action='store_true')
    practice_mode.add_argument('--solution', action='store_true')
    parser.add_argument('-h', '--help', action='store_true')
    parser.add_argument('-V', '--version', action='version', version=f'lh (linux-commands-guide) {__version__}')
    args = parser.parse_args(argv)
    r = Renderer(args.lang or default_lang())
    if args.topic and args.tool not in {'learn', 'practice'}:
        parser.error(r.label('El segundo nombre solo se usa con learn/practice.', 'A second name is only valid with learn/practice.'))
    if args.category and args.tool != 'list':
        parser.error(r.label('--category requiere lh list.', '--category requires lh list.'))
    if (args.hint or args.solution) and (args.tool != 'practice' or not args.topic):
        parser.error(r.label('--hint/--solution requieren lh practice <topic>.', '--hint/--solution require lh practice <topic>.'))
    if (args.quick or args.explain) and (not args.tool or args.tool in {'list', 'learn', 'practice'} or args.search is not None):
        parser.error(r.label('--quick/--explain requieren una herramienta y no una búsqueda.', '--quick/--explain require a tool, not a search.'))
    if args.search is not None and (not args.search.strip() or args.tool in {'list', 'learn', 'practice'}):
        parser.error(r.label('Usa palabras de búsqueda con una herramienta o sin nombre.', 'Use search words with a tool or without a name.'))
    catalog = load_catalog()
    if args.help or (args.tool is None and args.search is None):
        _help(r, catalog)
        return
    if args.tool == 'list':
        r.header(r.label('Herramientas por categoría', 'Tools by category'))
        r.listing(catalog.list(args.category))
        return
    if args.tool in {'learn', 'practice'}:
        from guia_linux.learning import show_learning
        try:
            show_learning(args.tool, args.topic, r, args.hint, args.solution)
        except KeyError:
            print(r.label('Tema desconocido; usa lh ', 'Unknown topic; use lh ') + args.tool, file=sys.stderr)
            raise SystemExit(1) from None
        return
    tool = None
    if args.tool:
        try:
            tool = catalog.get(args.tool)
        except KeyError:
            message = r.label(f"Herramienta '{safe_text(args.tool)}' no encontrada", f"Tool '{safe_text(args.tool)}' not found")
            matches = difflib.get_close_matches(args.tool.lower(), catalog.tools, n=3, cutoff=0.65)
            if matches:
                message += r.label('. Quizás: ', '. Perhaps: ') + ', '.join(matches)
            print(message + ' — lh --help', file=sys.stderr)
            raise SystemExit(1) from None
    if args.search is not None:
        r.search(args.search, catalog.search(args.search, tool.name if tool else None))
    else:
        r.tool(tool, args.quick, args.explain)


def run() -> None:
    """Console entry point, quiet when a downstream pipe closes early."""
    try:
        main()
        sys.stdout.flush()
    except BrokenPipeError:
        devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull, sys.stdout.fileno())
        os.close(devnull)
        raise SystemExit(141) from None


if __name__ == '__main__':
    run()
