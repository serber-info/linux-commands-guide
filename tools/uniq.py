from shellcolorize import Color

uniq_commands = [
    {"command": f"{Color.GREEN}uniq {Color.YELLOW}{Color.RESET}filename", "description": "Elimina líneas duplicadas consecutivas"},
    {"command": f"{Color.GREEN}uniq {Color.YELLOW}-c {Color.RESET}filename", "description": "Cuenta las ocurrencias de líneas duplicadas"},
    {"command": f"{Color.GREEN}uniq {Color.YELLOW}-d {Color.RESET}filename", "description": "Muestra solo las líneas duplicadas"},
    {"command": f"{Color.GREEN}uniq {Color.YELLOW}-u {Color.RESET}filename", "description": "Muestra solo las líneas que no están duplicadas"},
]

print(f"\nOpciones de UNIQ con ejemplos y descripciones:\n")
print(f"{'Comando':<21} | {'Descripción'}")
print("-" * 71)
for cmd in uniq_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<35} | {description}")
