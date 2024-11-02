# Configuración de colores
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

head_commands = [
    {"command": f"{GREEN}head{RESET} filename", "description": "Muestra las primeras 10 líneas del archivo especificado"},
    {"command": f"{GREEN}head{RESET} -n N filename", "description": "Muestra las primeras N líneas del archivo"},
    {"command": f"{GREEN}head{RESET} -c N filename", "description": "Muestra los primeros N bytes del archivo"},
    {"command": f"{GREEN}head{RESET} -q filename1 filename2", "description": "Suprime los encabezados de archivo en la salida"},
    {"command": f"{GREEN}head{RESET} -v filename", "description": "Muestra siempre los encabezados de archivo"},
    {"command": f"{GREEN}head{RESET} --lines=N filename", "description": "Similar a -n N, muestra las primeras N líneas"},
    {"command": f"{GREEN}head{RESET} --bytes=N filename", "description": "Similar a -c N, muestra los primeros N bytes"},
    {"command": f"{GREEN}head{RESET} --quiet filename1 filename2", "description": "Similar a -q, suprime los encabezados de archivo"},
    {"command": f"{GREEN}head{RESET} --verbose filename", "description": "Similar a -v, muestra siempre los encabezados de archivo"},
    {"command": f"{GREEN}head{RESET} -z filename", "description": "Divide por ceros en lugar de por nuevas líneas (útil en archivos binarios)"},
]

print(f"\nComandos de HEAD con ejemplos y descripciones:\n")
print(f"{'Comando':<41} | {'Descripción'}")
print("-" * 118)
for cmd in head_commands:
    command = cmd["command"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<50} | {description}")
