from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de SED"
TITLE_EN = "SED Options"
BRIEF = "Editor de flujo de texto"
BRIEF_EN = "Stream text editor"

COMMANDS = [
    {"command": f"{Color.GREEN}sed{Color.RESET} 's/old/new/g' filename", "description": "Reemplaza todas las ocurrencias de 'old' por 'new'", "description_en": "Replace all occurrences of 'old' with 'new'"},
    {"command": f"{Color.GREEN}sed{Color.RESET} -i 's/old/new/g' filename", "description": "Edita el archivo directamente (in-place)", "description_en": "Edit file in-place"},
    {"command": f"{Color.GREEN}sed{Color.RESET} '1d' filename", "description": "Elimina la primera línea", "description_en": "Delete the first line"},
    {"command": f"{Color.GREEN}sed{Color.RESET} '$d' filename", "description": "Elimina la última línea", "description_en": "Delete the last line"},
    {"command": f"{Color.GREEN}sed{Color.RESET} -n '5,10p' filename", "description": "Muestra solo las líneas de la 5 a la 10", "description_en": "Print only lines 5 through 10"},
    {"command": f"{Color.GREEN}sed{Color.RESET} 's/^/# /' filename", "description": "Añade '#' al inicio de cada línea", "description_en": "Add '#' at the beginning of every line"},
    {"command": f"{Color.GREEN}sed{Color.RESET} '/pattern/d' filename", "description": "Elimina líneas que coinciden con 'pattern'", "description_en": "Delete lines matching 'pattern'"},
    {"command": f"{Color.GREEN}sed{Color.RESET} -e 's/a/b/' -e 's/c/d/' filename", "description": "Aplica múltiples sustituciones", "description_en": "Apply multiple substitutions"},
    {"command": f"{Color.GREEN}sed{Color.RESET} -r 's/[0-9]+/num/g' filename", "description": "Usa regex extendida para reemplazar números", "description_en": "Use extended regex to replace numbers"},
    {"command": f"{Color.GREEN}sed{Color.RESET} -n '/pattern/p' filename", "description": "Imprime solo las líneas que coinciden con 'pattern'", "description_en": "Print only lines matching 'pattern'"},
    {"command": f"{Color.GREEN}sed{Color.RESET} '2,5s/old/new/' filename", "description": "Reemplaza 'old' por 'new' solo en las líneas 2-5", "description_en": "Replace 'old' with 'new' only on lines 2-5"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
