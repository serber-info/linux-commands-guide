from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de DF"
TITLE_EN = "DF Options"
BRIEF = "Muestra el uso de espacio en disco"
BRIEF_EN = "Display disk space usage"

COMMANDS = [
    {"command": f"{Color.GREEN}df{Color.RESET}", "description": "Muestra el espacio en disco de todos los sistemas de archivos", "description_en": "Show disk space for all filesystems"},
    {"command": f"{Color.GREEN}df{Color.RESET} -h", "description": "Formato legible (KB, MB, GB)", "description_en": "Human-readable format (KB, MB, GB)"},
    {"command": f"{Color.GREEN}df{Color.RESET} -H", "description": "Formato legible usando potencias de 1000", "description_en": "Human-readable using powers of 1000"},
    {"command": f"{Color.GREEN}df{Color.RESET} -a", "description": "Incluye sistemas de archivos de tamaño 0", "description_en": "Include 0-block filesystems"},
    {"command": f"{Color.GREEN}df{Color.RESET} -T", "description": "Muestra el tipo de sistema de archivos", "description_en": "Show filesystem type"},
    {"command": f"{Color.GREEN}df{Color.RESET} -t TYPE", "description": "Muestra solo sistemas de archivos del tipo indicado", "description_en": "Show only filesystems of the given type"},
    {"command": f"{Color.GREEN}df{Color.RESET} -x TYPE", "description": "Excluye sistemas de archivos del tipo indicado", "description_en": "Exclude filesystems of the given type"},
    {"command": f"{Color.GREEN}df{Color.RESET} -i", "description": "Muestra uso de inodos en lugar de bloques", "description_en": "Show inode usage instead of blocks"},
    {"command": f"{Color.GREEN}df{Color.RESET} --total", "description": "Añade una línea con el total al final", "description_en": "Add a grand total line"},
    {"command": f"{Color.GREEN}df{Color.RESET} -l", "description": "Muestra solo sistemas de archivos locales", "description_en": "Show only local filesystems"},
    {"command": f"{Color.GREEN}df{Color.RESET} --output=source,size,used,avail", "description": "Muestra solo los campos especificados", "description_en": "Show only the specified fields"},
    {"command": f"{Color.GREEN}df{Color.RESET} --block-size=1M", "description": "Muestra tamaños en bloques de 1 MB", "description_en": "Show sizes in 1 MB blocks"},
    {"command": f"{Color.GREEN}df{Color.RESET} -k", "description": "Muestra tamaños en bloques de 1024 bytes", "description_en": "Show sizes in 1024-byte blocks"},
    {"command": f"{Color.GREEN}df{Color.RESET} -m", "description": "Muestra tamaños en megabytes", "description_en": "Show sizes in megabytes"},
    {"command": f"{Color.GREEN}df{Color.RESET} --inodes", "description": "Muestra información de inodos", "description_en": "Show inode information"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
