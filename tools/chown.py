
# Configuración de colores
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

chown_commands = [
    {"command": f"{GREEN}chown{RESET} user filename", "description": "Cambia el propietario del archivo a 'user'"},
    {"command": f"{GREEN}chown{RESET} user:group filename", "description": "Cambia el propietario del archivo a 'user' y el grupo a 'group'"},
    {"command": f"{GREEN}chown{RESET} :group filename", "description": "Cambia solo el grupo del archivo a 'group'"},
    {"command": f"{GREEN}chown{RESET} -R user directory", "description": "Cambia recursivamente el propietario de un directorio y su contenido a 'user'"},
    {"command": f"{GREEN}chown{RESET} -R user:group directory", "description": "Cambia recursivamente el propietario y el grupo de un directorio y su contenido"},
    {"command": f"{GREEN}chown{RESET} --from=current_user:new_user filename", "description": "Cambia el propietario solo si coincide con el propietario actual especificado"},
    {"command": f"{GREEN}chown{RESET} --reference=ref_file filename", "description": "Cambia el propietario y grupo del archivo para que coincidan con 'ref_file'"},
]

print(f"\nComandos de CHOWN con ejemplos y descripciones:\n")
print(f"{'Comando':<46} | {'Descripción'}")
print("-" * 128)
for cmd in chown_commands:
    command = cmd["command"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<55} | {description}")

