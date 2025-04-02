from shellcolorize import Color

watch_commands = [
    {"command": f"{Color.GREEN}watch {Color.RESET}df -h", "description": "Ejecuta 'df -h' en intervalos regulares, mostrando el uso de disco"},
    {"command": f"{Color.GREEN}watch {Color.RESET}-n 5 ls", "description": "Ejecuta 'ls' cada 5 segundos"},
    {"command": f"{Color.GREEN}watch {Color.RESET}-d ls", "description": "Resalta diferencias entre cada ejecución de 'ls'"},
]

print(f"\nOpciones de WATCH con ejemplos y descripciones:\n")
print(f"{'Comando':<16} | {'Descripción'}")
print("-" * 85)
for cmd in watch_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<25} | {description}")

