from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de NC (Netcat)"
TITLE_EN = "NC (Netcat) Options"
BRIEF = "Navaja suiza de TCP/IP"
BRIEF_EN = "TCP/IP Swiss army knife"

COMMANDS = [
    {"command": f"{Color.GREEN}nc{Color.RESET} -l -p <port>", "description": "Escucha en el puerto especificado (modo servidor)", "description_en": "Listen on the specified port (server mode)"},
    {"command": f"{Color.GREEN}nc{Color.RESET} <host> <port>", "description": "Conecta al host y puerto (modo cliente)", "description_en": "Connect to host and port (client mode)"},
    {"command": f"{Color.GREEN}nc{Color.RESET} -z <host> <port>", "description": "Escanea puertos sin enviar datos", "description_en": "Port scan without sending data"},
    {"command": f"{Color.GREEN}nc{Color.RESET} -z <host> 20-80", "description": "Escanea un rango de puertos", "description_en": "Scan a port range"},
    {"command": f"{Color.GREEN}nc{Color.RESET} -v", "description": "Modo verbose — salida detallada", "description_en": "Verbose mode — detailed output"},
    {"command": f"{Color.GREEN}nc{Color.RESET} -u", "description": "Usa UDP en lugar de TCP", "description_en": "Use UDP instead of TCP"},
    {"command": f"{Color.GREEN}nc{Color.RESET} -n", "description": "Omite la resolución DNS", "description_en": "Skip DNS resolution"},
    {"command": f"{Color.GREEN}nc{Color.RESET} -k", "description": "Mantiene la conexión abierta tras desconexión", "description_en": "Keep listening after client disconnects"},
    {"command": f"{Color.GREEN}nc{Color.RESET} -w <timeout>", "description": "Tiempo de espera en segundos", "description_en": "Connection timeout in seconds"},
    {"command": f"{Color.GREEN}nc{Color.RESET} -e <command>", "description": "Ejecuta un comando tras la conexión", "description_en": "Execute command after connection"},
    {"command": f"{Color.GREEN}nc{Color.RESET} -x <proxy>", "description": "Usa un proxy SOCKS para la conexión", "description_en": "Use a SOCKS proxy for the connection"},
    {"command": f"{Color.GREEN}nc{Color.RESET} -q <seconds>", "description": "Espera N segundos tras EOF antes de cerrar", "description_en": "Wait N seconds after EOF before closing"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
