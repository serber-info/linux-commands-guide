from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de LXC"
TITLE_EN = "LXC Options"
BRIEF = "Gestión de contenedores LXC"
BRIEF_EN = "LXC container management"

COMMANDS = [
    {"command": f"{Color.GREEN}lxc-ls{Color.RESET}", "description": "Lista todos los contenedores existentes", "description_en": "List all existing containers"},
    {"command": f"{Color.GREEN}lxc-stop{Color.RESET} -n container_name", "description": "Detiene un contenedor en ejecución", "description_en": "Stop a running container"},
    {"command": f"{Color.GREEN}lxc-start{Color.RESET} -n container_name", "description": "Inicia un contenedor detenido", "description_en": "Start a stopped container"},
    {"command": f"{Color.GREEN}lxc-restart{Color.RESET} -n container_name", "description": "Reinicia un contenedor", "description_en": "Restart a container"},
    {"command": f"{Color.GREEN}lxc-config{Color.RESET} -n container_name -s storage", "description": "Administra el almacenamiento del contenedor", "description_en": "Manage container storage"},
    {"command": f"{Color.GREEN}lxc-config{Color.RESET} -n container_name -s network", "description": "Administra la configuración de red", "description_en": "Manage network configuration"},
    {"command": f"{Color.GREEN}lxc-config{Color.RESET} -n container_name -s security", "description": "Administra la configuración de seguridad", "description_en": "Manage security configuration"},
    {"command": f"{Color.GREEN}lxc-attach{Color.RESET} -n container_name", "description": "Conecta al contenedor especificado", "description_en": "Attach to the specified container"},
    {"command": f"{Color.GREEN}lxc-attach{Color.RESET} -n container_name -f /path", "description": "Conecta al contenedor y comparte un directorio", "description_en": "Attach to container and share a directory"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
