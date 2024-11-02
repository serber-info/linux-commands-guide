
# Configuración de colores
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

sort_commands = [
    {"command": f"{GREEN}sort {YELLOW}{RESET}filename", "description": "Ordena las lineas del archivo alfabéticamente"},
    {"command": f"{GREEN}sort {YELLOW}-n {RESET}filename", "description": "Ordena las líneas numéricamente"},
    {"command": f"{GREEN}sort {YELLOW}-r {RESET}filename", "description": "Ordena las líneas en orden inverso"},
    {"command": f"{GREEN}sort {YELLOW}-u {RESET}filename", "description": "Elimina duplicados y ordena las líneas"},
    {"command": f"{GREEN}sort {YELLOW}-k2,2 -n {RESET}filename", "description": "Ordena numéricamente usando la segunda columna"},
    {"command": f"{GREEN}sort {YELLOW}-t',' -k1,1 {RESET}filename", "description": "Ordena usando el primer campo, delimitado por ','"},
    {"command": f"{GREEN}sort {YELLOW}-m {RESET}file1 file2", "description": "Combina y ordena los archivos file1 y file2 ya ordenados"},
]

print(f"\nOpciones de SORT con ejemplos y descripciones:\n")
print(f"{'Comando':<31} | {'Descripción'}")
print("-" * 90)
for cmd in sort_commands:
    command = cmd["command"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<45} | {description}")

