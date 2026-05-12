from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de FIND"
TITLE_EN = "FIND Options"
BRIEF = "Busca archivos y directorios"
BRIEF_EN = "Search for files and directories"

COMMANDS = [
    {"command": f"{Color.GREEN}find{Color.RESET} /path", "description": "Busca todos los archivos y directorios en la ruta", "description_en": "List all files and directories under path"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path -name 'file'", "description": "Busca por nombre exacto", "description_en": "Search by exact name"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path -iname 'file'", "description": "Busca por nombre ignorando mayúsculas", "description_en": "Case-insensitive name search"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path -type f", "description": "Busca solo archivos", "description_en": "Find regular files only"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path -type d", "description": "Busca solo directorios", "description_en": "Find directories only"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path -size +100M", "description": "Busca archivos mayores de 100 MB", "description_en": "Find files larger than 100 MB"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path -size -100M", "description": "Busca archivos menores de 100 MB", "description_en": "Find files smaller than 100 MB"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path -mtime -7", "description": "Archivos modificados en los últimos 7 días", "description_en": "Files modified in the last 7 days"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path -atime -7", "description": "Archivos accedidos en los últimos 7 días", "description_en": "Files accessed in the last 7 days"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path -mmin -30", "description": "Archivos modificados en los últimos 30 minutos", "description_en": "Files modified in the last 30 minutes"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path -user username", "description": "Archivos pertenecientes a un usuario", "description_en": "Files owned by a specific user"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path -group groupname", "description": "Archivos pertenecientes a un grupo", "description_en": "Files belonging to a group"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path -perm 755", "description": "Archivos con permisos exactos 755", "description_en": "Files with exact permissions 755"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path -empty", "description": "Archivos o directorios vacíos", "description_en": "Find empty files or directories"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path -exec cmd {{}} \\;", "description": "Ejecuta un comando en cada resultado", "description_en": "Execute a command on each result"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path -delete", "description": "Elimina los archivos encontrados", "description_en": "Delete found files"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path -name '*.txt' -o -name '*.log'", "description": "Busca archivos .txt o .log", "description_en": "Find .txt or .log files"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path -not -name '*.txt'", "description": "Excluye archivos con el nombre especificado", "description_en": "Exclude files matching name"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path -maxdepth 2", "description": "Limita la búsqueda a 2 niveles de profundidad", "description_en": "Limit search depth to 2 levels"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path -mindepth 2", "description": "Omite los primeros 2 niveles de profundidad", "description_en": "Skip the first 2 directory levels"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path -newer file", "description": "Archivos más recientes que 'file'", "description_en": "Files newer than 'file'"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path -type f -exec chmod 644 {{}} \\;", "description": "Cambia permisos de archivos encontrados a 644", "description_en": "Set permissions of found files to 644"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path -type f -print0 | xargs -0 grep 'pat'", "description": "Busca un patrón en el contenido de los archivos", "description_en": "Search for a pattern inside found files"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
