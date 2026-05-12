from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de FIREWALL-CMD"
TITLE_EN = "FIREWALL-CMD Options"
BRIEF = "Gestión del firewall firewalld"
BRIEF_EN = "Manage the firewalld firewall"

COMMANDS = [
    {"command": f"{Color.GREEN}firewall-cmd{Color.RESET} --state", "description": "Muestra el estado del firewall", "description_en": "Show firewall state"},
    {"command": f"{Color.GREEN}firewall-cmd{Color.RESET} --get-default-zone", "description": "Muestra la zona por defecto", "description_en": "Show the default zone"},
    {"command": f"{Color.GREEN}firewall-cmd{Color.RESET} --list-all", "description": "Lista todas las reglas de la zona por defecto", "description_en": "List all rules in the default zone"},
    {"command": f"{Color.GREEN}firewall-cmd{Color.RESET} --list-all-zones", "description": "Lista todas las zonas y sus configuraciones", "description_en": "List all zones and their settings"},
    {"command": f"{Color.GREEN}firewall-cmd{Color.RESET} --zone=zone --add-port=80/tcp --permanent", "description": "Abre el puerto 80 TCP de forma permanente", "description_en": "Permanently open TCP port 80"},
    {"command": f"{Color.GREEN}firewall-cmd{Color.RESET} --zone=zone --remove-port=80/tcp --permanent", "description": "Cierra el puerto 80 TCP de forma permanente", "description_en": "Permanently close TCP port 80"},
    {"command": f"{Color.GREEN}firewall-cmd{Color.RESET} --zone=zone --add-service=http --permanent", "description": "Permite el servicio HTTP de forma permanente", "description_en": "Permanently allow the HTTP service"},
    {"command": f"{Color.GREEN}firewall-cmd{Color.RESET} --zone=zone --remove-service=http --permanent", "description": "Bloquea el servicio HTTP de forma permanente", "description_en": "Permanently block the HTTP service"},
    {"command": f"{Color.GREEN}firewall-cmd{Color.RESET} --reload", "description": "Recarga la configuración del firewall", "description_en": "Reload firewall configuration"},
    {"command": f"{Color.GREEN}firewall-cmd{Color.RESET} --runtime-to-permanent", "description": "Guarda los cambios en tiempo real como permanentes", "description_en": "Save runtime changes as permanent"},
    {"command": f"{Color.GREEN}firewall-cmd{Color.RESET} --zone=zone --add-interface=eth0", "description": "Asocia eth0 a una zona", "description_en": "Bind eth0 to a zone"},
    {"command": f"{Color.GREEN}firewall-cmd{Color.RESET} --get-zones", "description": "Lista todas las zonas disponibles", "description_en": "List all available zones"},
    {"command": f"{Color.GREEN}firewall-cmd{Color.RESET} --new-zone=custom --permanent", "description": "Crea una nueva zona personalizada", "description_en": "Create a new custom zone"},
    {"command": f"{Color.GREEN}firewall-cmd{Color.RESET} --delete-zone=custom --permanent", "description": "Elimina una zona personalizada", "description_en": "Delete a custom zone"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
