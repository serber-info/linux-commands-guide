from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de RSYNC"
TITLE_EN = "RSYNC Options"
BRIEF = "Sincronización eficiente de archivos"
BRIEF_EN = "Efficient file synchronization"

COMMANDS = [
    {"command": f"{Color.GREEN}rsync{Color.RESET} -av src/ dst/", "description": "Sincroniza src/ en dst/ con salida verbose", "description_en": "Sync src/ to dst/ with verbose output"},
    {"command": f"{Color.GREEN}rsync{Color.RESET} -avz src/ user@host:/dst/", "description": "Sincroniza con compresión a un host remoto", "description_en": "Sync with compression to a remote host"},
    {"command": f"{Color.GREEN}rsync{Color.RESET} -avz user@host:/src/ dst/", "description": "Descarga desde un host remoto con compresión", "description_en": "Download from a remote host with compression"},
    {"command": f"{Color.GREEN}rsync{Color.RESET} --delete src/ dst/", "description": "Elimina en dst/ los archivos que no existen en src/", "description_en": "Delete files in dst/ that don't exist in src/"},
    {"command": f"{Color.GREEN}rsync{Color.RESET} --dry-run src/ dst/", "description": "Simula la sincronización sin realizar cambios", "description_en": "Simulate sync without making changes"},
    {"command": f"{Color.GREEN}rsync{Color.RESET} -a --progress src/ dst/", "description": "Muestra el progreso de cada archivo", "description_en": "Show per-file transfer progress"},
    {"command": f"{Color.GREEN}rsync{Color.RESET} --exclude='*.log' src/ dst/", "description": "Excluye archivos que coincidan con el patrón", "description_en": "Exclude files matching the pattern"},
    {"command": f"{Color.GREEN}rsync{Color.RESET} --exclude-from=list.txt src/ dst/", "description": "Lee exclusiones desde un archivo", "description_en": "Read exclusions from a file"},
    {"command": f"{Color.GREEN}rsync{Color.RESET} -e 'ssh -p 2222' src/ user@host:/dst/", "description": "Usa SSH con un puerto no estándar", "description_en": "Use SSH with a non-standard port"},
    {"command": f"{Color.GREEN}rsync{Color.RESET} --checksum src/ dst/", "description": "Compara por checksum en lugar de timestamp/tamaño", "description_en": "Compare by checksum instead of timestamp/size"},
    {"command": f"{Color.GREEN}rsync{Color.RESET} -a --bwlimit=1000 src/ dst/", "description": "Limita el ancho de banda a 1000 KB/s", "description_en": "Limit bandwidth to 1000 KB/s"},
    {"command": f"{Color.GREEN}rsync{Color.RESET} --backup --backup-dir=/backup src/ dst/", "description": "Guarda copias de archivos sobreescritos", "description_en": "Keep backups of overwritten files"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
