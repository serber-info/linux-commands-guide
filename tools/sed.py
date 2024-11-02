
# Configuración de colores
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

sed_commands = [
    {"command": f"{GREEN}sed {YELLOW}'s/old/new/g' {RESET}filename", "description": "Reemplaza todas las ocurrencias de 'old' por 'new' en cada línea"},
    {"command": f"{GREEN}sed {YELLOW}-i 's/old/new/g' {RESET}filename", "description": "Reemplaza 'old' por 'new' en el archivo original"},
    {"command": f"{GREEN}sed {YELLOW}'1d' {RESET}filename", "description": "Elimina la primera línea del archivo"},
    {"command": f"{GREEN}sed {YELLOW}'$d' {RESET}filename", "description": "Elimina la última línea del archivo"},
    {"command": f"{GREEN}sed {YELLOW}-n '5,10p' {RESET}filename", "description": "Muestra solo las líneas de la 5 a la 10"},
    {"command": f"{GREEN}sed {YELLOW}'s/\\(old\\)/\\U\\1/g' {RESET}filename", "description": "Convierte 'old' a mayúsculas en cada línea"},
    {"command": f"{GREEN}sed {YELLOW}-e 's/old/new/' -e 's/test/tested/' {RESET}filename", "description": "Aplica múltiples sustituciones"},
    {"command": f"{GREEN}sed {YELLOW}'s/^/# /' {RESET}filename", "description": "Añade un '#' al inicio de cada línea"},
    {"command": f"{GREEN}sed {YELLOW}'/pattern/d' {RESET}filename", "description": "Elimina líneas que coinciden con 'pattern'"},
    {"command": f"{GREEN}sed {YELLOW}-r 's/[0-9]+/num/g' {RESET}filename", "description": "Usa regex extendida para reemplazar números por 'num'"},
]

print(f"\nOpciones de SED con ejemplos y descripciones:\n")
print(f"{'Comando':<51} | {'Descripción'}")
print("-" * 118)
for cmd in sed_commands:
    command = cmd["command"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<65} | {description}")

