
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

watch_commands = [
    {"command": f"{GREEN}watch {RESET}df -h", "description": "Ejecuta 'df -h' en intervalos regulares, mostrando el uso de disco"},
    {"command": f"{GREEN}watch {RESET}-n 5 ls", "description": "Ejecuta 'ls' cada 5 segundos"},
    {"command": f"{GREEN}watch {RESET}-d ls", "description": "Resalta diferencias entre cada ejecución de 'ls'"},
]

print(f"\nOpciones de WATCH con ejemplos y descripciones:\n")
print(f"{'Comando':<16} | {'Descripción'}")
print("-" * 85)
for cmd in watch_commands:
    command = cmd["command"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<25} | {description}")

