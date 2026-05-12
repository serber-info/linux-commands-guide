from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de CUT"
TITLE_EN = "CUT Options"
BRIEF = "Extrae secciones de cada línea"
BRIEF_EN = "Extract sections from each line"

COMMANDS = [
    {"command": f"{Color.GREEN}cut{Color.RESET} -d',' -f2 filename", "description": "Extrae la 2ª columna usando ',' como delimitador", "description_en": "Extract 2nd column using ',' as delimiter"},
    {"command": f"{Color.GREEN}cut{Color.RESET} -f1,3 filename", "description": "Extrae la 1ª y 3ª columna (tabulación)", "description_en": "Extract 1st and 3rd column (tab-delimited)"},
    {"command": f"{Color.GREEN}cut{Color.RESET} -c1-5 filename", "description": "Extrae los primeros 5 caracteres de cada línea", "description_en": "Extract the first 5 characters of each line"},
    {"command": f"{Color.GREEN}cut{Color.RESET} -d':' -f1 /etc/passwd", "description": "Extrae el primer campo de /etc/passwd", "description_en": "Extract the first field from /etc/passwd"},
    {"command": f"{Color.GREEN}cut{Color.RESET} -d' ' -f1-3 filename", "description": "Extrae los tres primeros campos separados por espacio", "description_en": "Extract the first three space-separated fields"},
    {"command": f"{Color.GREEN}cut{Color.RESET} -s -d',' -f2 filename", "description": "Muestra solo líneas que contienen el delimitador", "description_en": "Show only lines containing the delimiter"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
