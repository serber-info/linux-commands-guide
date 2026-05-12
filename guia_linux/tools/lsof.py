from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de LSOF"
TITLE_EN = "LSOF Options"
BRIEF = "Lista archivos abiertos por procesos"
BRIEF_EN = "List open files by processes"

COMMANDS = [
    {"command": f"{Color.GREEN}lsof{Color.RESET}", "description": "Muestra todos los archivos abiertos", "description_en": "Show all open files"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} -u username", "description": "Archivos abiertos por un usuario específico", "description_en": "Files opened by a specific user"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} -c process_name", "description": "Archivos abiertos por un proceso específico", "description_en": "Files opened by a specific process"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} -p PID", "description": "Archivos abiertos por el PID dado", "description_en": "Files opened by the given PID"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} -i", "description": "Muestra archivos de red abiertos (TCP/UDP)", "description_en": "Show open network files (TCP/UDP)"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} -i :80", "description": "Archivos abiertos en el puerto 80", "description_en": "Open files on port 80"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} -i TCP", "description": "Muestra solo conexiones TCP", "description_en": "Show only TCP connections"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} -i UDP", "description": "Muestra solo conexiones UDP", "description_en": "Show only UDP connections"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} +D /path/to/dir", "description": "Archivos abiertos en el directorio (recursivo)", "description_en": "Open files in directory (recursive)"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} +d /path/to/dir", "description": "Archivos abiertos en el directorio (sin recursión)", "description_en": "Open files in directory (non-recursive)"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} -t", "description": "Muestra solo los PIDs", "description_en": "Show only PIDs"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} -n", "description": "No resuelve nombres de host", "description_en": "Do not resolve hostnames"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} -P", "description": "No convierte puertos a nombres de servicio", "description_en": "Do not convert port numbers to service names"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} -r N", "description": "Refresca el listado cada N segundos", "description_en": "Refresh listing every N seconds"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} -a -u user -c proc", "description": "AND lógico — combina múltiples filtros", "description_en": "Logical AND — combine multiple filters"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
