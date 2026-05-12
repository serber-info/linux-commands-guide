#!/usr/bin/env python3
import argparse
import sys
from shellcolorize import Color
from guia_linux.tools import TOOLS
from guia_linux.utils import search_all, strip_ansi


def _print_help(lang: str) -> None:
    if lang == "en":
        print(f"\n{Color.CYAN}{Color.BOLD}Linux Command Reference{Color.RESET} — usage:\n")
        print(f"  {Color.GREEN}lh{Color.RESET} <tool>              Show commands for a tool")
        print(f"  {Color.GREEN}lh{Color.RESET} -s <keyword>        Search across all tools")
        print(f"  {Color.GREEN}lh{Color.RESET} --lang en <tool>    Force English output")
        print(f"  {Color.GREEN}lh{Color.RESET} --lang es <tool>    Force Spanish output\n")
    else:
        print(f"\n{Color.CYAN}{Color.BOLD}Guía de Comandos Linux{Color.RESET} — uso:\n")
        print(f"  {Color.GREEN}lh{Color.RESET} <herramienta>        Muestra comandos de una herramienta")
        print(f"  {Color.GREEN}lh{Color.RESET} -s <término>         Busca en todas las herramientas")
        print(f"  {Color.GREEN}lh{Color.RESET} --lang en <tool>     Fuerza salida en inglés")
        print(f"  {Color.GREEN}lh{Color.RESET} --lang es <tool>     Fuerza salida en español\n")

    label_tool = "Tool" if lang == "en" else "Herramienta"
    label_desc = "Description" if lang == "en" else "Descripción"
    print(f"  {Color.YELLOW}{label_tool:<16}{label_desc}{Color.RESET}")
    print(f"  {'-' * 60}")
    for name, module in sorted(TOOLS.items()):
        desc = getattr(module, 'TITLE_EN' if lang == 'en' else 'TITLE', name.upper())
        brief = getattr(module, 'BRIEF_EN' if lang == 'en' else 'BRIEF', '')
        print(f"  {Color.GREEN}{name:<16}{Color.RESET}{brief}")
    print()


def _search(query: str, lang: str) -> None:
    results = search_all(query, TOOLS, lang)
    desc_key = "description_en" if lang == "en" else "description"
    if not results:
        msg = f"No results for '{query}'" if lang == "en" else f"Sin resultados para '{query}'"
        print(f"\n{Color.RED}{msg}{Color.RESET}\n")
        return

    header = f"Results for '{query}'" if lang == "en" else f"Resultados para '{query}'"
    print(f"\n{Color.CYAN}{Color.BOLD}{header}{Color.RESET} ({len(results)}):\n")
    current_tool = None
    for tool_name, entry in results:
        if tool_name != current_tool:
            print(f"\n  {Color.YELLOW}[{tool_name}]{Color.RESET}")
            current_tool = tool_name
        display = str(entry.get("command") or entry.get("logfile") or entry.get("pattern") or "")
        desc = entry.get(desc_key, "")
        clean = strip_ansi(display)
        print(f"    {Color.GREEN}{clean}{Color.RESET}")
        print(f"      {Color.RED}{desc}{Color.RESET}")
    print()


def main() -> None:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("tool", nargs="?", default=None)
    parser.add_argument("-s", "--search", metavar="KEYWORD", default=None)
    parser.add_argument("--lang", choices=["es", "en"], default="es")
    parser.add_argument("-h", "--help", action="store_true")
    args = parser.parse_args()

    lang = args.lang

    if args.help or (args.tool is None and args.search is None):
        _print_help(lang)
        return

    if args.search:
        _search(args.search, lang)
        return

    tool_key = args.tool.lower()
    if tool_key not in TOOLS:
        msg = (
            f"Tool '{args.tool}' not found. Run 'lh --help' for the full list."
            if lang == "en"
            else f"Herramienta '{args.tool}' no encontrada. Ejecuta 'lh --help' para ver la lista."
        )
        print(f"\n{Color.RED}{msg}{Color.RESET}\n")
        sys.exit(1)

    TOOLS[tool_key].show(lang)


if __name__ == "__main__":
    main()
