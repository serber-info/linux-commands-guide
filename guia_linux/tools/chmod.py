from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de CHMOD"
TITLE_EN = "CHMOD Options"
BRIEF = "Cambia permisos de archivos y directorios"
BRIEF_EN = "Change file and directory permissions"

COMMANDS = [
    {"command": f"{Color.GREEN}chmod{Color.RESET} 755 filename", "description": "rwx para propietario, rx para grupo y otros", "description_en": "rwx for owner, rx for group and others"},
    {"command": f"{Color.GREEN}chmod{Color.RESET} 644 filename", "description": "rw para propietario, r para grupo y otros", "description_en": "rw for owner, r for group and others"},
    {"command": f"{Color.GREEN}chmod{Color.RESET} +x filename", "description": "Añade permiso de ejecución a todos", "description_en": "Add execute permission for everyone"},
    {"command": f"{Color.GREEN}chmod{Color.RESET} -x filename", "description": "Revoca permiso de ejecución a todos", "description_en": "Remove execute permission for everyone"},
    {"command": f"{Color.GREEN}chmod{Color.RESET} u+w filename", "description": "Añade escritura solo al propietario", "description_en": "Add write permission for owner only"},
    {"command": f"{Color.GREEN}chmod{Color.RESET} g-w filename", "description": "Revoca escritura al grupo", "description_en": "Remove write permission from group"},
    {"command": f"{Color.GREEN}chmod{Color.RESET} o+r filename", "description": "Añade lectura a otros", "description_en": "Add read permission for others"},
    {"command": f"{Color.GREEN}chmod{Color.RESET} u=rwx,g=rx,o= filename", "description": "Permisos exactos para cada categoría", "description_en": "Set exact permissions per category"},
    {"command": f"{Color.GREEN}chmod{Color.RESET} -R 755 directory", "description": "Aplica permisos recursivamente", "description_en": "Apply permissions recursively"},
    {"command": f"{Color.GREEN}chmod{Color.RESET} a+x filename", "description": "Añade ejecución para todos (all)", "description_en": "Add execute for all (all)"},
    {"command": f"{Color.GREEN}chmod{Color.RESET} ug=rw filename", "description": "Lectura y escritura para propietario y grupo", "description_en": "Read and write for owner and group"},
    {"command": f"{Color.GREEN}chmod{Color.RESET} 400 filename", "description": "Solo lectura para el propietario", "description_en": "Read-only for owner"},
    {"command": f"{Color.GREEN}chmod{Color.RESET} 777 filename", "description": "Todos los permisos para todos los usuarios", "description_en": "All permissions for all users"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
