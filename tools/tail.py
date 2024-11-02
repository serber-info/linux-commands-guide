# Configuración de colores
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

tail_commands = [
    {"command": f"{GREEN}tail{RESET} filename", "description": "Muestra las últimas 10 líneas del archivo especificado"},
    {"command": f"{GREEN}tail{RESET} -n N filename", "description": "Muestra las últimas N líneas del archivo"},
    {"command": f"{GREEN}tail{RESET} -c N filename", "description": "Muestra los últimos N bytes del archivo"},
    {"command": f"{GREEN}tail{RESET} -f filename", "description": "Muestra el contenido en tiempo real mientras se agrega al archivo"},
    {"command": f"{GREEN}tail{RESET} -F filename", "description": "Similar a -f, pero se reconecta si el archivo cambia (útil para logs)"},
    {"command": f"{GREEN}tail{RESET} --follow=descriptor filename", "description": "Sigue el archivo abierto como descriptor (útil para monitorear)"},
    {"command": f"{GREEN}tail{RESET} --pid=PID filename", "description": "Sigue el archivo hasta que el proceso PID finalice"},
    {"command": f"{GREEN}tail{RESET} --retry -f filename", "description": "Continúa intentando acceder al archivo si no está disponible inicialmente"},
    {"command": f"{GREEN}tail{RESET} --lines=N filename", "description": "Similar a -n N, muestra las últimas N líneas"},
    {"command": f"{GREEN}tail{RESET} --bytes=N filename", "description": "Similar a -c N, muestra los últimos N bytes"},
    {"command": f"{GREEN}tail{RESET} -q filename1 filename2", "description": "Suprime los encabezados de archivo en la salida"},
    {"command": f"{GREEN}tail{RESET} -v filename", "description": "Muestra siempre los encabezados de archivo"},
    {"command": f"{GREEN}tail{RESET} --quiet filename1 filename2", "description": "Similar a -q, suprime los encabezados de archivo"},
    {"command": f"{GREEN}tail{RESET} --verbose filename", "description": "Similar a -v, muestra siempre los encabezados de archivo"},
]

print(f"\nComandos de TAIL con ejemplos y descripciones:\n")
print(f"{'Comando':<41} | {'Descripción'}")
print("-" * 117)
for cmd in tail_commands:
    command = cmd["command"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<50} | {description}")

