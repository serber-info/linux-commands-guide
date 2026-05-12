from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de IFCONFIG"
TITLE_EN = "IFCONFIG Options"
BRIEF = "Configuración de interfaces de red (legacy)"
BRIEF_EN = "Network interface configuration (legacy)"

COMMANDS = [
    {"command": f"{Color.GREEN}ifconfig{Color.RESET}", "description": "Muestra el estado de todas las interfaces activas", "description_en": "Show all active network interfaces"},
    {"command": f"{Color.GREEN}ifconfig{Color.RESET} <iface>", "description": "Muestra el estado de la interfaz especificada", "description_en": "Show the specified interface"},
    {"command": f"{Color.GREEN}ifconfig{Color.RESET} <iface> up", "description": "Activa la interfaz de red", "description_en": "Bring the interface up"},
    {"command": f"{Color.GREEN}ifconfig{Color.RESET} <iface> down", "description": "Desactiva la interfaz de red", "description_en": "Bring the interface down"},
    {"command": f"{Color.GREEN}ifconfig{Color.RESET} <iface> <ip> netmask <mask>", "description": "Asigna IP y máscara a la interfaz", "description_en": "Assign IP and netmask to the interface"},
    {"command": f"{Color.GREEN}ifconfig{Color.RESET} <iface> broadcast <addr>", "description": "Establece la dirección de broadcast", "description_en": "Set the broadcast address"},
    {"command": f"{Color.GREEN}ifconfig{Color.RESET} <iface> mtu <size>", "description": "Define el tamaño de MTU", "description_en": "Set the MTU size"},
    {"command": f"{Color.GREEN}ifconfig{Color.RESET} <iface> promisc", "description": "Activa el modo promiscuo", "description_en": "Enable promiscuous mode"},
    {"command": f"{Color.GREEN}ifconfig{Color.RESET} <iface> -promisc", "description": "Desactiva el modo promiscuo", "description_en": "Disable promiscuous mode"},
    {"command": f"{Color.GREEN}ifconfig{Color.RESET} <iface> hw ether <mac>", "description": "Cambia la dirección MAC", "description_en": "Change the MAC address"},
    {"command": f"{Color.GREEN}ifconfig{Color.RESET} <iface> add <ip>", "description": "Añade una dirección IP secundaria", "description_en": "Add a secondary IP address"},
    {"command": f"{Color.GREEN}ifconfig{Color.RESET} <iface> del <ip>", "description": "Elimina una dirección IP secundaria", "description_en": "Remove a secondary IP address"},
    {"command": f"{Color.GREEN}ifconfig{Color.RESET} -a", "description": "Muestra todas las interfaces, activas e inactivas", "description_en": "Show all interfaces, active and inactive"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
