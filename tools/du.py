from shellcolorize import Color

du_commands = [
    {"command": f"{Color.GREEN}du{Color.RESET}", "description": "Muestra el tamaño de todos los archivos y directorios en el directorio actual"},
    {"command": f"{Color.GREEN}du{Color.RESET} -a", "description": "Muestra el tamaño de todos los archivos individuales además de directorios"},
    {"command": f"{Color.GREEN}du{Color.RESET} -h", "description": "Muestra el tamaño en formato legible (KB, MB, GB)"},
    {"command": f"{Color.GREEN}du{Color.RESET} -s", "description": "Muestra solo el tamaño total de cada argumento (resumen)"},
    {"command": f"{Color.GREEN}du{Color.RESET} -c", "description": "Muestra un total acumulado de todos los tamaños listados"},
    {"command": f"{Color.GREEN}du{Color.RESET} -k", "description": "Muestra el tamaño en bloques de 1024 bytes (equivalente a -B 1K)"},
    {"command": f"{Color.GREEN}du{Color.RESET} -m", "description": "Muestra el tamaño en megabytes (equivalente a -B 1M)"},
    {"command": f"{Color.GREEN}du{Color.RESET} -g", "description": "Muestra el tamaño en gigabytes (equivalente a -B 1G)"},
    {"command": f"{Color.GREEN}du{Color.RESET} -b", "description": "Muestra el tamaño en bytes (equivalente a -B 1)"},
    {"command": f"{Color.GREEN}du{Color.RESET} -L", "description": "Sigue enlaces simbólicos y calcula su tamaño"},
    {"command": f"{Color.GREEN}du{Color.RESET} -S", "description": "Excluye el tamaño de subdirectorios (solo el directorio principal)"},
    {"command": f"{Color.GREEN}du{Color.RESET} -x", "description": "Omite directorios montados en otros sistemas de archivos"},
    {"command": f"{Color.GREEN}du{Color.RESET} --time", "description": "Muestra la fecha de última modificación para cada archivo o directorio"},
    {"command": f"{Color.GREEN}du{Color.RESET} --time=iso", "description": "Muestra la fecha en formato ISO (ISO 8601)"},
    {"command": f"{Color.GREEN}du{Color.RESET} -d N", "description": "Muestra el tamaño solo hasta el nivel de profundidad N (ej. -d 1 para solo primer nivel)"},
    {"command": f"{Color.GREEN}du{Color.RESET} --max-depth=N", "description": "Similar a -d N, muestra el tamaño solo hasta el nivel N de profundidad"},
    {"command": f"{Color.GREEN}du{Color.RESET} --threshold=SIZE", "description": "Muestra solo archivos o directorios de un tamaño mayor o igual a SIZE"},
    {"command": f"{Color.GREEN}du{Color.RESET} --exclude=PATTERN", "description": "Excluye archivos y directorios que coincidan con PATTERN del cálculo de tamaño"},
    {"command": f"{Color.GREEN}du{Color.RESET} --apparent-size", "description": "Muestra el tamaño aparente (sin considerar compresión o bloques)"},
    {"command": f"{Color.GREEN}du{Color.RESET} -B SIZE", "description": "Escala el tamaño en bloques de SIZE (ej. -B MB para mostrar en megabytes)"},
    {"command": f"{Color.GREEN}du{Color.RESET} --block-size=SIZE", "description": "Similar a -B SIZE, muestra el tamaño en bloques de SIZE"},
    {"command": f"{Color.GREEN}du{Color.RESET} --inodes", "description": "Cuenta y muestra el número de inodos en lugar del tamaño en bytes"},
    {"command": f"{Color.GREEN}du{Color.RESET} --exclude-from=FILE", "description": "Excluye archivos y directorios listados en FILE"},
    {"command": f"{Color.GREEN}du{Color.RESET} --files0-from=FILE", "description": "Lee nombres de archivo desde FILE, separados por NULL (para nombres con espacios)"},
    {"command": f"{Color.GREEN}du{Color.RESET} --dereference-args", "description": "Sigue enlaces simbólicos dados en la línea de comandos"},
    {"command": f"{Color.GREEN}du{Color.RESET} --all", "description": "Similar a -a, muestra el tamaño de todos los archivos individuales además de directorios"},
    {"command": f"{Color.GREEN}du{Color.RESET} --human-readable", "description": "Similar a -h, muestra tamaños en formato legible (KB, MB, GB)"},
    {"command": f"{Color.GREEN}du{Color.RESET} --summarize", "description": "Similar a -s, muestra solo el tamaño total"},
    {"command": f"{Color.GREEN}du{Color.RESET} --total", "description": "Similar a -c, muestra un total acumulado de todos los tamaños listados"},
]

print(f"\nComandos de DU con ejemplos y descripciones:\n")
print(f"{'Comando':<31} | {'Descripción'}")
print("-" * 122)
for cmd in du_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<40} | {description}")
