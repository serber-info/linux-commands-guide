import re
from shellcolorize import Color

_ANSI_RE = re.compile(r'\033\[[0-9;]*m')


def strip_ansi(text: str) -> str:
    return _ANSI_RE.sub('', text)


def ansi_ljust(text: str, width: int) -> str:
    visible = len(strip_ansi(text))
    return text + ' ' * max(0, width - visible)


def print_table(title: str, commands: list, lang: str = "es") -> None:
    desc_key = "description_en" if lang == "en" else "description"
    cmd_label = "Command" if lang == "en" else "Comando"
    desc_label = "Description" if lang == "en" else "Descripción"
    sep = "-" * 132

    print(f"\n{Color.CYAN}{Color.BOLD}{title}{Color.RESET}:\n")
    print(f"{cmd_label:<50} | {desc_label}")
    print(sep)

    for entry in commands:
        # Section / category headers
        if "section" in entry or "category" in entry:
            key = "section" if "section" in entry else "category"
            text = entry.get(f"{key}_en" if lang == "en" else key, entry.get(key, ""))
            if text:
                print(f"\n{Color.CYAN}{strip_ansi(str(text))}{Color.RESET}")
                print(sep)
            continue

        display = entry.get("command") or entry.get("logfile") or entry.get("pattern") or ""
        desc = entry.get(desc_key, "")

        if display or desc:
            print(f"{ansi_ljust(str(display), 59)} | {Color.RED}{desc}{Color.RESET}")


def search_all(query: str, tools: dict, lang: str = "es") -> list:
    desc_key = "description_en" if lang == "en" else "description"
    results = []
    q = query.lower()
    for tool_name, module in tools.items():
        for entry in getattr(module, 'COMMANDS', []):
            if "section" in entry or "category" in entry:
                continue
            display = strip_ansi(str(
                entry.get("command") or
                entry.get("logfile") or
                entry.get("pattern") or ""
            ))
            desc = entry.get(desc_key, "")
            if q in display.lower() or q in desc.lower():
                results.append((tool_name, entry))
    return results
