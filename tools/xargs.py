from shellcolorize import Color

xargs_commands = [
    {"command": f"{Color.GREEN}xargs {Color.YELLOW}{Color.RESET}rm < filelist.txt", "description": "Ejecuta 'rm' en cada archivo listado en filelist.txt"},
    {"command": f"{Color.GREEN}echo {Color.YELLOW}'one two three' {Color.RESET}| {Color.GREEN}xargs {Color.YELLOW}-n 1 {Color.RESET}                 ", "description": "Pasa cada palabra como un argumento separado"},
    {"command": f"{Color.GREEN}find {Color.RESET}. -name {Color.YELLOW}'*.txt' {Color.RESET}| {Color.GREEN}xargs grep {Color.YELLOW}'pattern' {Color.RESET}       ", "description": "Usa xargs para ejecutar grep en archivos encontrados por find"},
    {"command": f"{Color.GREEN}cat {Color.RESET}filelist.txt | {Color.GREEN}xargs {Color.YELLOW}-I {{}} mv {{}} /backup/ {Color.RESET}     ", "description": "Mueve cada archivo listado a /backup"},
    {"command": f"{Color.GREEN}ls {Color.RESET}| xargs {Color.YELLOW}-p echo {Color.RESET}                                ", "description": "Ejecuta echo con confirmación previa (-p) para cada archivo listado"},
]

print(f"\nOpciones de XARGS con ejemplos y descripciones:\n")
print(f"{'Comando':<51} | {'Descripción'}")
print("-" * 121)
for cmd in xargs_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<65} | {description}")

