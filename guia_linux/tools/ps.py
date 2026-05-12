from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de PS"
TITLE_EN = "PS Options"
BRIEF = "Información sobre procesos en ejecución"
BRIEF_EN = "Information about running processes"

COMMANDS = [
    {"command": f"{Color.GREEN}ps{Color.RESET}", "description": "Muestra procesos de la terminal actual", "description_en": "Show processes for the current terminal"},
    {"command": f"{Color.GREEN}ps{Color.RESET} aux", "description": "Muestra todos los procesos (estilo BSD)", "description_en": "Show all processes (BSD style)"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -A", "description": "Muestra todos los procesos del sistema", "description_en": "Show all system processes"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -e", "description": "Similar a -A; todos los procesos", "description_en": "Same as -A; all processes"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -f", "description": "Formato detallado con relaciones padre-hijo (PPID)", "description_en": "Full format showing parent-child relationships"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -u <user>", "description": "Procesos de un usuario específico", "description_en": "Processes of a specific user"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -p <pid>", "description": "Información de un proceso por PID", "description_en": "Information for a specific PID"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -C <command>", "description": "Procesos ejecutados por el comando dado", "description_en": "Processes running the given command"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -o pid,user,%cpu,%mem", "description": "Columnas personalizadas en la salida", "description_en": "Custom output columns"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -H", "description": "Muestra procesos en formato jerárquico", "description_en": "Show processes in hierarchical format"},
    {"command": f"{Color.GREEN}ps{Color.RESET} --sort=%cpu", "description": "Ordena por uso de CPU", "description_en": "Sort by CPU usage"},
    {"command": f"{Color.GREEN}ps{Color.RESET} --sort=-%mem", "description": "Ordena por memoria (descendente)", "description_en": "Sort by memory usage (descending)"},
    {"command": f"{Color.GREEN}ps{Color.RESET} --forest", "description": "Vista en árbol de procesos", "description_en": "Tree view of processes"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -L", "description": "Muestra los hilos de los procesos", "description_en": "Show process threads"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -eo pid,user,pcpu,pmem,comm", "description": "Salida personalizada de todos los procesos", "description_en": "Custom output for all processes"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
