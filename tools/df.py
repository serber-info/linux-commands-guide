# Configuración de colores
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

df_commands = [
    {"command": f"{GREEN}df{RESET}", "description": "Muestra el espacio en disco utilizado y disponible para todos los sistemas de archivos"},
    {"command": f"{GREEN}df{RESET} -h", "description": "Muestra el tamaño en formato legible (KB, MB, GB)"},
    {"command": f"{GREEN}df{RESET} -H", "description": "Muestra el tamaño en formato legible usando potencias de 1000 (KB, MB, GB)"},
    {"command": f"{GREEN}df{RESET} -a", "description": "Incluye sistemas de archivos con un tamaño de 0 bloques"},
    {"command": f"{GREEN}df{RESET} -T", "description": "Muestra el tipo de sistema de archivos junto con el uso de espacio"},
    {"command": f"{GREEN}df{RESET} -t TYPE", "description": "Muestra solo los sistemas de archivos del tipo especificado"},
    {"command": f"{GREEN}df{RESET} -x TYPE", "description": "Excluye sistemas de archivos del tipo especificado"},
    {"command": f"{GREEN}df{RESET} -i", "description": "Muestra el uso de inodos en lugar de bloques de datos"},
    {"command": f"{GREEN}df{RESET} --total", "description": "Muestra una línea total al final del resultado"},
    {"command": f"{GREEN}df{RESET} -l", "description": "Muestra solo sistemas de archivos locales"},
    {"command": f"{GREEN}df{RESET} --output=FIELD", "description": "Muestra solo los campos especificados en FIELD (ej. 'source', 'size')"},
    {"command": f"{GREEN}df{RESET} --block-size=SIZE", "description": "Escala el tamaño de bloques al tamaño especificado (ej. --block-size=1M)"},
    {"command": f"{GREEN}df{RESET} -P", "description": "Usa el formato POSIX para la salida (columnas de tamaño fijo)"},
    {"command": f"{GREEN}df{RESET} --sync", "description": "Sincroniza el sistema de archivos antes de consultar el uso de disco"},
    {"command": f"{GREEN}df{RESET} --exclude-type=TYPE", "description": "Excluye sistemas de archivos del tipo especificado"},
    {"command": f"{GREEN}df{RESET} --include-type=TYPE", "description": "Incluye solo sistemas de archivos del tipo especificado"},
    {"command": f"{GREEN}df{RESET} -B SIZE", "description": "Escala el tamaño en bloques de SIZE (ej. -B 1M para mostrar en megabytes)"},
    {"command": f"{GREEN}df{RESET} --si", "description": "Usa potencias de 1000 en lugar de 1024 para el tamaño de bloques (como -H)"},
    {"command": f"{GREEN}df{RESET} -k", "description": "Muestra el tamaño en bloques de 1024 bytes"},
    {"command": f"{GREEN}df{RESET} -m", "description": "Muestra el tamaño en megabytes (equivalente a -B 1M)"},
    {"command": f"{GREEN}df{RESET} -g", "description": "Muestra el tamaño en gigabytes (equivalente a -B 1G)"},
    {"command": f"{GREEN}df{RESET} --inodes", "description": "Muestra información de inodos en lugar del uso de espacio"},
]

print(f"\nComandos de DF con ejemplos y descripciones:\n")
print(f"{'Comando':<31} | {'Descripción'}")
print("-" * 120)
for cmd in df_commands:
    command = cmd["command"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<40} | {description}")
