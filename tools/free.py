from shellcolorize import Color

free_commands = [
    {"command": f"{Color.GREEN}free{Color.RESET}", "description": "Muestra el uso de memoria y swap en el sistema"},
    {"command": f"{Color.GREEN}free{Color.RESET} -b", "description": "Muestra el uso de memoria en bytes"},
    {"command": f"{Color.GREEN}free{Color.RESET} -k", "description": "Muestra el uso de memoria en kilobytes (valor predeterminado)"},
    {"command": f"{Color.GREEN}free{Color.RESET} -m", "description": "Muestra el uso de memoria en megabytes"},
    {"command": f"{Color.GREEN}free{Color.RESET} -g", "description": "Muestra el uso de memoria en gigabytes"},
    {"command": f"{Color.GREEN}free{Color.RESET} -h", "description": "Muestra el uso de memoria en un formato legible para humanos (e.g., KB, MB, GB)"},
    {"command": f"{Color.GREEN}free{Color.RESET} --si", "description": "Muestra el uso de memoria usando potencias de 1000 en lugar de 1024"},
    {"command": f"{Color.GREEN}free{Color.RESET} -t", "description": "Incluye una línea que muestra el total de memoria, incluyendo swap"},
    {"command": f"{Color.GREEN}free{Color.RESET} -s <delay>", "description": "Actualiza la salida cada <delay> segundos, útil para monitoreo en tiempo real"},
    {"command": f"{Color.GREEN}free{Color.RESET} -c <count>", "description": "Especifica el número de actualizaciones antes de salir (se usa con -s)"},
    {"command": f"{Color.GREEN}free{Color.RESET} -w", "description": "Muestra la memoria de alto y bajo nivel (si es aplicable en el sistema)"},
    {"command": f"{Color.GREEN}free{Color.RESET} --help", "description": "Muestra la ayuda de free con todas las opciones disponibles"},
    {"command": f"{Color.GREEN}free{Color.RESET} --version", "description": "Muestra la versión de free instalada en el sistema"},
]

print(f"\nComandos de FREE con ejemplos y descripciones:\n")
print(f"{'Comando':<31} | {'Descripción'}")
print("-" * 113)
for cmd in free_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<40} | {description}")
