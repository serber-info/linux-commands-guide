# Configuración de colores
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

uname_commands = [
    {"command": f"{GREEN}uname{RESET}", "description": "Muestra el nombre del kernel del sistema"},
    {"command": f"{GREEN}uname{RESET} -a", "description": "Muestra toda la información disponible del sistema"},
    {"command": f"{GREEN}uname{RESET} -s", "description": "Muestra solo el nombre del kernel del sistema"},
    {"command": f"{GREEN}uname{RESET} -n", "description": "Muestra el nombre de red del host"},
    {"command": f"{GREEN}uname{RESET} -r", "description": "Muestra la versión del kernel"},
    {"command": f"{GREEN}uname{RESET} -v", "description": "Muestra la fecha de compilación del kernel"},
    {"command": f"{GREEN}uname{RESET} -m", "description": "Muestra el tipo de hardware de la máquina"},
    {"command": f"{GREEN}uname{RESET} -p", "description": "Muestra el tipo de procesador (si está disponible)"},
    {"command": f"{GREEN}uname{RESET} -i", "description": "Muestra la plataforma de hardware (si está disponible)"},
    {"command": f"{GREEN}uname{RESET} -o", "description": "Muestra el sistema operativo"},
    {"command": f"{GREEN}uname{RESET} --help", "description": "Muestra la ayuda del comando uname con todas las opciones"},
    {"command": f"{GREEN}uname{RESET} --version", "description": "Muestra la versión del programa uname"},
]

print(f"\nComandos de UNAME con ejemplos y descripciones:\n")
print(f"{'Comando':<26} | {'Descripción'}")
print("-" * 86)
for cmd in uname_commands:
    command = cmd["command"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<35} | {description}")
