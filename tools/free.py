# Configuración de colores
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

free_commands = [
    {"command": f"{GREEN}free{RESET}", "description": "Muestra el uso de memoria y swap en el sistema"},
    {"command": f"{GREEN}free{RESET} -b", "description": "Muestra el uso de memoria en bytes"},
    {"command": f"{GREEN}free{RESET} -k", "description": "Muestra el uso de memoria en kilobytes (valor predeterminado)"},
    {"command": f"{GREEN}free{RESET} -m", "description": "Muestra el uso de memoria en megabytes"},
    {"command": f"{GREEN}free{RESET} -g", "description": "Muestra el uso de memoria en gigabytes"},
    {"command": f"{GREEN}free{RESET} -h", "description": "Muestra el uso de memoria en un formato legible para humanos (e.g., KB, MB, GB)"},
    {"command": f"{GREEN}free{RESET} --si", "description": "Muestra el uso de memoria usando potencias de 1000 en lugar de 1024"},
    {"command": f"{GREEN}free{RESET} -t", "description": "Incluye una línea que muestra el total de memoria, incluyendo swap"},
    {"command": f"{GREEN}free{RESET} -s <delay>", "description": "Actualiza la salida cada <delay> segundos, útil para monitoreo en tiempo real"},
    {"command": f"{GREEN}free{RESET} -c <count>", "description": "Especifica el número de actualizaciones antes de salir (se usa con -s)"},
    {"command": f"{GREEN}free{RESET} -w", "description": "Muestra la memoria de alto y bajo nivel (si es aplicable en el sistema)"},
    {"command": f"{GREEN}free{RESET} --help", "description": "Muestra la ayuda de free con todas las opciones disponibles"},
    {"command": f"{GREEN}free{RESET} --version", "description": "Muestra la versión de free instalada en el sistema"},
]

print(f"\nComandos de FREE con ejemplos y descripciones:\n")
print(f"{'Comando':<31} | {'Descripción'}")
print("-" * 113)
for cmd in free_commands:
    command = cmd["command"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<40} | {description}")
