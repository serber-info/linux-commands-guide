from shellcolorize import Color

df_commands = [
    {"command": f"{Color.GREEN}df{Color.RESET}", "description": "Muestra el espacio en disco utilizado y disponible para todos los sistemas de archivos"},
    {"command": f"{Color.GREEN}df{Color.RESET} -h", "description": "Muestra el tamaño en formato legible (KB, MB, GB)"},
    {"command": f"{Color.GREEN}df{Color.RESET} -H", "description": "Muestra el tamaño en formato legible usando potencias de 1000 (KB, MB, GB)"},
    {"command": f"{Color.GREEN}df{Color.RESET} -a", "description": "Incluye sistemas de archivos con un tamaño de 0 bloques"},
    {"command": f"{Color.GREEN}df{Color.RESET} -T", "description": "Muestra el tipo de sistema de archivos junto con el uso de espacio"},
    {"command": f"{Color.GREEN}df{Color.RESET} -t TYPE", "description": "Muestra solo los sistemas de archivos del tipo especificado"},
    {"command": f"{Color.GREEN}df{Color.RESET} -x TYPE", "description": "Excluye sistemas de archivos del tipo especificado"},
    {"command": f"{Color.GREEN}df{Color.RESET} -i", "description": "Muestra el uso de inodos en lugar de bloques de datos"},
    {"command": f"{Color.GREEN}df{Color.RESET} --total", "description": "Muestra una línea total al final del resultado"},
    {"command": f"{Color.GREEN}df{Color.RESET} -l", "description": "Muestra solo sistemas de archivos locales"},
    {"command": f"{Color.GREEN}df{Color.RESET} --output=FIELD", "description": "Muestra solo los campos especificados en FIELD (ej. 'source', 'size')"},
    {"command": f"{Color.GREEN}df{Color.RESET} --block-size=SIZE", "description": "Escala el tamaño de bloques al tamaño especificado (ej. --block-size=1M)"},
    {"command": f"{Color.GREEN}df{Color.RESET} -P", "description": "Usa el formato POSIX para la salida (columnas de tamaño fijo)"},
    {"command": f"{Color.GREEN}df{Color.RESET} --sync", "description": "Sincroniza el sistema de archivos antes de consultar el uso de disco"},
    {"command": f"{Color.GREEN}df{Color.RESET} --exclude-type=TYPE", "description": "Excluye sistemas de archivos del tipo especificado"},
    {"command": f"{Color.GREEN}df{Color.RESET} --include-type=TYPE", "description": "Incluye solo sistemas de archivos del tipo especificado"},
    {"command": f"{Color.GREEN}df{Color.RESET} -B SIZE", "description": "Escala el tamaño en bloques de SIZE (ej. -B 1M para mostrar en megabytes)"},
    {"command": f"{Color.GREEN}df{Color.RESET} --si", "description": "Usa potencias de 1000 en lugar de 1024 para el tamaño de bloques (como -H)"},
    {"command": f"{Color.GREEN}df{Color.RESET} -k", "description": "Muestra el tamaño en bloques de 1024 bytes"},
    {"command": f"{Color.GREEN}df{Color.RESET} -m", "description": "Muestra el tamaño en megabytes (equivalente a -B 1M)"},
    {"command": f"{Color.GREEN}df{Color.RESET} -g", "description": "Muestra el tamaño en gigabytes (equivalente a -B 1G)"},
    {"command": f"{Color.GREEN}df{Color.RESET} --inodes", "description": "Muestra información de inodos en lugar del uso de espacio"},
]

print(f"\nComandos de DF con ejemplos y descripciones:\n")
print(f"{'Comando':<31} | {'Descripción'}")
print("-" * 120)
for cmd in df_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<40} | {description}")
