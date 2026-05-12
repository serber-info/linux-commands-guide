from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de SS"
TITLE_EN = "SS Options"
BRIEF = "Estadísticas de sockets (reemplaza netstat)"
BRIEF_EN = "Socket statistics (replaces netstat)"

COMMANDS = [
    {"command": f"{Color.GREEN}ss{Color.RESET}", "description": "Muestra todos los sockets abiertos", "description_en": "Show all open sockets"},
    {"command": f"{Color.GREEN}ss{Color.RESET} -a", "description": "Muestra todos los sockets (en escucha y conectados)", "description_en": "Show all sockets (listening and connected)"},
    {"command": f"{Color.GREEN}ss{Color.RESET} -t", "description": "Muestra solo conexiones TCP", "description_en": "Show only TCP connections"},
    {"command": f"{Color.GREEN}ss{Color.RESET} -u", "description": "Muestra solo conexiones UDP", "description_en": "Show only UDP connections"},
    {"command": f"{Color.GREEN}ss{Color.RESET} -l", "description": "Muestra solo puertos en escucha", "description_en": "Show only listening ports"},
    {"command": f"{Color.GREEN}ss{Color.RESET} -p", "description": "Muestra el proceso asociado a cada socket", "description_en": "Show the process associated with each socket"},
    {"command": f"{Color.GREEN}ss{Color.RESET} -n", "description": "Muestra IPs y puertos en formato numérico", "description_en": "Show IPs and ports in numeric format"},
    {"command": f"{Color.GREEN}ss{Color.RESET} -tulnp", "description": "Combinación común: TCP/UDP puertos en escucha con PID", "description_en": "Common combo: TCP/UDP listening ports with PID"},
    {"command": f"{Color.GREEN}ss{Color.RESET} -s", "description": "Muestra un resumen de estadísticas", "description_en": "Show a statistics summary"},
    {"command": f"{Color.GREEN}ss{Color.RESET} -4", "description": "Muestra solo sockets IPv4", "description_en": "Show only IPv4 sockets"},
    {"command": f"{Color.GREEN}ss{Color.RESET} -6", "description": "Muestra solo sockets IPv6", "description_en": "Show only IPv6 sockets"},
    {"command": f"{Color.GREEN}ss{Color.RESET} -x", "description": "Muestra sockets de dominio Unix", "description_en": "Show Unix domain sockets"},
    {"command": f"{Color.GREEN}ss{Color.RESET} -o", "description": "Muestra información de tiempo de los sockets", "description_en": "Show socket timer information"},
    {"command": f"{Color.GREEN}ss{Color.RESET} sport = :80", "description": "Filtra sockets por puerto de origen", "description_en": "Filter sockets by source port"},
    {"command": f"{Color.GREEN}ss{Color.RESET} dport = :443", "description": "Filtra sockets por puerto de destino", "description_en": "Filter sockets by destination port"},
    {"command": f"{Color.GREEN}ss{Color.RESET} -t state established", "description": "Muestra solo conexiones TCP establecidas", "description_en": "Show only established TCP connections"},
    {"command": f"{Color.GREEN}ss{Color.RESET} -t state time-wait", "description": "Muestra conexiones en estado TIME-WAIT", "description_en": "Show connections in TIME-WAIT state"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
