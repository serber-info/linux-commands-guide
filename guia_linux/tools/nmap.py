from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de NMAP"
TITLE_EN = "NMAP Options"
BRIEF = "Escáner de redes y puertos"
BRIEF_EN = "Network and port scanner"

COMMANDS = [
    {"command": f"{Color.GREEN}nmap{Color.RESET} host", "description": "Escaneo básico de puertos en un host", "description_en": "Basic port scan on a host"},
    {"command": f"{Color.GREEN}nmap{Color.RESET} -sS host", "description": "Escaneo SYN (sigiloso, requiere root)", "description_en": "SYN scan (stealthy, requires root)"},
    {"command": f"{Color.GREEN}nmap{Color.RESET} -sT host", "description": "Escaneo TCP completo (sin root)", "description_en": "Full TCP connect scan (no root needed)"},
    {"command": f"{Color.GREEN}nmap{Color.RESET} -sU host", "description": "Escaneo de puertos UDP", "description_en": "UDP port scan"},
    {"command": f"{Color.GREEN}nmap{Color.RESET} -sV host", "description": "Detecta versiones de servicios", "description_en": "Detect service versions"},
    {"command": f"{Color.GREEN}nmap{Color.RESET} -O host", "description": "Detecta el sistema operativo", "description_en": "Detect the operating system"},
    {"command": f"{Color.GREEN}nmap{Color.RESET} -A host", "description": "Escaneo completo (OS, versión, scripts, traceroute)", "description_en": "Full scan (OS, version, scripts, traceroute)"},
    {"command": f"{Color.GREEN}nmap{Color.RESET} -p 80,443 host", "description": "Escanea puertos específicos", "description_en": "Scan specific ports"},
    {"command": f"{Color.GREEN}nmap{Color.RESET} -p- host", "description": "Escanea todos los puertos (1-65535)", "description_en": "Scan all 65535 ports"},
    {"command": f"{Color.GREEN}nmap{Color.RESET} -T4 host", "description": "Nivel de agresividad T4 (rápido)", "description_en": "Timing template T4 (fast)"},
    {"command": f"{Color.GREEN}nmap{Color.RESET} --open host", "description": "Muestra solo puertos abiertos", "description_en": "Show only open ports"},
    {"command": f"{Color.GREEN}nmap{Color.RESET} -Pn host", "description": "Escanea sin hacer ping previo", "description_en": "Skip ping, scan directly"},
    {"command": f"{Color.GREEN}nmap{Color.RESET} -sC host", "description": "Ejecuta scripts de detección básicos", "description_en": "Run default detection scripts"},
    {"command": f"{Color.GREEN}nmap{Color.RESET} --script=http-title host", "description": "Ejecuta un script específico de NSE", "description_en": "Run a specific NSE script"},
    {"command": f"{Color.GREEN}nmap{Color.RESET} -iL targets.txt", "description": "Escanea una lista de hosts desde archivo", "description_en": "Scan a list of hosts from a file"},
    {"command": f"{Color.GREEN}nmap{Color.RESET} -oN scan.txt host", "description": "Guarda la salida en formato normal", "description_en": "Save output in normal format"},
    {"command": f"{Color.GREEN}nmap{Color.RESET} -oX scan.xml host", "description": "Guarda la salida en formato XML", "description_en": "Save output in XML format"},
    {"command": f"{Color.GREEN}nmap{Color.RESET} --traceroute host", "description": "Realiza un traceroute al host", "description_en": "Run a traceroute to the host"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
