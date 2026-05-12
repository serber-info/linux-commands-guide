from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de IP"
TITLE_EN = "IP Command Options"
BRIEF = "Gestión moderna de interfaces y rutas de red"
BRIEF_EN = "Modern network interface and routing management"

COMMANDS = [
    {"command": f"{Color.GREEN}ip{Color.RESET} link show", "description": "Muestra el estado de todos los enlaces de red", "description_en": "Show all network links"},
    {"command": f"{Color.GREEN}ip{Color.RESET} link set <iface> up", "description": "Activa la interfaz", "description_en": "Bring interface up"},
    {"command": f"{Color.GREEN}ip{Color.RESET} link set <iface> down", "description": "Desactiva la interfaz", "description_en": "Bring interface down"},
    {"command": f"{Color.GREEN}ip{Color.RESET} addr show", "description": "Muestra las IPs configuradas en todas las interfaces", "description_en": "Show IP addresses on all interfaces"},
    {"command": f"{Color.GREEN}ip{Color.RESET} addr add <ip/mask> dev <iface>", "description": "Asigna una IP a la interfaz", "description_en": "Assign an IP address to interface"},
    {"command": f"{Color.GREEN}ip{Color.RESET} addr del <ip/mask> dev <iface>", "description": "Elimina una IP de la interfaz", "description_en": "Remove an IP address from interface"},
    {"command": f"{Color.GREEN}ip{Color.RESET} addr flush dev <iface>", "description": "Elimina todas las IPs de la interfaz", "description_en": "Flush all IP addresses from interface"},
    {"command": f"{Color.GREEN}ip{Color.RESET} route show", "description": "Muestra la tabla de enrutamiento", "description_en": "Show the routing table"},
    {"command": f"{Color.GREEN}ip{Color.RESET} route add <dest> via <gw> dev <iface>", "description": "Añade una ruta a la tabla de enrutamiento", "description_en": "Add a route to the routing table"},
    {"command": f"{Color.GREEN}ip{Color.RESET} route del <dest>", "description": "Elimina una ruta", "description_en": "Remove a route"},
    {"command": f"{Color.GREEN}ip{Color.RESET} route flush cache", "description": "Limpia la caché de rutas", "description_en": "Flush the routing cache"},
    {"command": f"{Color.GREEN}ip{Color.RESET} neigh show", "description": "Muestra la tabla ARP/NDP", "description_en": "Show the ARP/NDP neighbor table"},
    {"command": f"{Color.GREEN}ip{Color.RESET} neigh add <ip> lladdr <mac> dev <iface>", "description": "Añade una entrada ARP estática", "description_en": "Add a static ARP entry"},
    {"command": f"{Color.GREEN}ip{Color.RESET} link set <iface> mtu <size>", "description": "Establece el MTU de la interfaz", "description_en": "Set interface MTU"},
    {"command": f"{Color.GREEN}ip{Color.RESET} link set <iface> promisc on", "description": "Activa el modo promiscuo", "description_en": "Enable promiscuous mode"},
    {"command": f"{Color.GREEN}ip{Color.RESET} link set dev <iface> address <mac>", "description": "Cambia la dirección MAC", "description_en": "Change the MAC address"},
    {"command": f"{Color.GREEN}ip{Color.RESET} tunnel add <name> mode <mode>", "description": "Crea un túnel de red", "description_en": "Create a network tunnel"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
