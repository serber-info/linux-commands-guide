from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de NETSTAT"
TITLE_EN = "NETSTAT Options"
BRIEF = "Estadísticas de conexiones de red"
BRIEF_EN = "Network connection statistics"

COMMANDS = [
    {"command": f"{Color.GREEN}netstat{Color.RESET}", "description": "Muestra todas las conexiones de red activas", "description_en": "Show all active network connections"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} -a", "description": "Muestra todas las conexiones y puertos en escucha", "description_en": "Show all connections and listening ports"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} -t", "description": "Muestra solo conexiones TCP", "description_en": "Show only TCP connections"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} -u", "description": "Muestra solo conexiones UDP", "description_en": "Show only UDP connections"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} -l", "description": "Muestra solo puertos en escucha", "description_en": "Show only listening ports"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} -p", "description": "Muestra el proceso (PID) de cada conexión", "description_en": "Show the process (PID) for each connection"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} -n", "description": "Muestra IPs y puertos en formato numérico", "description_en": "Show IPs and ports in numeric format"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} -r", "description": "Muestra la tabla de enrutamiento", "description_en": "Show the routing table"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} -i", "description": "Muestra estadísticas de interfaz de red", "description_en": "Show network interface statistics"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} -c", "description": "Actualiza la información en intervalos continuos", "description_en": "Continuously update output"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} -s", "description": "Muestra estadísticas por protocolo", "description_en": "Show per-protocol statistics"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} -g", "description": "Muestra la tabla de membresía multicast", "description_en": "Show multicast group membership"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} -tulnp", "description": "Combinación común: TCP/UDP puertos en escucha con PID", "description_en": "Common combo: TCP/UDP listening ports with PID"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
