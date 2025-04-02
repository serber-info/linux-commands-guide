from shellcolorize import Color

sed_commands = [
    {"command": f"{Color.GREEN}sed {Color.YELLOW}'s/old/new/g' {Color.RESET}filename", "description": "Reemplaza todas las ocurrencias de 'old' por 'new' en cada línea"},
    {"command": f"{Color.GREEN}sed {Color.YELLOW}-i 's/old/new/g' {Color.RESET}filename", "description": "Reemplaza 'old' por 'new' en el archivo original"},
    {"command": f"{Color.GREEN}sed {Color.YELLOW}'1d' {Color.RESET}filename", "description": "Elimina la primera línea del archivo"},
    {"command": f"{Color.GREEN}sed {Color.YELLOW}'$d' {Color.RESET}filename", "description": "Elimina la última línea del archivo"},
    {"command": f"{Color.GREEN}sed {Color.YELLOW}-n '5,10p' {Color.RESET}filename", "description": "Muestra solo las líneas de la 5 a la 10"},
    {"command": f"{Color.GREEN}sed {Color.YELLOW}'s/\\(old\\)/\\U\\1/g' {Color.RESET}filename", "description": "Convierte 'old' a mayúsculas en cada línea"},
    {"command": f"{Color.GREEN}sed {Color.YELLOW}-e 's/old/new/' -e 's/test/tested/' {Color.RESET}filename", "description": "Aplica múltiples sustituciones"},
    {"command": f"{Color.GREEN}sed {Color.YELLOW}'s/^/# /' {Color.RESET}filename", "description": "Añade un '#' al inicio de cada línea"},
    {"command": f"{Color.GREEN}sed {Color.YELLOW}'/pattern/d' {Color.RESET}filename", "description": "Elimina líneas que coinciden con 'pattern'"},
    {"command": f"{Color.GREEN}sed {Color.YELLOW}-r 's/[0-9]+/num/g' {Color.RESET}filename", "description": "Usa regex extendida para reemplazar números por 'num'"},
]

print(f"\nOpciones de SED con ejemplos y descripciones:\n")
print(f"{'Comando':<51} | {'Descripción'}")
print("-" * 118)
for cmd in sed_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<65} | {description}")

