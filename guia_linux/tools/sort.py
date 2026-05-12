from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de SORT"
TITLE_EN = "SORT Options"
BRIEF = "Ordena líneas de texto"
BRIEF_EN = "Sort lines of text"

COMMANDS = [
    {"command": f"{Color.GREEN}sort{Color.RESET} filename", "description": "Ordena las líneas alfabéticamente", "description_en": "Sort lines alphabetically"},
    {"command": f"{Color.GREEN}sort{Color.RESET} -n filename", "description": "Ordena las líneas numéricamente", "description_en": "Sort lines numerically"},
    {"command": f"{Color.GREEN}sort{Color.RESET} -r filename", "description": "Ordena en orden inverso", "description_en": "Sort in reverse order"},
    {"command": f"{Color.GREEN}sort{Color.RESET} -u filename", "description": "Elimina duplicados y ordena", "description_en": "Remove duplicates and sort"},
    {"command": f"{Color.GREEN}sort{Color.RESET} -k2,2 -n filename", "description": "Ordena numéricamente por la segunda columna", "description_en": "Sort numerically by the second column"},
    {"command": f"{Color.GREEN}sort{Color.RESET} -t',' -k1,1 filename", "description": "Ordena por el primer campo con ',' como delimitador", "description_en": "Sort by first field using ',' as delimiter"},
    {"command": f"{Color.GREEN}sort{Color.RESET} -m file1 file2", "description": "Combina y ordena archivos ya ordenados", "description_en": "Merge already-sorted files"},
    {"command": f"{Color.GREEN}sort{Color.RESET} -h filename", "description": "Ordena tamaños legibles (1K, 2M, 3G)", "description_en": "Sort human-readable sizes (1K, 2M, 3G)"},
    {"command": f"{Color.GREEN}sort{Color.RESET} -f filename", "description": "Ignora mayúsculas/minúsculas en el ordenamiento", "description_en": "Ignore case when sorting"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
