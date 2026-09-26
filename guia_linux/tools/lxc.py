from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de LXC"
TITLE_EN = "LXC Options"
BRIEF = "Gestión de contenedores LXC"
BRIEF_EN = "LXC container management"

COMMANDS = [
    {"command": f"{Color.GREEN}lxc-ls{Color.RESET} -f", "description": "Lista los contenedores con estado, IP y tipo", "description_en": "List containers with state, IP and type"},
    {"command": f"{Color.GREEN}lxc-create{Color.RESET} -n name -t download", "description": "Crea un contenedor desde una imagen (asistente interactivo)", "description_en": "Create a container from an image (interactive)"},
    {"command": f"{Color.GREEN}lxc-create{Color.RESET} -n name -t download -- -d debian -r bookworm -a amd64", "description": "Crea un contenedor Debian sin preguntas", "description_en": "Create a Debian container non-interactively"},
    {"command": f"{Color.GREEN}lxc-start{Color.RESET} -n name", "description": "Inicia un contenedor en segundo plano", "description_en": "Start a container in the background"},
    {"command": f"{Color.GREEN}lxc-stop{Color.RESET} -n name", "description": "Detiene un contenedor", "description_en": "Stop a container"},
    {"command": f"{Color.GREEN}lxc-stop{Color.RESET} -n name -r", "description": "Reinicia un contenedor", "description_en": "Reboot a container"},
    {"command": f"{Color.GREEN}lxc-attach{Color.RESET} -n name", "description": "Abre una shell dentro del contenedor", "description_en": "Open a shell inside the container"},
    {"command": f"{Color.GREEN}lxc-attach{Color.RESET} -n name -- command", "description": "Ejecuta un comando dentro del contenedor", "description_en": "Run a command inside the container"},
    {"command": f"{Color.GREEN}lxc-console{Color.RESET} -n name", "description": "Conecta a la consola (salir: Ctrl+A Q)", "description_en": "Attach to the console (exit: Ctrl+A Q)"},
    {"command": f"{Color.GREEN}lxc-info{Color.RESET} -n name", "description": "Muestra estado, PID, IP y uso de recursos", "description_en": "Show state, PID, IP and resource usage"},
    {"command": f"{Color.GREEN}lxc-freeze{Color.RESET} -n name", "description": "Congela todos los procesos del contenedor", "description_en": "Freeze all processes in the container"},
    {"command": f"{Color.GREEN}lxc-unfreeze{Color.RESET} -n name", "description": "Descongela el contenedor", "description_en": "Unfreeze the container"},
    {"command": f"{Color.GREEN}lxc-copy{Color.RESET} -n name -N new_name", "description": "Clona un contenedor", "description_en": "Clone a container"},
    {"command": f"{Color.GREEN}lxc-snapshot{Color.RESET} -n name", "description": "Crea un snapshot (el contenedor debe estar parado)", "description_en": "Create a snapshot (container must be stopped)"},
    {"command": f"{Color.GREEN}lxc-snapshot{Color.RESET} -n name -L", "description": "Lista los snapshots", "description_en": "List snapshots"},
    {"command": f"{Color.GREEN}lxc-destroy{Color.RESET} -n name", "description": "Elimina un contenedor y su sistema de archivos", "description_en": "Delete a container and its filesystem"},
    {"command": f"{Color.GREEN}lxc-config{Color.RESET} lxc.lxcpath", "description": "Muestra dónde se guardan los contenedores", "description_en": "Show where containers are stored"},
    {"command": f"{Color.GREEN}lxc-checkconfig{Color.RESET}", "description": "Comprueba el soporte del kernel para LXC", "description_en": "Check kernel support for LXC"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
