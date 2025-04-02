from shellcolorize import Color

uname_commands = [
    {"command": f"{Color.GREEN}uname{Color.RESET}", "description": "Muestra el nombre del kernel del sistema"},
    {"command": f"{Color.GREEN}uname{Color.RESET} -a", "description": "Muestra toda la información disponible del sistema"},
    {"command": f"{Color.GREEN}uname{Color.RESET} -s", "description": "Muestra solo el nombre del kernel del sistema"},
    {"command": f"{Color.GREEN}uname{Color.RESET} -n", "description": "Muestra el nombre de red del host"},
    {"command": f"{Color.GREEN}uname{Color.RESET} -r", "description": "Muestra la versión del kernel"},
    {"command": f"{Color.GREEN}uname{Color.RESET} -v", "description": "Muestra la fecha de compilación del kernel"},
    {"command": f"{Color.GREEN}uname{Color.RESET} -m", "description": "Muestra el tipo de hardware de la máquina"},
    {"command": f"{Color.GREEN}uname{Color.RESET} -p", "description": "Muestra el tipo de procesador (si está disponible)"},
    {"command": f"{Color.GREEN}uname{Color.RESET} -i", "description": "Muestra la plataforma de hardware (si está disponible)"},
    {"command": f"{Color.GREEN}uname{Color.RESET} -o", "description": "Muestra el sistema operativo"},
    {"command": f"{Color.GREEN}uname{Color.RESET} --help", "description": "Muestra la ayuda del comando uname con todas las opciones"},
    {"command": f"{Color.GREEN}uname{Color.RESET} --version", "description": "Muestra la versión del programa uname"},
]

print(f"\nComandos de UNAME con ejemplos y descripciones:\n")
print(f"{'Comando':<26} | {'Descripción'}")
print("-" * 86)
for cmd in uname_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<35} | {description}")
