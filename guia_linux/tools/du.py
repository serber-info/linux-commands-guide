from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de DU"
TITLE_EN = "DU Options"
BRIEF = "Muestra el uso de espacio de directorios"
BRIEF_EN = "Display directory space usage"

COMMANDS = [
    {"command": f"{Color.GREEN}du{Color.RESET}", "description": "Muestra el tamaño de archivos y directorios actuales", "description_en": "Show size of files and directories"},
    {"command": f"{Color.GREEN}du{Color.RESET} -a", "description": "Incluye archivos individuales en la salida", "description_en": "Include individual files in output"},
    {"command": f"{Color.GREEN}du{Color.RESET} -h", "description": "Formato legible (KB, MB, GB)", "description_en": "Human-readable format (KB, MB, GB)"},
    {"command": f"{Color.GREEN}du{Color.RESET} -s", "description": "Muestra solo el total de cada argumento", "description_en": "Show only the total for each argument"},
    {"command": f"{Color.GREEN}du{Color.RESET} -c", "description": "Muestra un total acumulado al final", "description_en": "Show a grand total at the end"},
    {"command": f"{Color.GREEN}du{Color.RESET} -k", "description": "Muestra tamaños en bloques de 1024 bytes", "description_en": "Show sizes in 1024-byte blocks"},
    {"command": f"{Color.GREEN}du{Color.RESET} -m", "description": "Muestra tamaños en megabytes", "description_en": "Show sizes in megabytes"},
    {"command": f"{Color.GREEN}du{Color.RESET} -b", "description": "Muestra tamaños en bytes", "description_en": "Show sizes in bytes"},
    {"command": f"{Color.GREEN}du{Color.RESET} -L", "description": "Sigue enlaces simbólicos", "description_en": "Follow symbolic links"},
    {"command": f"{Color.GREEN}du{Color.RESET} -x", "description": "Omite directorios en otros sistemas de archivos", "description_en": "Skip directories on other filesystems"},
    {"command": f"{Color.GREEN}du{Color.RESET} -d N", "description": "Muestra hasta N niveles de profundidad", "description_en": "Show up to N levels of depth"},
    {"command": f"{Color.GREEN}du{Color.RESET} --max-depth=N", "description": "Similar a -d N", "description_en": "Same as -d N"},
    {"command": f"{Color.GREEN}du{Color.RESET} --threshold=SIZE", "description": "Muestra solo entradas mayores o iguales a SIZE", "description_en": "Show only entries >= SIZE"},
    {"command": f"{Color.GREEN}du{Color.RESET} --exclude=PATTERN", "description": "Excluye archivos que coincidan con PATTERN", "description_en": "Exclude files matching PATTERN"},
    {"command": f"{Color.GREEN}du{Color.RESET} --apparent-size", "description": "Muestra el tamaño aparente en lugar de bloques usados", "description_en": "Show apparent size instead of disk usage"},
    {"command": f"{Color.GREEN}du{Color.RESET} --inodes", "description": "Cuenta inodos en lugar de tamaño", "description_en": "Count inodes instead of size"},
    {"command": f"{Color.GREEN}du{Color.RESET} --time", "description": "Muestra la fecha de última modificación", "description_en": "Show last modification time"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
