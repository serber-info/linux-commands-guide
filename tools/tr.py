
# Configuración de colores
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

tr_commands = [
    {"command": f"{GREEN}tr {YELLOW}'a-z' 'A-Z' {RESET}< filename", "description": "Convierte minúsculas en mayúsculas"},
    {"command": f"{GREEN}tr {YELLOW}-d '[:digit:]' {RESET}< filename", "description": "Elimina todos los dígitos en cada línea"},
    {"command": f"{GREEN}tr {YELLOW}' ' '_' {RESET}< filename", "description": "Reemplaza espacios con guiones bajos"},
    {"command": f"{GREEN}tr {YELLOW}-s ' ' {RESET}< filename", "description": "Reemplaza secuencias de espacios con un solo espacio"},
    {"command": f"{GREEN}tr {YELLOW}-c '[:alnum:]' '_' {RESET}< filename", "description": "Reemplaza todos los caracteres excepto alfanuméricos con '_'"},
]

print(f"\nOpciones de TR con ejemplos y descripciones:\n")
print(f"{'Comando':<36} | {'Descripción'}")
print("-" * 99)
for cmd in tr_commands:
    command = cmd["command"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<50} | {description}")

