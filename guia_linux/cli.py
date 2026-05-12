#!/usr/bin/env python3
import argparse
import sys
from shellcolorize import Color
from guia_linux.tools import TOOLS
from guia_linux.utils import search_all, strip_ansi


def _help_header(lang: str) -> None:
    title = 'Linux Command Reference' if lang == 'en' else 'Guía de Comandos Linux'
    w = max(46, len(title) + 6)
    border = '═' * w
    print()
    print(f"  {Color.CYAN}╔{border}╗{Color.RESET}")
    print(f"  {Color.CYAN}║{Color.RESET}  {Color.BOLD}{Color.CYAN}{title}{Color.RESET}"
          + ' ' * max(0, w - len(title) - 2)
          + f"  {Color.CYAN}║{Color.RESET}")
    print(f"  {Color.CYAN}╚{border}╝{Color.RESET}")


def _print_help(lang: str) -> None:
    _help_header(lang)

    if lang == 'en':
        print(f"""
  {Color.BOLD}Usage{Color.RESET}
    {Color.GREEN}lh{Color.RESET} <tool>                  Show commands for a tool
    {Color.GREEN}lh{Color.RESET} <tool> --lang en         Force English output
    {Color.GREEN}lh{Color.RESET} -s <keyword>             Search across all tools
    {Color.GREEN}lh{Color.RESET} -s <keyword> --lang en   Search with English descriptions

  {Color.BOLD}Examples{Color.RESET}
    {Color.GREEN}lh grep{Color.RESET}                     All grep options
    {Color.GREEN}lh --lang en docker{Color.RESET}         Docker commands in English
    {Color.GREEN}lh -s recursive{Color.RESET}             Find every command mentioning "recursive"
""")
    else:
        print(f"""
  {Color.BOLD}Uso{Color.RESET}
    {Color.GREEN}lh{Color.RESET} <herramienta>              Muestra comandos de una herramienta
    {Color.GREEN}lh{Color.RESET} <herramienta> --lang es    Fuerza salida en español
    {Color.GREEN}lh{Color.RESET} -s <término>               Busca en todas las herramientas
    {Color.GREEN}lh{Color.RESET} -s <término> --lang en     Busca con descripciones en inglés

  {Color.BOLD}Ejemplos{Color.RESET}
    {Color.GREEN}lh grep{Color.RESET}                       Todas las opciones de grep
    {Color.GREEN}lh --lang en docker{Color.RESET}           Comandos docker en inglés
    {Color.GREEN}lh -s recursivo{Color.RESET}               Busca comandos con "recursivo"
""")

    label = 'Tool' if lang == 'en' else 'Herramienta'
    desc  = 'Description' if lang == 'en' else 'Descripción'
    print(f"  {Color.BOLD}{Color.GREEN}{label:<18}{desc}{Color.RESET}")
    print(f"  {Color.DIM}{'─' * 60}{Color.RESET}")
    for name, module in sorted(TOOLS.items()):
        brief = getattr(module, 'BRIEF_EN' if lang == 'en' else 'BRIEF', '')
        print(f"  {Color.GREEN}{name:<18}{Color.RESET}{Color.DIM}{brief}{Color.RESET}")
    print()


def _search(query: str, lang: str) -> None:
    results  = search_all(query, TOOLS, lang)
    desc_key = 'description_en' if lang == 'en' else 'description'

    w = 50
    border = '═' * w
    header = f"Search: {query}" if lang == 'en' else f"Búsqueda: {query}"
    count  = f'{len(results)} result{"s" if len(results) != 1 else ""}' if lang == 'en' \
             else f'{len(results)} resultado{"s" if len(results) != 1 else ""}'

    print()
    print(f"  {Color.CYAN}╔{border}╗{Color.RESET}")
    print(f"  {Color.CYAN}║{Color.RESET}  {Color.BOLD}{Color.CYAN}{header}{Color.RESET}"
          + ' ' * max(0, w - len(header) - 2)
          + f"  {Color.CYAN}║{Color.RESET}")
    print(f"  {Color.CYAN}╚{border}╝{Color.RESET}")

    if not results:
        msg = f"No results for '{query}'" if lang == 'en' else f"Sin resultados para '{query}'"
        print(f"\n  {Color.DIM}{msg}{Color.RESET}\n")
        return

    print(f"\n  {Color.DIM}{count}{Color.RESET}\n")

    current_tool = None
    for tool_name, entry in results:
        if tool_name != current_tool:
            print(f"  {Color.CYAN}▶  {Color.BOLD}{tool_name}{Color.RESET}")
            current_tool = tool_name
        display = strip_ansi(str(
            entry.get('command') or entry.get('logfile') or entry.get('pattern') or ''
        ))
        desc = entry.get(desc_key, '')
        print(f"    {Color.GREEN}{display}{Color.RESET}")
        print(f"    {Color.DIM}{desc}{Color.RESET}")
    print()


def main() -> None:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('tool', nargs='?', default=None)
    parser.add_argument('-s', '--search', metavar='KEYWORD', default=None)
    parser.add_argument('--lang', choices=['es', 'en'], default='es')
    parser.add_argument('-h', '--help', action='store_true')
    args = parser.parse_args()

    lang = args.lang

    if args.help or (args.tool is None and args.search is None):
        _print_help(lang)
        return

    if args.search:
        _search(args.search, lang)
        return

    key = args.tool.lower()
    if key not in TOOLS:
        msg = (f"Tool '{args.tool}' not found — run 'lh --help' for the full list."
               if lang == 'en'
               else f"Herramienta '{args.tool}' no encontrada — ejecuta 'lh --help' para ver la lista.")
        print(f"\n  {Color.RED}✖  {msg}{Color.RESET}\n")
        sys.exit(1)

    TOOLS[key].show(lang)


if __name__ == '__main__':
    main()
