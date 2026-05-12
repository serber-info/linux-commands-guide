from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de LSBLK"
TITLE_EN = "LSBLK Options"
BRIEF = "Lista dispositivos de bloque del sistema"
BRIEF_EN = "List block devices"

COMMANDS = [
    {"command": f"{Color.GREEN}lsblk{Color.RESET}", "description": "Lista todos los dispositivos de bloque", "description_en": "List all block devices"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} -a", "description": "Incluye dispositivos vacíos", "description_en": "Include empty devices"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} -b", "description": "Muestra tamaños en bytes", "description_en": "Show sizes in bytes"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} -d", "description": "Muestra solo discos, sin particiones", "description_en": "Show only disks, no partitions"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} -f", "description": "Muestra sistema de archivos, UUID y etiqueta", "description_en": "Show filesystem, UUID and label"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} -J", "description": "Salida en formato JSON", "description_en": "JSON format output"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} -l", "description": "Formato de lista plana (sin árbol)", "description_en": "Flat list format (no tree)"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} -m", "description": "Incluye información de permisos", "description_en": "Include permission information"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} -n", "description": "Suprime la fila de encabezado", "description_en": "Suppress header row"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} -o NAME,SIZE,TYPE,MOUNTPOINT", "description": "Muestra solo las columnas especificadas", "description_en": "Show only the specified columns"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} -P", "description": "Salida en formato clave=valor", "description_en": "Key=value format output"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} --output-all", "description": "Muestra todas las columnas disponibles", "description_en": "Show all available columns"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} --paths", "description": "Muestra rutas completas en la columna NAME", "description_en": "Show full device paths in NAME column"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} --scsi", "description": "Incluye información SCSI del dispositivo", "description_en": "Include SCSI device information"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
