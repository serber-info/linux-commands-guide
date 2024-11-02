from shellcolorize import Color

sort_commands = [
    {"command": f"{Color.GREEN}sort {Color.YELLOW}{Color.RESET}filename", "description": "Ordena las lineas del archivo alfabéticamente"},
    {"command": f"{Color.GREEN}sort {Color.YELLOW}-n {Color.RESET}filename", "description": "Ordena las líneas numéricamente"},
    {"command": f"{Color.GREEN}sort {Color.YELLOW}-r {Color.RESET}filename", "description": "Ordena las líneas en orden inverso"},
    {"command": f"{Color.GREEN}sort {Color.YELLOW}-u {Color.RESET}filename", "description": "Elimina duplicados y ordena las líneas"},
    {"command": f"{Color.GREEN}sort {Color.YELLOW}-k2,2 -n {Color.RESET}filename", "description": "Ordena numéricamente usando la segunda columna"},
    {"command": f"{Color.GREEN}sort {Color.YELLOW}-t',' -k1,1 {Color.RESET}filename", "description": "Ordena usando el primer campo, delimitado por ','"},
    {"command": f"{Color.GREEN}sort {Color.YELLOW}-m {Color.RESET}file1 file2", "description": "Combina y ordena los archivos file1 y file2 ya ordenados"},
]

print(f"\nOpciones de SORT con ejemplos y descripciones:\n")
print(f"{'Comando':<31} | {'Descripción'}")
print("-" * 90)
for cmd in sort_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<45} | {description}")

