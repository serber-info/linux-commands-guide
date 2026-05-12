from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de UNIQ"
TITLE_EN = "UNIQ Options"
BRIEF = "Filtra líneas duplicadas adyacentes"
BRIEF_EN = "Filter adjacent duplicate lines"

COMMANDS = [
    {"command": f"{Color.GREEN}uniq{Color.RESET} filename", "description": "Elimina líneas duplicadas consecutivas", "description_en": "Remove consecutive duplicate lines"},
    {"command": f"{Color.GREEN}uniq{Color.RESET} -c filename", "description": "Cuenta las ocurrencias de cada línea", "description_en": "Count occurrences of each line"},
    {"command": f"{Color.GREEN}uniq{Color.RESET} -d filename", "description": "Muestra solo las líneas duplicadas", "description_en": "Show only duplicate lines"},
    {"command": f"{Color.GREEN}uniq{Color.RESET} -u filename", "description": "Muestra solo las líneas únicas (no duplicadas)", "description_en": "Show only unique (non-duplicated) lines"},
    {"command": f"{Color.GREEN}uniq{Color.RESET} -i filename", "description": "Ignora mayúsculas/minúsculas al comparar", "description_en": "Ignore case when comparing"},
    {"command": f"{Color.GREEN}sort{Color.RESET} filename | {Color.GREEN}uniq{Color.RESET}", "description": "Patrón habitual: ordenar antes de aplicar uniq", "description_en": "Common pattern: sort first, then apply uniq"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
