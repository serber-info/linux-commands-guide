import re
from shellcolorize import Color

_ANSI = re.compile(r'\033\[[0-9;]*m')


def strip_ansi(text: str) -> str:
    return _ANSI.sub('', text)


def ansi_ljust(text: str, width: int) -> str:
    """Pad text to visible width, ignoring ANSI escape codes."""
    visible = len(strip_ansi(text))
    return text + ' ' * max(0, width - visible)


# ── Shared visual primitives ──────────────────────────────────────────────────

def _header(title: str) -> None:
    w = max(46, len(title) + 6)
    border = '═' * w
    print()
    print(f"  {Color.CYAN}╔{border}╗{Color.RESET}")
    print(f"  {Color.CYAN}║{Color.RESET}  {Color.BOLD}{Color.CYAN}{title}{Color.RESET}"
          + ' ' * max(0, w - len(title) - 2)
          + f"  {Color.CYAN}║{Color.RESET}")
    print(f"  {Color.CYAN}╚{border}╝{Color.RESET}")
    print()


def _column_headers(cmd_label: str, desc_label: str, cmd_width: int = 50) -> None:
    print(f"  {Color.BOLD}{Color.GREEN}{cmd_label:<{cmd_width}}{Color.RESET}"
          f"  {Color.BOLD}{Color.GREEN}{desc_label}{Color.RESET}")
    print(f"  {Color.DIM}{'─' * (cmd_width + 2 + 42)}{Color.RESET}")


def _section(text: str) -> None:
    print()
    print(f"  {Color.CYAN}▶  {Color.BOLD}{text}{Color.RESET}")
    print(f"  {Color.DIM}{'─' * 94}{Color.RESET}")


# ── Main table printer ────────────────────────────────────────────────────────

def print_table(title: str, commands: list, lang: str = 'es') -> None:
    desc_key   = 'description_en' if lang == 'en' else 'description'
    cmd_label  = 'Command'     if lang == 'en' else 'Comando'
    desc_label = 'Description' if lang == 'en' else 'Descripción'
    CMD_WIDTH  = 50

    _header(title)
    has_sections = any('section' in e or 'category' in e for e in commands)

    if not has_sections:
        _column_headers(cmd_label, desc_label, CMD_WIDTH)

    for entry in commands:
        # ── Section / category header ──────────────────────────────────────
        if 'section' in entry or 'category' in entry:
            key  = 'section' if 'section' in entry else 'category'
            text = entry.get(f'{key}_en' if lang == 'en' else key, entry.get(key, ''))
            if text:
                if not any(e for e in commands[:commands.index(entry)]
                           if 'section' in e or 'category' in e):
                    _column_headers(cmd_label, desc_label, CMD_WIDTH)
                _section(strip_ansi(str(text)))
            continue

        display = entry.get('command') or entry.get('logfile') or entry.get('pattern') or ''
        desc    = entry.get(desc_key, '')

        if display or desc:
            padded = ansi_ljust(str(display), CMD_WIDTH)
            print(f"  {padded}  {Color.DIM}{desc}{Color.RESET}")

    print()


# ── Cross-tool search ─────────────────────────────────────────────────────────

def search_all(query: str, tools: dict, lang: str = 'es') -> list:
    desc_key = 'description_en' if lang == 'en' else 'description'
    results  = []
    q        = query.lower()
    for tool_name, module in tools.items():
        for entry in getattr(module, 'COMMANDS', []):
            if 'section' in entry or 'category' in entry:
                continue
            display = strip_ansi(str(
                entry.get('command') or
                entry.get('logfile') or
                entry.get('pattern') or ''
            ))
            desc = entry.get(desc_key, '')
            if q in display.lower() or q in desc.lower():
                results.append((tool_name, entry))
    return results
