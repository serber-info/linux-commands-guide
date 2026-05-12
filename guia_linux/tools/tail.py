from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de TAIL"
TITLE_EN = "TAIL Options"
BRIEF = "Muestra el final de un archivo"
BRIEF_EN = "Display the end of a file"

COMMANDS = [
    {"command": f"{Color.GREEN}tail{Color.RESET} filename", "description": "Muestra las últimas 10 líneas del archivo", "description_en": "Show the last 10 lines of the file"},
    {"command": f"{Color.GREEN}tail{Color.RESET} -n N filename", "description": "Muestra las últimas N líneas", "description_en": "Show the last N lines"},
    {"command": f"{Color.GREEN}tail{Color.RESET} -c N filename", "description": "Muestra los últimos N bytes", "description_en": "Show the last N bytes"},
    {"command": f"{Color.GREEN}tail{Color.RESET} -f filename", "description": "Sigue el archivo en tiempo real", "description_en": "Follow the file in real time"},
    {"command": f"{Color.GREEN}tail{Color.RESET} -F filename", "description": "Sigue el archivo, reconectándose si cambia de nombre", "description_en": "Follow file, reconnecting if renamed"},
    {"command": f"{Color.GREEN}tail{Color.RESET} --follow=descriptor filename", "description": "Sigue por descriptor de archivo", "description_en": "Follow by file descriptor"},
    {"command": f"{Color.GREEN}tail{Color.RESET} --pid=PID filename", "description": "Sigue hasta que el proceso PID finalice", "description_en": "Follow until process PID exits"},
    {"command": f"{Color.GREEN}tail{Color.RESET} --retry -f filename", "description": "Sigue intentando acceder si el archivo no existe", "description_en": "Keep retrying if file is not accessible"},
    {"command": f"{Color.GREEN}tail{Color.RESET} -q file1 file2", "description": "Suprime los encabezados en la salida", "description_en": "Suppress file headers in output"},
    {"command": f"{Color.GREEN}tail{Color.RESET} -v filename", "description": "Muestra siempre el encabezado del archivo", "description_en": "Always show file header"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
