# Configuración de colores
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

ifconfig_commands = [
    {"command": f"{GREEN}ifconfig{RESET}", "description": "Muestra el estado de todas las interfaces de red activas"},
    {"command": f"{GREEN}ifconfig{RESET} <iface>", "description": "Muestra el estado de la interfaz especificada"},
    {"command": f"{GREEN}ifconfig{RESET} <iface> up", "description": "Activa la interfaz de red especificada"},
    {"command": f"{GREEN}ifconfig{RESET} <iface> down", "description": "Desactiva la interfaz de red especificada"},
    {"command": f"{GREEN}ifconfig{RESET} <iface> <ip> netmask <mask>", "description": "Asigna una dirección IP y máscara de red a la interfaz"},
    {"command": f"{GREEN}ifconfig{RESET} <iface> broadcast <address>", "description": "Establece la dirección de broadcast para la interfaz"},
    {"command": f"{GREEN}ifconfig{RESET} <iface> mtu <size>", "description": "Define el tamaño de MTU para la interfaz"},
    {"command": f"{GREEN}ifconfig{RESET} <iface> promisc", "description": "Activa el modo promiscuo en la interfaz"},
    {"command": f"{GREEN}ifconfig{RESET} <iface> -promisc", "description": "Desactiva el modo promiscuo en la interfaz"},
    {"command": f"{GREEN}ifconfig{RESET} <iface> hw ether <mac>", "description": "Cambia la dirección MAC de la interfaz"},
    {"command": f"{GREEN}ifconfig{RESET} <iface> add <ip>", "description": "Añade una dirección IP secundaria a la interfaz"},
    {"command": f"{GREEN}ifconfig{RESET} <iface> del <ip>", "description": "Elimina una dirección IP secundaria de la interfaz"},
    {"command": f"{GREEN}ifconfig{RESET} <iface> txqueuelen <len>", "description": "Define la longitud de la cola de transmisión para la interfaz"},
    {"command": f"{GREEN}ifconfig{RESET} <iface> pointopoint <dest_addr>", "description": "Configura la dirección punto a punto de la interfaz"},
    {"command": f"{GREEN}ifconfig{RESET} <iface> arp", "description": "Activa el protocolo ARP en la interfaz"},
    {"command": f"{GREEN}ifconfig{RESET} <iface> -arp", "description": "Desactiva el protocolo ARP en la interfaz"},
    {"command": f"{GREEN}ifconfig{RESET} <iface> metric <value>", "description": "Establece el valor de métrica para la interfaz"},
    {"command": f"{GREEN}ifconfig{RESET} -a", "description": "Muestra todas las interfaces de red, activas e inactivas"},
]

print(f"\nComandos de IFCONFIG con ejemplos y descripciones:\n")
print(f"{'Comando':<41} | {'Descripción'}")
print("-" * 105)
for cmd in ifconfig_commands:
    command = cmd["command"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<50} | {description}")
