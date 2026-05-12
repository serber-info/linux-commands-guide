from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de XARGS"
TITLE_EN = "XARGS Options"
BRIEF = "Construye y ejecuta comandos desde stdin"
BRIEF_EN = "Build and execute commands from stdin"

COMMANDS = [
    {"command": f"{Color.GREEN}find{Color.RESET} /path -name '*.log' | {Color.GREEN}xargs{Color.RESET} rm", "description": "Elimina todos los archivos .log encontrados", "description_en": "Delete all found .log files"},
    {"command": f"{Color.GREEN}cat{Color.RESET} list.txt | {Color.GREEN}xargs{Color.RESET} mkdir", "description": "Crea directorios a partir de una lista", "description_en": "Create directories from a list"},
    {"command": f"{Color.GREEN}echo{Color.RESET} 'a b c' | {Color.GREEN}xargs{Color.RESET} -n 1 echo", "description": "Procesa un argumento por vez", "description_en": "Process one argument at a time"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path -print0 | {Color.GREEN}xargs{Color.RESET} -0 ls", "description": "Maneja nombres con espacios usando NUL como separador", "description_en": "Handle filenames with spaces using NUL separator"},
    {"command": f"{Color.GREEN}echo{Color.RESET} 'f1 f2 f3' | {Color.GREEN}xargs{Color.RESET} -I{{}} cp {{}} /dest/", "description": "Sustituye {} por cada argumento", "description_en": "Replace {} with each argument"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path -name '*.py' | {Color.GREEN}xargs{Color.RESET} -P 4 python3", "description": "Ejecuta hasta 4 procesos en paralelo", "description_en": "Run up to 4 processes in parallel"},
    {"command": f"{Color.GREEN}cat{Color.RESET} urls.txt | {Color.GREEN}xargs{Color.RESET} -n 1 curl -O", "description": "Descarga URLs de una en una", "description_en": "Download URLs one at a time"},
    {"command": f"{Color.GREEN}find{Color.RESET} . -name '*.txt' | {Color.GREEN}xargs{Color.RESET} grep 'word'", "description": "Busca 'word' en todos los .txt encontrados", "description_en": "Search for 'word' in all found .txt files"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
