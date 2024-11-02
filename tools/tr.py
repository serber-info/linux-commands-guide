from shellcolorize import Color

tr_commands = [
    {"command": f"{Color.GREEN}tr {Color.YELLOW}'a-z' 'A-Z' {Color.RESET}< filename", "description": "Convierte minúsculas en mayúsculas"},
    {"command": f"{Color.GREEN}tr {Color.YELLOW}-d '[:digit:]' {Color.RESET}< filename", "description": "Elimina todos los dígitos en cada línea"},
    {"command": f"{Color.GREEN}tr {Color.YELLOW}' ' '_' {Color.RESET}< filename", "description": "Reemplaza espacios con guiones bajos"},
    {"command": f"{Color.GREEN}tr {Color.YELLOW}-s ' ' {Color.RESET}< filename", "description": "Reemplaza secuencias de espacios con un solo espacio"},
    {"command": f"{Color.GREEN}tr {Color.YELLOW}-c '[:alnum:]' '_' {Color.RESET}< filename", "description": "Reemplaza todos los caracteres excepto alfanuméricos con '_'"},
]

print(f"\nOpciones de TR con ejemplos y descripciones:\n")
print(f"{'Comando':<36} | {'Descripción'}")
print("-" * 99)
for cmd in tr_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<50} | {description}")

