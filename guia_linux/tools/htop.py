from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de HTOP"
TITLE_EN = "HTOP Options"
BRIEF = "Monitor de procesos interactivo"
BRIEF_EN = "Interactive process monitor"

COMMANDS = [
    {"command": f"{Color.GREEN}htop{Color.RESET}", "description": "Inicia htop con configuración predeterminada", "description_en": "Start htop with default settings"},
    {"command": f"{Color.GREEN}htop{Color.RESET} -d N", "description": "Retardo de actualización en décimas de segundo", "description_en": "Update delay in tenths of a second"},
    {"command": f"{Color.GREEN}htop{Color.RESET} -C", "description": "Desactiva el uso de colores", "description_en": "Disable colors"},
    {"command": f"{Color.GREEN}htop{Color.RESET} -u user", "description": "Muestra solo procesos del usuario indicado", "description_en": "Show only processes of the given user"},
    {"command": f"{Color.GREEN}htop{Color.RESET} -p pid1,pid2", "description": "Muestra solo los procesos con los PIDs indicados", "description_en": "Show only the specified PIDs"},
    {"command": f"{Color.GREEN}htop{Color.RESET} -s column", "description": "Ordena por la columna especificada (cpu, mem...)", "description_en": "Sort by the specified column (cpu, mem...)"},
    {"command": f"{Color.GREEN}htop{Color.RESET} -t", "description": "Activa la vista de árbol de procesos", "description_en": "Enable tree view of processes"},
    {"command": f"{Color.GREEN}htop{Color.RESET} --no-color", "description": "Alias de -C; desactiva colores", "description_en": "Alias for -C; disable colors"},
    {"command": f"{Color.GREEN}htop{Color.RESET} --tree", "description": "Alias de -t; vista en árbol", "description_en": "Alias for -t; tree view"},
    {"command": f"{Color.GREEN}htop{Color.RESET} --version", "description": "Muestra la versión de htop instalada", "description_en": "Show installed htop version"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
