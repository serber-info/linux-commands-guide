from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de HEAD"
TITLE_EN = "HEAD Options"
BRIEF = "Muestra el inicio de un archivo"
BRIEF_EN = "Display the beginning of a file"

COMMANDS = [
    {"command": f"{Color.GREEN}head{Color.RESET} filename", "description": "Muestra las primeras 10 líneas del archivo", "description_en": "Show the first 10 lines of the file"},
    {"command": f"{Color.GREEN}head{Color.RESET} -n N filename", "description": "Muestra las primeras N líneas", "description_en": "Show the first N lines"},
    {"command": f"{Color.GREEN}head{Color.RESET} -c N filename", "description": "Muestra los primeros N bytes", "description_en": "Show the first N bytes"},
    {"command": f"{Color.GREEN}head{Color.RESET} -q file1 file2", "description": "Suprime los encabezados de archivo en la salida", "description_en": "Suppress file headers in output"},
    {"command": f"{Color.GREEN}head{Color.RESET} -v filename", "description": "Muestra siempre el encabezado del archivo", "description_en": "Always show file header"},
    {"command": f"{Color.GREEN}head{Color.RESET} --lines=N filename", "description": "Igual que -n N", "description_en": "Same as -n N"},
    {"command": f"{Color.GREEN}head{Color.RESET} --bytes=N filename", "description": "Igual que -c N", "description_en": "Same as -c N"},
    {"command": f"{Color.GREEN}head{Color.RESET} -z filename", "description": "Usa NUL como terminador en lugar de nueva línea", "description_en": "Use NUL as line delimiter instead of newline"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
