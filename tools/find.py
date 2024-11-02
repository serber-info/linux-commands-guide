from shellcolorize import Color

find_commands = [
    {"command": f"{Color.GREEN}find{Color.RESET} /path/to/search", "description": "Busca todos los archivos y directorios en la ruta especificada"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path/to/search -name 'filename'", "description": "Busca archivos y directorios que coincidan con el nombre exacto"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path/to/search -iname 'filename'", "description": "Busca archivos y directorios que coincidan con el nombre, ignorando mayúsculas"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path/to/search -type f", "description": "Busca solo archivos"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path/to/search -type d", "description": "Busca solo directorios"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path/to/search -size +100M", "description": "Busca archivos mayores de 100 MB"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path/to/search -size -100M", "description": "Busca archivos menores de 100 MB"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path/to/search -mtime -7", "description": "Busca archivos modificados en los últimos 7 días"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path/to/search -atime -7", "description": "Busca archivos accedidos en los últimos 7 días"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path/to/search -mmin -30", "description": "Busca archivos modificados en los últimos 30 minutos"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path/to/search -user username", "description": "Busca archivos pertenecientes a un usuario específico"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path/to/search -group groupname", "description": "Busca archivos pertenecientes a un grupo específico"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path/to/search -perm 755", "description": "Busca archivos con permisos 755"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path/to/search -empty", "description": "Busca archivos o directorios vacíos"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path/to/search -exec command {{}} \\;", "description": "Ejecuta un comando en cada archivo encontrado"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path/to/search -delete", "description": "Elimina los archivos encontrados (con precaución)"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path/to/search -name '*.txt' -or -name '*.log'", "description": "Busca archivos con extensión .txt o .log"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path/to/search -path '*/dir/*'", "description": "Busca archivos dentro de una ruta específica (usando comodines)"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path/to/search -not -name '*.txt'", "description": "Busca archivos que no coincidan con el nombre especificado"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path/to/search -maxdepth 2", "description": "Limita la búsqueda a 2 niveles de profundidad"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path/to/search -mindepth 2", "description": "Omite los primeros 2 niveles de profundidad en la búsqueda"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path/to/search -newer file", "description": "Busca archivos modificados más recientemente que 'file'"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path/to/search -type f -exec chmod 644 {{}} \\;", "description": "Cambia los permisos de los archivos encontrados a 644"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path/to/search -type f -exec mv {{}} /dest/dir \\;", "description": "Mueve los archivos encontrados a un directorio de destino"},
    {"command": f"{Color.GREEN}find{Color.RESET} /path/to/search -type f -print0 | xargs -0 grep 'pattern'", "description": "Busca un patrón en el contenido de los archivos encontrados"},
]

print(f"\nOpciones de FIND con ejemplos y descripciones:\n")
print(f"{'Comando':<66} | {'Descripción'}")
print("-" * 147)
for cmd in find_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<75} | {description}")

