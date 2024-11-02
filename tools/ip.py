from shellcolorize import Color

ip_commands = [
    {"command": f"{Color.GREEN}ip{Color.RESET} link show", "description": "Muestra el estado de todos los enlaces de red"},
    {"command": f"{Color.GREEN}ip{Color.RESET} link set <iface> up", "description": "Activa la interfaz de red especificada"},
    {"command": f"{Color.GREEN}ip{Color.RESET} link set <iface> down", "description": "Desactiva la interfaz de red especificada"},
    {"command": f"{Color.GREEN}ip{Color.RESET} addr show", "description": "Muestra las direcciones IP configuradas en todas las interfaces"},
    {"command": f"{Color.GREEN}ip{Color.RESET} addr add <ip/mask> dev <iface>", "description": "Asigna una dirección IP a la interfaz especificada"},
    {"command": f"{Color.GREEN}ip{Color.RESET} addr del <ip/mask> dev <iface>", "description": "Elimina una dirección IP de la interfaz especificada"},
    {"command": f"{Color.GREEN}ip{Color.RESET} route show", "description": "Muestra la tabla de enrutamiento"},
    {"command": f"{Color.GREEN}ip{Color.RESET} route add <dest> via <gateway> dev <iface>", "description": "Añade una ruta específica a la tabla de enrutamiento"},
    {"command": f"{Color.GREEN}ip{Color.RESET} route del <dest>", "description": "Elimina una ruta de la tabla de enrutamiento"},
    {"command": f"{Color.GREEN}ip{Color.RESET} neigh show", "description": "Muestra la tabla de vecinos ARP/NDP"},
    {"command": f"{Color.GREEN}ip{Color.RESET} neigh add <ip> lladdr <mac> dev <iface>", "description": "Añade una entrada ARP/NDP estática"},
    {"command": f"{Color.GREEN}ip{Color.RESET} neigh del <ip> dev <iface>", "description": "Elimina una entrada ARP/NDP"},
    {"command": f"{Color.GREEN}ip{Color.RESET} link set <iface> mtu <size>", "description": "Establece el tamaño de MTU para la interfaz"},
    {"command": f"{Color.GREEN}ip{Color.RESET} link set <iface> promisc on", "description": "Activa el modo promiscuo en la interfaz"},
    {"command": f"{Color.GREEN}ip{Color.RESET} link set <iface> promisc off", "description": "Desactiva el modo promiscuo en la interfaz"},
    {"command": f"{Color.GREEN}ip{Color.RESET} link set <iface> txqueuelen <len>", "description": "Establece la longitud de la cola de transmisión"},
    {"command": f"{Color.GREEN}ip{Color.RESET} rule add from <src> table <table>", "description": "Añade una regla de enrutamiento basado en políticas"},
    {"command": f"{Color.GREEN}ip{Color.RESET} rule del from <src> table <table>", "description": "Elimina una regla de enrutamiento basado en políticas"},
    {"command": f"{Color.GREEN}ip{Color.RESET} link set dev <iface> alias <name>", "description": "Asigna un alias descriptivo a la interfaz"},
    {"command": f"{Color.GREEN}ip{Color.RESET} link set dev <iface> address <mac>", "description": "Cambia la dirección MAC de la interfaz"},
    {"command": f"{Color.GREEN}ip{Color.RESET} link set dev <iface> arp on", "description": "Activa el protocolo ARP en la interfaz"},
    {"command": f"{Color.GREEN}ip{Color.RESET} link set dev <iface> arp off", "description": "Desactiva el protocolo ARP en la interfaz"},
    {"command": f"{Color.GREEN}ip{Color.RESET} tunnel add <tunnel> mode <mode>", "description": "Crea un túnel de red en el modo especificado (sit, ipip, gre)"},
    {"command": f"{Color.GREEN}ip{Color.RESET} tunnel del <tunnel>", "description": "Elimina el túnel de red especificado"},
    {"command": f"{Color.GREEN}ip{Color.RESET} maddr add <multicast_addr> dev <iface>", "description": "Añade una dirección multicast a la interfaz"},
    {"command": f"{Color.GREEN}ip{Color.RESET} maddr del <multicast_addr> dev <iface>", "description": "Elimina una dirección multicast de la interfaz"},
    {"command": f"{Color.GREEN}ip{Color.RESET} addr flush dev <iface>", "description": "Elimina todas las direcciones IP de la interfaz"},
    {"command": f"{Color.GREEN}ip{Color.RESET} route flush cache", "description": "Elimina todas las entradas de caché de rutas"},
]

print(f"\nComandos de IP con ejemplos y descripciones:\n")
print(f"{'Comando':<51} | {'Descripción'}")
print("-" * 117)
for cmd in ip_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<60} | {description}")

