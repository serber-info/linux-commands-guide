from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de SYSTEMCTL"
TITLE_EN = "SYSTEMCTL Options"
BRIEF = "Gestión de servicios con systemd"
BRIEF_EN = "Manage services with systemd"

COMMANDS = [
    {"command": f"{Color.GREEN}systemctl{Color.RESET} start service", "description": "Inicia el servicio", "description_en": "Start the service"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} stop service", "description": "Detiene el servicio", "description_en": "Stop the service"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} restart service", "description": "Reinicia el servicio", "description_en": "Restart the service"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} reload service", "description": "Recarga la configuración sin detenerlo", "description_en": "Reload configuration without stopping"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} enable service", "description": "Habilita el inicio automático al arranque", "description_en": "Enable automatic start at boot"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} disable service", "description": "Deshabilita el inicio automático al arranque", "description_en": "Disable automatic start at boot"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} status service", "description": "Muestra el estado actual del servicio", "description_en": "Show current service status"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} is-active service", "description": "Verifica si el servicio está activo", "description_en": "Check if the service is active"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} is-enabled service", "description": "Verifica si el servicio está habilitado", "description_en": "Check if the service is enabled"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} list-units --type=service", "description": "Lista todos los servicios activos", "description_en": "List all active services"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} list-unit-files --type=service", "description": "Lista todos los archivos de unidad de servicios", "description_en": "List all service unit files"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} daemon-reload", "description": "Recarga el gestor systemd tras cambios en archivos", "description_en": "Reload systemd after unit file changes"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} mask service", "description": "Enmascara el servicio para evitar que se inicie", "description_en": "Mask service to prevent it from starting"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} unmask service", "description": "Desenmascara un servicio bloqueado", "description_en": "Unmask a previously masked service"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} show service", "description": "Muestra los detalles de configuración del servicio", "description_en": "Show service configuration details"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} cat service", "description": "Muestra el archivo de unidad del servicio", "description_en": "Show the service unit file"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} edit service", "description": "Edita el archivo de unidad del servicio", "description_en": "Edit the service unit file"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} isolate multi-user.target", "description": "Cambia al modo multiusuario (sin GUI)", "description_en": "Switch to multi-user mode (no GUI)"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} isolate graphical.target", "description": "Cambia al modo gráfico", "description_en": "Switch to graphical mode"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
