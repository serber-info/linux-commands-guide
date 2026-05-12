from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de CAT"
TITLE_EN = "CAT Options"
BRIEF = "Muestra y concatena contenido de archivos"
BRIEF_EN = "Display and concatenate file contents"

COMMANDS = [
    {"command": f"{Color.GREEN}cat{Color.RESET} filename", "description": "Muestra el contenido del archivo", "description_en": "Display file contents"},
    {"command": f"{Color.GREEN}cat{Color.RESET} file1 file2 > output", "description": "Concatena file1 y file2 en output", "description_en": "Concatenate file1 and file2 into output"},
    {"command": f"{Color.GREEN}cat{Color.RESET} -n filename", "description": "Muestra el contenido con números de línea", "description_en": "Show content with line numbers"},
    {"command": f"{Color.GREEN}cat{Color.RESET} -b filename", "description": "Numera solo las líneas no vacías", "description_en": "Number only non-empty lines"},
    {"command": f"{Color.GREEN}cat{Color.RESET} -s filename", "description": "Suprime líneas vacías consecutivas", "description_en": "Squeeze consecutive blank lines"},
    {"command": f"{Color.GREEN}cat{Color.RESET} -T filename", "description": "Muestra tabulaciones como ^I", "description_en": "Show tabs as ^I"},
    {"command": f"{Color.GREEN}cat{Color.RESET} -E filename", "description": "Muestra $ al final de cada línea", "description_en": "Show $ at end of each line"},
    {"command": f"{Color.GREEN}cat{Color.RESET} -v filename", "description": "Muestra caracteres no imprimibles", "description_en": "Show non-printable characters"},
    {"command": f"{Color.GREEN}cat{Color.RESET} -A filename", "description": "Muestra todos los caracteres especiales", "description_en": "Show all special characters"},
    {"command": f"{Color.GREEN}cat{Color.RESET} -r, --line-range N:M filename", "description": "Muestra solo las líneas N a M (batcat)", "description_en": "Show only lines N to M (batcat)"},
    {"command": f"{Color.GREEN}cat{Color.RESET} --theme <theme>", "description": "Establece el tema de resaltado de sintaxis (batcat)", "description_en": "Set syntax-highlighting theme (batcat)"},
    {"command": f"{Color.GREEN}cat{Color.RESET} --paging never filename", "description": "Desactiva el paginador en batcat", "description_en": "Disable pager in batcat"},
    {"command": f"{Color.GREEN}cat{Color.RESET} -u, --unbuffered", "description": "Desactiva el buffering (compatibilidad POSIX)", "description_en": "Disable buffering (POSIX compatibility)"},
    {"command": f"{Color.GREEN}cat{Color.RESET} -L, --list-languages", "description": "Lista los lenguajes soportados para resaltado", "description_en": "List supported syntax-highlighting languages"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
