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
    {"command": f"{Color.GREEN}bat{Color.RESET} -r N:M filename", "description": "Muestra solo las líneas N a M (bat/batcat)", "description_en": "Show only lines N to M (bat/batcat)"},
    {"command": f"{Color.GREEN}bat{Color.RESET} --theme=<theme> filename", "description": "Resalta la sintaxis con el tema indicado (bat)", "description_en": "Highlight syntax with the given theme (bat)"},
    {"command": f"{Color.GREEN}bat{Color.RESET} --paging=never filename", "description": "Muestra el archivo sin paginador (bat)", "description_en": "Print the file without a pager (bat)"},
    {"command": f"{Color.GREEN}cat{Color.RESET} -u filename", "description": "Ignorada por GNU cat (se mantiene por compatibilidad POSIX)", "description_en": "Ignored by GNU cat (kept for POSIX compatibility)"},
    {"command": f"{Color.GREEN}bat{Color.RESET} --list-languages", "description": "Lista los lenguajes con resaltado de sintaxis (bat)", "description_en": "List languages with syntax highlighting (bat)"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
