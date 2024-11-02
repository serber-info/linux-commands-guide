# Configuración de colores
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

du_commands = [
    {"command": f"{GREEN}du{RESET}", "description": "Muestra el tamaño de todos los archivos y directorios en el directorio actual"},
    {"command": f"{GREEN}du{RESET} -a", "description": "Muestra el tamaño de todos los archivos individuales además de directorios"},
    {"command": f"{GREEN}du{RESET} -h", "description": "Muestra el tamaño en formato legible (KB, MB, GB)"},
    {"command": f"{GREEN}du{RESET} -s", "description": "Muestra solo el tamaño total de cada argumento (resumen)"},
    {"command": f"{GREEN}du{RESET} -c", "description": "Muestra un total acumulado de todos los tamaños listados"},
    {"command": f"{GREEN}du{RESET} -k", "description": "Muestra el tamaño en bloques de 1024 bytes (equivalente a -B 1K)"},
    {"command": f"{GREEN}du{RESET} -m", "description": "Muestra el tamaño en megabytes (equivalente a -B 1M)"},
    {"command": f"{GREEN}du{RESET} -g", "description": "Muestra el tamaño en gigabytes (equivalente a -B 1G)"},
    {"command": f"{GREEN}du{RESET} -b", "description": "Muestra el tamaño en bytes (equivalente a -B 1)"},
    {"command": f"{GREEN}du{RESET} -L", "description": "Sigue enlaces simbólicos y calcula su tamaño"},
    {"command": f"{GREEN}du{RESET} -S", "description": "Excluye el tamaño de subdirectorios (solo el directorio principal)"},
    {"command": f"{GREEN}du{RESET} -x", "description": "Omite directorios montados en otros sistemas de archivos"},
    {"command": f"{GREEN}du{RESET} --time", "description": "Muestra la fecha de última modificación para cada archivo o directorio"},
    {"command": f"{GREEN}du{RESET} --time=iso", "description": "Muestra la fecha en formato ISO (ISO 8601)"},
    {"command": f"{GREEN}du{RESET} -d N", "description": "Muestra el tamaño solo hasta el nivel de profundidad N (ej. -d 1 para solo primer nivel)"},
    {"command": f"{GREEN}du{RESET} --max-depth=N", "description": "Similar a -d N, muestra el tamaño solo hasta el nivel N de profundidad"},
    {"command": f"{GREEN}du{RESET} --threshold=SIZE", "description": "Muestra solo archivos o directorios de un tamaño mayor o igual a SIZE"},
    {"command": f"{GREEN}du{RESET} --exclude=PATTERN", "description": "Excluye archivos y directorios que coincidan con PATTERN del cálculo de tamaño"},
    {"command": f"{GREEN}du{RESET} --apparent-size", "description": "Muestra el tamaño aparente (sin considerar compresión o bloques)"},
    {"command": f"{GREEN}du{RESET} -B SIZE", "description": "Escala el tamaño en bloques de SIZE (ej. -B MB para mostrar en megabytes)"},
    {"command": f"{GREEN}du{RESET} --block-size=SIZE", "description": "Similar a -B SIZE, muestra el tamaño en bloques de SIZE"},
    {"command": f"{GREEN}du{RESET} --inodes", "description": "Cuenta y muestra el número de inodos en lugar del tamaño en bytes"},
    {"command": f"{GREEN}du{RESET} --exclude-from=FILE", "description": "Excluye archivos y directorios listados en FILE"},
    {"command": f"{GREEN}du{RESET} --files0-from=FILE", "description": "Lee nombres de archivo desde FILE, separados por NULL (para nombres con espacios)"},
    {"command": f"{GREEN}du{RESET} --dereference-args", "description": "Sigue enlaces simbólicos dados en la línea de comandos"},
    {"command": f"{GREEN}du{RESET} --all", "description": "Similar a -a, muestra el tamaño de todos los archivos individuales además de directorios"},
    {"command": f"{GREEN}du{RESET} --human-readable", "description": "Similar a -h, muestra tamaños en formato legible (KB, MB, GB)"},
    {"command": f"{GREEN}du{RESET} --summarize", "description": "Similar a -s, muestra solo el tamaño total"},
    {"command": f"{GREEN}du{RESET} --total", "description": "Similar a -c, muestra un total acumulado de todos los tamaños listados"},
]

print(f"\nComandos de DU con ejemplos y descripciones:\n")
print(f"{'Comando':<31} | {'Descripción'}")
print("-" * 122)
for cmd in du_commands:
    command = cmd["command"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<40} | {description}")
