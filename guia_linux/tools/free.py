from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de FREE"
TITLE_EN = "FREE Options"
BRIEF = "Muestra el uso de memoria del sistema"
BRIEF_EN = "Display system memory usage"

COMMANDS = [
    {"command": f"{Color.GREEN}free{Color.RESET}", "description": "Muestra el uso de memoria y swap", "description_en": "Show memory and swap usage"},
    {"command": f"{Color.GREEN}free{Color.RESET} -b", "description": "Muestra el uso de memoria en bytes", "description_en": "Show memory in bytes"},
    {"command": f"{Color.GREEN}free{Color.RESET} -k", "description": "Muestra el uso de memoria en kilobytes", "description_en": "Show memory in kilobytes"},
    {"command": f"{Color.GREEN}free{Color.RESET} -m", "description": "Muestra el uso de memoria en megabytes", "description_en": "Show memory in megabytes"},
    {"command": f"{Color.GREEN}free{Color.RESET} -g", "description": "Muestra el uso de memoria en gigabytes", "description_en": "Show memory in gigabytes"},
    {"command": f"{Color.GREEN}free{Color.RESET} -h", "description": "Formato legible por humanos", "description_en": "Human-readable format"},
    {"command": f"{Color.GREEN}free{Color.RESET} --si", "description": "Usa potencias de 1000 en lugar de 1024", "description_en": "Use powers of 1000 instead of 1024"},
    {"command": f"{Color.GREEN}free{Color.RESET} -t", "description": "Muestra una línea con el total (memoria + swap)", "description_en": "Show a total line (memory + swap)"},
    {"command": f"{Color.GREEN}free{Color.RESET} -s N", "description": "Actualiza la salida cada N segundos", "description_en": "Refresh output every N seconds"},
    {"command": f"{Color.GREEN}free{Color.RESET} -c N", "description": "Especifica el número de actualizaciones antes de salir", "description_en": "Number of updates before exiting (use with -s)"},
    {"command": f"{Color.GREEN}free{Color.RESET} -w", "description": "Muestra columnas de buffers y caché por separado", "description_en": "Show buffers and cache in separate columns"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
