from shellcolorize import Color

tail_commands = [
    {"command": f"{Color.GREEN}tail{Color.RESET} filename", "description": "Muestra las últimas 10 líneas del archivo especificado"},
    {"command": f"{Color.GREEN}tail{Color.RESET} -n N filename", "description": "Muestra las últimas N líneas del archivo"},
    {"command": f"{Color.GREEN}tail{Color.RESET} -c N filename", "description": "Muestra los últimos N bytes del archivo"},
    {"command": f"{Color.GREEN}tail{Color.RESET} -f filename", "description": "Muestra el contenido en tiempo real mientras se agrega al archivo"},
    {"command": f"{Color.GREEN}tail{Color.RESET} -F filename", "description": "Similar a -f, pero se reconecta si el archivo cambia (útil para logs)"},
    {"command": f"{Color.GREEN}tail{Color.RESET} --follow=descriptor filename", "description": "Sigue el archivo abierto como descriptor (útil para monitorear)"},
    {"command": f"{Color.GREEN}tail{Color.RESET} --pid=PID filename", "description": "Sigue el archivo hasta que el proceso PID finalice"},
    {"command": f"{Color.GREEN}tail{Color.RESET} --retry -f filename", "description": "Continúa intentando acceder al archivo si no está disponible inicialmente"},
    {"command": f"{Color.GREEN}tail{Color.RESET} --lines=N filename", "description": "Similar a -n N, muestra las últimas N líneas"},
    {"command": f"{Color.GREEN}tail{Color.RESET} --bytes=N filename", "description": "Similar a -c N, muestra los últimos N bytes"},
    {"command": f"{Color.GREEN}tail{Color.RESET} -q filename1 filename2", "description": "Suprime los encabezados de archivo en la salida"},
    {"command": f"{Color.GREEN}tail{Color.RESET} -v filename", "description": "Muestra siempre los encabezados de archivo"},
    {"command": f"{Color.GREEN}tail{Color.RESET} --quiet filename1 filename2", "description": "Similar a -q, suprime los encabezados de archivo"},
    {"command": f"{Color.GREEN}tail{Color.RESET} --verbose filename", "description": "Similar a -v, muestra siempre los encabezados de archivo"},
]

print(f"\nComandos de TAIL con ejemplos y descripciones:\n")
print(f"{'Comando':<41} | {'Descripción'}")
print("-" * 117)
for cmd in tail_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<50} | {description}")

