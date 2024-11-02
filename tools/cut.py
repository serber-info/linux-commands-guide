
# Configuración de colores
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

cut_commands = [
    {"command": f"{GREEN}cut {YELLOW}-d',' -f2 {RESET}filename", "description": "Extrae la segunda columna usando ',' como delimitador"},
    {"command": f"{GREEN}cut {YELLOW}-f1,3 {RESET}filename", "description": "Extrae la primera y tercera columna (delimitador predeterminado: tabulación)"},
    {"command": f"{GREEN}cut {YELLOW}-c1-5 {RESET}filename", "description": "Extrae los primeros 5 caracteres de cada línea"},
    {"command": f"{GREEN}cut {YELLOW}-d':' -f1 {RESET}/etc/passwd", "description": "Extrae el primer campo de cada línea en /etc/passwd"},
    {"command": f"{GREEN}cut {YELLOW}-d' ' -f1-3 {RESET}filename", "description": "Extrae los primeros tres campos usando espacio como delimitador"},
    {"command": f"{GREEN}cut {YELLOW}-s -d',' -f2 {RESET}filename", "description": "Muestra solo líneas que contienen el delimitador especificado"},
]

print(f"\nOpciones de CUT con ejemplos y descripciones:\n")
print(f"{'Comando':<36} | {'Descripción'}")
print("-" * 115)
for cmd in cut_commands:
    command = cmd["command"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<50} | {description}")
