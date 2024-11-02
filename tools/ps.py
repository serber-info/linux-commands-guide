# Configuración de colores
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

ps_commands = [
    {"command": f"{GREEN}ps{RESET}", "description": "Muestra procesos para la terminal actual"},
    {"command": f"{GREEN}ps{RESET} -A", "description": "Muestra todos los procesos en el sistema"},
    {"command": f"{GREEN}ps{RESET} -e", "description": "Similar a -A; muestra todos los procesos en el sistema"},
    {"command": f"{GREEN}ps{RESET} -a", "description": "Muestra todos los procesos excepto los de sesión y terminal"},
    {"command": f"{GREEN}ps{RESET} -d", "description": "Muestra todos los procesos excepto los de sesión"},
    {"command": f"{GREEN}ps{RESET} -T", "description": "Muestra todos los hilos de la terminal actual"},
    {"command": f"{GREEN}ps{RESET} -x", "description": "Incluye procesos que no tienen terminal asociado (sin TTY)"},
    {"command": f"{GREEN}ps{RESET} -f", "description": "Formato de salida detallado, mostrando relaciones de padre-hijo (PPID)"},
    {"command": f"{GREEN}ps{RESET} -j", "description": "Muestra el formato de sesión y proceso en el estilo BSD"},
    {"command": f"{GREEN}ps{RESET} -l", "description": "Formato largo, incluye campos adicionales como estado y prioridad"},
    {"command": f"{GREEN}ps{RESET} -u <user>", "description": "Muestra procesos de un usuario específico"},
    {"command": f"{GREEN}ps{RESET} -p <pid>", "description": "Muestra información de un proceso específico por PID"},
    {"command": f"{GREEN}ps{RESET} -U <user>", "description": "Muestra procesos que pertenecen a un usuario específico"},
    {"command": f"{GREEN}ps{RESET} -g <group>", "description": "Muestra procesos de un grupo de usuarios"},
    {"command": f"{GREEN}ps{RESET} -G <gid>", "description": "Muestra procesos pertenecientes a un grupo específico (por GID)"},
    {"command": f"{GREEN}ps{RESET} -C <command>", "description": "Muestra procesos ejecutados por un comando específico"},
    {"command": f"{GREEN}ps{RESET} -o <format>", "description": "Especifica columnas para mostrar, separadas por comas (ej. -o pid,user,%cpu)"},
    {"command": f"{GREEN}ps{RESET} -H", "description": "Muestra procesos en formato jerárquico, mostrando relación padre-hijo"},
    {"command": f"{GREEN}ps{RESET} -r", "description": "Muestra solo procesos en ejecución"},
    {"command": f"{GREEN}ps{RESET} --sort <key>", "description": "Ordena la salida según el campo especificado (ej. --sort=%mem)"},
    {"command": f"{GREEN}ps{RESET} -N", "description": "Excluye los procesos especificados en el filtro"},
    {"command": f"{GREEN}ps{RESET} -v", "description": "Formato detallado, muestra el uso de memoria virtual y real"},
    {"command": f"{GREEN}ps{RESET} -s <session_id>", "description": "Muestra procesos de una sesión específica"},
    {"command": f"{GREEN}ps{RESET} -L", "description": "Muestra todos los hilos asociados a los procesos seleccionados"},
    {"command": f"{GREEN}ps{RESET} -P", "description": "Muestra la prioridad de los procesos"},
    {"command": f"{GREEN}ps{RESET} -k <key>", "description": "Ordena los procesos según el campo especificado (alias de --sort)"},
    {"command": f"{GREEN}ps{RESET} --forest", "description": "Muestra los procesos en un formato de árbol (jerárquico)"},
    {"command": f"{GREEN}ps{RESET} aux", "description": "Muestra todos los procesos en un estilo de salida BSD detallado"},
    {"command": f"{GREEN}ps{RESET} -eo <format>", "description": "Especifica campos personalizados para la salida (ej. -eo pid,user,pcpu)"},
    {"command": f"{GREEN}ps{RESET} --no-headers", "description": "Oculta la fila de encabezados en la salida"},
    {"command": f"{GREEN}ps{RESET} -M", "description": "Muestra el tamaño de memoria compartida (RAM) utilizado por los procesos"},
    {"command": f"{GREEN}ps{RESET} --help", "description": "Muestra la ayuda del comando ps con todas las opciones disponibles"},
]

print(f"\nComandos de PS con ejemplos y descripciones:\n")
print(f"{'Comando':<21} | {'Descripción'}")
print("-" * 100)
for cmd in ps_commands:
    command = cmd["command"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<30} | {description}")
