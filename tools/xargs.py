
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

xargs_commands = [
    {"command": f"{GREEN}xargs {YELLOW}{RESET}rm < filelist.txt", "description": "Ejecuta 'rm' en cada archivo listado en filelist.txt"},
    {"command": f"{GREEN}echo {YELLOW}'one two three' {RESET}| {GREEN}xargs {YELLOW}-n 1 {RESET}                 ", "description": "Pasa cada palabra como un argumento separado"},
    {"command": f"{GREEN}find {RESET}. -name {YELLOW}'*.txt' {RESET}| {GREEN}xargs grep {YELLOW}'pattern' {RESET}       ", "description": "Usa xargs para ejecutar grep en archivos encontrados por find"},
    {"command": f"{GREEN}cat {RESET}filelist.txt | {GREEN}xargs {YELLOW}-I {{}} mv {{}} /backup/ {RESET}     ", "description": "Mueve cada archivo listado a /backup"},
    {"command": f"{GREEN}ls {RESET}| xargs {YELLOW}-p echo {RESET}                                ", "description": "Ejecuta echo con confirmación previa (-p) para cada archivo listado"},
]

print(f"\nOpciones de XARGS con ejemplos y descripciones:\n")
print(f"{'Comando':<51} | {'Descripción'}")
print("-" * 121)
for cmd in xargs_commands:
    command = cmd["command"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<65} | {description}")

