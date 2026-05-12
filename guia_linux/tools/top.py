from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de TOP"
TITLE_EN = "TOP Options"
BRIEF = "Monitor de procesos en tiempo real"
BRIEF_EN = "Real-time process monitor"

COMMANDS = [
    {"command": f"{Color.GREEN}top{Color.RESET}", "description": "Inicia top con configuración predeterminada", "description_en": "Start top with default settings"},
    {"command": f"{Color.GREEN}top{Color.RESET} -b", "description": "Modo batch (no interactivo), útil para scripts", "description_en": "Batch mode (non-interactive), useful for scripts"},
    {"command": f"{Color.GREEN}top{Color.RESET} -d N", "description": "Actualiza cada N segundos", "description_en": "Update every N seconds"},
    {"command": f"{Color.GREEN}top{Color.RESET} -n N", "description": "Sale tras N iteraciones", "description_en": "Exit after N iterations"},
    {"command": f"{Color.GREEN}top{Color.RESET} -p pid1,pid2", "description": "Muestra solo los PIDs especificados", "description_en": "Monitor only the specified PIDs"},
    {"command": f"{Color.GREEN}top{Color.RESET} -u user", "description": "Muestra solo procesos del usuario indicado", "description_en": "Show only processes of the given user"},
    {"command": f"{Color.GREEN}top{Color.RESET} -i", "description": "Omite los procesos inactivos", "description_en": "Omit idle processes"},
    {"command": f"{Color.GREEN}top{Color.RESET} -c", "description": "Muestra la línea completa de comando", "description_en": "Show full command line"},
    {"command": f"{Color.GREEN}top{Color.RESET} -o %CPU", "description": "Ordena por la columna especificada", "description_en": "Sort by the specified column"},
    {"command": f"{Color.GREEN}top{Color.RESET} -H", "description": "Muestra cada hilo por separado", "description_en": "Show individual threads"},
    {"command": f"{Color.GREEN}top{Color.RESET} -1", "description": "Muestra cada CPU por separado", "description_en": "Show each CPU individually"},
    {"section": "Teclas interactivas", "section_en": "Interactive Keys"},
    {"command": f"{Color.GREEN}q{Color.RESET}", "description": "Salir de top", "description_en": "Quit top"},
    {"command": f"{Color.GREEN}M{Color.RESET}", "description": "Ordenar por uso de memoria", "description_en": "Sort by memory usage"},
    {"command": f"{Color.GREEN}P{Color.RESET}", "description": "Ordenar por uso de CPU", "description_en": "Sort by CPU usage"},
    {"command": f"{Color.GREEN}k{Color.RESET}", "description": "Envía una señal a un proceso", "description_en": "Send a signal to a process"},
    {"command": f"{Color.GREEN}r{Color.RESET}", "description": "Cambia la prioridad (renice) de un proceso", "description_en": "Change process priority (renice)"},
    {"command": f"{Color.GREEN}V{Color.RESET}", "description": "Activa/desactiva la vista en árbol", "description_en": "Toggle tree view"},
    {"command": f"{Color.GREEN}W{Color.RESET}", "description": "Guarda la configuración actual", "description_en": "Save current settings"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
