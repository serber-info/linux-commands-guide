from shellcolorize import Color

ps_commands = [
    {"command": f"{Color.GREEN}ps{Color.RESET}", "description": "Muestra procesos para la terminal actual"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -A", "description": "Muestra todos los procesos en el sistema"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -e", "description": "Similar a -A; muestra todos los procesos en el sistema"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -a", "description": "Muestra todos los procesos excepto los de sesión y terminal"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -d", "description": "Muestra todos los procesos excepto los de sesión"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -T", "description": "Muestra todos los hilos de la terminal actual"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -x", "description": "Incluye procesos que no tienen terminal asociado (sin TTY)"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -f", "description": "Formato de salida detallado, mostrando relaciones de padre-hijo (PPID)"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -j", "description": "Muestra el formato de sesión y proceso en el estilo BSD"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -l", "description": "Formato largo, incluye campos adicionales como estado y prioridad"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -u <user>", "description": "Muestra procesos de un usuario específico"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -p <pid>", "description": "Muestra información de un proceso específico por PID"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -U <user>", "description": "Muestra procesos que pertenecen a un usuario específico"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -g <group>", "description": "Muestra procesos de un grupo de usuarios"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -G <gid>", "description": "Muestra procesos pertenecientes a un grupo específico (por GID)"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -C <command>", "description": "Muestra procesos ejecutados por un comando específico"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -o <format>", "description": "Especifica columnas para mostrar, separadas por comas (ej. -o pid,user,%cpu)"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -H", "description": "Muestra procesos en formato jerárquico, mostrando relación padre-hijo"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -r", "description": "Muestra solo procesos en ejecución"},
    {"command": f"{Color.GREEN}ps{Color.RESET} --sort <key>", "description": "Ordena la salida según el campo especificado (ej. --sort=%mem)"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -N", "description": "Excluye los procesos especificados en el filtro"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -v", "description": "Formato detallado, muestra el uso de memoria virtual y real"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -s <session_id>", "description": "Muestra procesos de una sesión específica"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -L", "description": "Muestra todos los hilos asociados a los procesos seleccionados"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -P", "description": "Muestra la prioridad de los procesos"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -k <key>", "description": "Ordena los procesos según el campo especificado (alias de --sort)"},
    {"command": f"{Color.GREEN}ps{Color.RESET} --forest", "description": "Muestra los procesos en un formato de árbol (jerárquico)"},
    {"command": f"{Color.GREEN}ps{Color.RESET} aux", "description": "Muestra todos los procesos en un estilo de salida BSD detallado"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -eo <format>", "description": "Especifica campos personalizados para la salida (ej. -eo pid,user,pcpu)"},
    {"command": f"{Color.GREEN}ps{Color.RESET} --no-headers", "description": "Oculta la fila de encabezados en la salida"},
    {"command": f"{Color.GREEN}ps{Color.RESET} -M", "description": "Muestra el tamaño de memoria compartida (RAM) utilizado por los procesos"},
    {"command": f"{Color.GREEN}ps{Color.RESET} --help", "description": "Muestra la ayuda del comando ps con todas las opciones disponibles"},
]

print(f"\nComandos de PS con ejemplos y descripciones:\n")
print(f"{'Comando':<21} | {'Descripción'}")
print("-" * 100)
for cmd in ps_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<30} | {description}")
