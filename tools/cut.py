from shellcolorize import Color

cut_commands = [
    {"command": f"{Color.GREEN}cut {Color.YELLOW}-d',' -f2 {Color.RESET}filename", "description": "Extrae la segunda columna usando ',' como delimitador"},
    {"command": f"{Color.GREEN}cut {Color.YELLOW}-f1,3 {Color.RESET}filename", "description": "Extrae la primera y tercera columna (delimitador predeterminado: tabulación)"},
    {"command": f"{Color.GREEN}cut {Color.YELLOW}-c1-5 {Color.RESET}filename", "description": "Extrae los primeros 5 caracteres de cada línea"},
    {"command": f"{Color.GREEN}cut {Color.YELLOW}-d':' -f1 {Color.RESET}/etc/passwd", "description": "Extrae el primer campo de cada línea en /etc/passwd"},
    {"command": f"{Color.GREEN}cut {Color.YELLOW}-d' ' -f1-3 {Color.RESET}filename", "description": "Extrae los primeros tres campos usando espacio como delimitador"},
    {"command": f"{Color.GREEN}cut {Color.YELLOW}-s -d',' -f2 {Color.RESET}filename", "description": "Muestra solo líneas que contienen el delimitador especificado"},
]

print(f"\nOpciones de CUT con ejemplos y descripciones:\n")
print(f"{'Comando':<36} | {'Descripción'}")
print("-" * 115)
for cmd in cut_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<50} | {description}")
