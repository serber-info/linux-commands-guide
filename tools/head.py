from shellcolorize import Color

head_commands = [
    {"command": f"{Color.GREEN}head{Color.RESET} filename", "description": "Muestra las primeras 10 líneas del archivo especificado"},
    {"command": f"{Color.GREEN}head{Color.RESET} -n N filename", "description": "Muestra las primeras N líneas del archivo"},
    {"command": f"{Color.GREEN}head{Color.RESET} -c N filename", "description": "Muestra los primeros N bytes del archivo"},
    {"command": f"{Color.GREEN}head{Color.RESET} -q filename1 filename2", "description": "Suprime los encabezados de archivo en la salida"},
    {"command": f"{Color.GREEN}head{Color.RESET} -v filename", "description": "Muestra siempre los encabezados de archivo"},
    {"command": f"{Color.GREEN}head{Color.RESET} --lines=N filename", "description": "Similar a -n N, muestra las primeras N líneas"},
    {"command": f"{Color.GREEN}head{Color.RESET} --bytes=N filename", "description": "Similar a -c N, muestra los primeros N bytes"},
    {"command": f"{Color.GREEN}head{Color.RESET} --quiet filename1 filename2", "description": "Similar a -q, suprime los encabezados de archivo"},
    {"command": f"{Color.GREEN}head{Color.RESET} --verbose filename", "description": "Similar a -v, muestra siempre los encabezados de archivo"},
    {"command": f"{Color.GREEN}head{Color.RESET} -z filename", "description": "Divide por ceros en lugar de por nuevas líneas (útil en archivos binarios)"},
]

print(f"\nComandos de HEAD con ejemplos y descripciones:\n")
print(f"{'Comando':<41} | {'Descripción'}")
print("-" * 118)
for cmd in head_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<50} | {description}")
