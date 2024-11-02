
# Configuración de colores
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

uniq_commands = [
    {"command": f"{GREEN}uniq {YELLOW}{RESET}filename", "description": "Elimina líneas duplicadas consecutivas"},
    {"command": f"{GREEN}uniq {YELLOW}-c {RESET}filename", "description": "Cuenta las ocurrencias de líneas duplicadas"},
    {"command": f"{GREEN}uniq {YELLOW}-d {RESET}filename", "description": "Muestra solo las líneas duplicadas"},
    {"command": f"{GREEN}uniq {YELLOW}-u {RESET}filename", "description": "Muestra solo las líneas que no están duplicadas"},
]

print(f"\nOpciones de UNIQ con ejemplos y descripciones:\n")
print(f"{'Comando':<21} | {'Descripción'}")
print("-" * 71)
for cmd in uniq_commands:
    command = cmd["command"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<35} | {description}")
