from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Atajos de teclado en la terminal"
TITLE_EN = "Terminal Keyboard Shortcuts"
BRIEF = "Atajos de teclado de bash/zsh"
BRIEF_EN = "Bash/zsh keyboard shortcuts"

COMMANDS = [
    {"command": f"{Color.GREEN}[TAB]{Color.RESET}", "description": "Autocompleta comandos, rutas y opciones", "description_en": "Autocomplete commands, paths and options"},
    {"command": f"{Color.GREEN}[CTRL] + A{Color.RESET}", "description": "Mueve el cursor al inicio de la línea", "description_en": "Move cursor to beginning of line"},
    {"command": f"{Color.GREEN}[CTRL] + E{Color.RESET}", "description": "Mueve el cursor al final de la línea", "description_en": "Move cursor to end of line"},
    {"command": f"{Color.GREEN}[CTRL] + ← / →{Color.RESET}", "description": "Salta a la palabra anterior/siguiente", "description_en": "Jump to previous/next word"},
    {"command": f"{Color.GREEN}[ALT] + B / F{Color.RESET}", "description": "Retrocede/avanza una palabra", "description_en": "Move backward/forward one word"},
    {"command": f"{Color.GREEN}[CTRL] + U{Color.RESET}", "description": "Elimina desde el cursor al inicio de línea", "description_en": "Delete from cursor to beginning of line"},
    {"command": f"{Color.GREEN}[CTRL] + K{Color.RESET}", "description": "Elimina desde el cursor al final de línea", "description_en": "Delete from cursor to end of line"},
    {"command": f"{Color.GREEN}[CTRL] + W{Color.RESET}", "description": "Elimina la palabra anterior al cursor", "description_en": "Delete the word before the cursor"},
    {"command": f"{Color.GREEN}[CTRL] + Y{Color.RESET}", "description": "Pega el último texto eliminado (yank)", "description_en": "Paste the last deleted text (yank)"},
    {"command": f"{Color.GREEN}[CTRL] + C{Color.RESET}", "description": "Termina el proceso en ejecución (SIGINT)", "description_en": "Terminate the running process (SIGINT)"},
    {"command": f"{Color.GREEN}[CTRL] + D{Color.RESET}", "description": "Cierra stdin (EOF) / sale del shell", "description_en": "Close stdin (EOF) / exit the shell"},
    {"command": f"{Color.GREEN}[CTRL] + L{Color.RESET}", "description": "Limpia la terminal (equivale a 'clear')", "description_en": "Clear the terminal (same as 'clear')"},
    {"command": f"{Color.GREEN}[CTRL] + Z{Color.RESET}", "description": "Suspende el proceso actual (SIGTSTP)", "description_en": "Suspend the current process (SIGTSTP)"},
    {"command": f"{Color.GREEN}[CTRL] + R{Color.RESET}", "description": "Busca en el historial de comandos", "description_en": "Search command history"},
    {"command": f"{Color.GREEN}[↑] / [↓]{Color.RESET}", "description": "Navega por el historial de comandos", "description_en": "Navigate command history"},
    {"command": f"{Color.GREEN}[CTRL] + [+]{Color.RESET}", "description": "Aumenta el zoom del terminal", "description_en": "Increase terminal zoom"},
    {"command": f"{Color.GREEN}[CTRL] + [-]{Color.RESET}", "description": "Disminuye el zoom del terminal", "description_en": "Decrease terminal zoom"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
