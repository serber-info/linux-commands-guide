from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de TR"
TITLE_EN = "TR Options"
BRIEF = "Traduce o elimina caracteres"
BRIEF_EN = "Translate or delete characters"

COMMANDS = [
    {"command": f"{Color.GREEN}tr{Color.RESET} 'a-z' 'A-Z' < filename", "description": "Convierte minúsculas a mayúsculas", "description_en": "Convert lowercase to uppercase"},
    {"command": f"{Color.GREEN}tr{Color.RESET} 'A-Z' 'a-z' < filename", "description": "Convierte mayúsculas a minúsculas", "description_en": "Convert uppercase to lowercase"},
    {"command": f"{Color.GREEN}tr{Color.RESET} -d '[:digit:]' < filename", "description": "Elimina todos los dígitos", "description_en": "Delete all digits"},
    {"command": f"{Color.GREEN}tr{Color.RESET} ' ' '_' < filename", "description": "Reemplaza espacios con guiones bajos", "description_en": "Replace spaces with underscores"},
    {"command": f"{Color.GREEN}tr{Color.RESET} -s ' ' < filename", "description": "Comprime secuencias de espacios en uno", "description_en": "Squeeze consecutive spaces into one"},
    {"command": f"{Color.GREEN}tr{Color.RESET} -c '[:alnum:]' '_' < filename", "description": "Reemplaza todo lo que no sea alfanumérico con '_'", "description_en": "Replace non-alphanumeric characters with '_'"},
    {"command": f"{Color.GREEN}tr{Color.RESET} -d '\\n' < filename", "description": "Elimina los saltos de línea", "description_en": "Remove newline characters"},
    {"command": f"{Color.GREEN}tr{Color.RESET} -d '[:space:]' < filename", "description": "Elimina todos los espacios en blanco", "description_en": "Delete all whitespace characters"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
