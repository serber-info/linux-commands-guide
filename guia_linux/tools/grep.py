from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de GREP"
TITLE_EN = "GREP Options"
BRIEF = "Busca patrones en archivos"
BRIEF_EN = "Search for patterns in files"

COMMANDS = [
    {"command": f"{Color.GREEN}grep{Color.RESET} 'word' filename", "description": "Busca líneas que contengan 'word' en el archivo", "description_en": "Search lines containing 'word' in the file"},
    {"command": f"{Color.GREEN}grep{Color.RESET} -i 'word' filename", "description": "Busca ignorando mayúsculas/minúsculas", "description_en": "Case-insensitive search"},
    {"command": f"{Color.GREEN}grep{Color.RESET} -v 'word' filename", "description": "Muestra líneas que NO contienen 'word'", "description_en": "Show lines that do NOT contain 'word'"},
    {"command": f"{Color.GREEN}grep{Color.RESET} -w 'word' filename", "description": "Busca 'word' como palabra completa", "description_en": "Match 'word' as a whole word"},
    {"command": f"{Color.GREEN}grep{Color.RESET} -x 'word' filename", "description": "Muestra líneas que coinciden exactamente con 'word'", "description_en": "Match lines that exactly equal 'word'"},
    {"command": f"{Color.GREEN}grep{Color.RESET} -c 'word' filename", "description": "Cuenta las líneas que contienen 'word'", "description_en": "Count lines containing 'word'"},
    {"command": f"{Color.GREEN}grep{Color.RESET} -l 'word' *", "description": "Lista archivos que contienen 'word'", "description_en": "List files containing 'word'"},
    {"command": f"{Color.GREEN}grep{Color.RESET} -L 'word' *", "description": "Lista archivos que NO contienen 'word'", "description_en": "List files NOT containing 'word'"},
    {"command": f"{Color.GREEN}grep{Color.RESET} -n 'word' filename", "description": "Muestra número de línea junto a cada coincidencia", "description_en": "Show line numbers alongside matches"},
    {"command": f"{Color.GREEN}grep{Color.RESET} -A N 'word' filename", "description": "Muestra N líneas después de la coincidencia", "description_en": "Print N lines after each match"},
    {"command": f"{Color.GREEN}grep{Color.RESET} -B N 'word' filename", "description": "Muestra N líneas antes de la coincidencia", "description_en": "Print N lines before each match"},
    {"command": f"{Color.GREEN}grep{Color.RESET} -C N 'word' filename", "description": "Muestra N líneas alrededor de la coincidencia", "description_en": "Print N lines around each match"},
    {"command": f"{Color.GREEN}grep{Color.RESET} --color 'word' filename", "description": "Resalta 'word' en color en la salida", "description_en": "Highlight 'word' in color"},
    {"command": f"{Color.GREEN}grep{Color.RESET} -E 'w1|w2' filename", "description": "Expresiones regulares extendidas (OR lógico)", "description_en": "Extended regex — logical OR"},
    {"command": f"{Color.GREEN}grep{Color.RESET} -f patterns.txt filename", "description": "Lee los patrones de búsqueda desde un archivo", "description_en": "Read search patterns from a file"},
    {"command": f"{Color.GREEN}grep{Color.RESET} -o 'word' filename", "description": "Muestra solo la parte coincidente, no la línea entera", "description_en": "Print only the matching part, not the full line"},
    {"command": f"{Color.GREEN}grep{Color.RESET} -q 'word' filename", "description": "Modo silencioso — devuelve código de salida sin imprimir", "description_en": "Quiet mode — return exit code without printing"},
    {"command": f"{Color.GREEN}grep{Color.RESET} -R 'word' directory", "description": "Busca recursivamente en todos los archivos del directorio", "description_en": "Recursively search all files in directory"},
    {"command": f"{Color.GREEN}grep{Color.RESET} -m N 'word' filename", "description": "Muestra solo las primeras N coincidencias", "description_en": "Stop after N matches"},
    {"command": f"{Color.GREEN}grep{Color.RESET} --exclude='*.log' 'word' dir", "description": "Excluye archivos que coincidan con el patrón", "description_en": "Exclude files matching pattern"},
    {"command": f"{Color.GREEN}grep{Color.RESET} --include='*.txt' 'word' dir", "description": "Incluye solo archivos que coincidan con el patrón", "description_en": "Include only files matching pattern"},
    {"command": f"{Color.GREEN}grep{Color.RESET} -P 'word' filename", "description": "Usa expresiones regulares Perl (PCRE)", "description_en": "Use Perl-compatible regular expressions (PCRE)"},
    {"command": f"{Color.GREEN}grep{Color.RESET} '^word' filename", "description": "Busca líneas que comiencen con 'word'", "description_en": "Match lines starting with 'word'"},
    {"command": f"{Color.GREEN}grep{Color.RESET} 'word$' filename", "description": "Busca líneas que terminen con 'word'", "description_en": "Match lines ending with 'word'"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
