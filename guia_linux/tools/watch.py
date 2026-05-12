from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de WATCH"
TITLE_EN = "WATCH Options"
BRIEF = "Ejecuta un comando periódicamente"
BRIEF_EN = "Execute a command periodically"

COMMANDS = [
    {"command": f"{Color.GREEN}watch{Color.RESET} command", "description": "Ejecuta el comando cada 2 segundos (por defecto)", "description_en": "Execute command every 2 seconds (default)"},
    {"command": f"{Color.GREEN}watch{Color.RESET} -n N command", "description": "Ejecuta el comando cada N segundos", "description_en": "Execute command every N seconds"},
    {"command": f"{Color.GREEN}watch{Color.RESET} -d command", "description": "Resalta los cambios entre actualizaciones", "description_en": "Highlight changes between updates"},
    {"command": f"{Color.GREEN}watch{Color.RESET} -t command", "description": "Oculta el encabezado de watch", "description_en": "Hide the watch header"},
    {"command": f"{Color.GREEN}watch{Color.RESET} -p command", "description": "Intenta ejecutar el comando con precisión periódica", "description_en": "Attempt precise period execution"},
    {"command": f"{Color.GREEN}watch{Color.RESET} -e command", "description": "Sale si el comando devuelve un error", "description_en": "Exit if command returns an error"},
    {"command": f"{Color.GREEN}watch{Color.RESET} -g command", "description": "Sale cuando la salida del comando cambia", "description_en": "Exit when the command output changes"},
    {"command": f"{Color.GREEN}watch{Color.RESET} -n 1 df -h", "description": "Ejemplo: monitoriza el disco cada segundo", "description_en": "Example: monitor disk usage every second"},
    {"command": f"{Color.GREEN}watch{Color.RESET} -n 2 'ps aux | grep nginx'", "description": "Ejemplo: monitoriza el proceso nginx", "description_en": "Example: monitor the nginx process"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
