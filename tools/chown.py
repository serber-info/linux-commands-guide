from shellcolorize import Color

chown_commands = [
    {"command": f"{Color.GREEN}chown{Color.RESET} user filename", "description": "Cambia el propietario del archivo a 'user'"},
    {"command": f"{Color.GREEN}chown{Color.RESET} user:group filename", "description": "Cambia el propietario del archivo a 'user' y el grupo a 'group'"},
    {"command": f"{Color.GREEN}chown{Color.RESET} :group filename", "description": "Cambia solo el grupo del archivo a 'group'"},
    {"command": f"{Color.GREEN}chown{Color.RESET} -R user directory", "description": "Cambia recursivamente el propietario de un directorio y su contenido a 'user'"},
    {"command": f"{Color.GREEN}chown{Color.RESET} -R user:group directory", "description": "Cambia recursivamente el propietario y el grupo de un directorio y su contenido"},
    {"command": f"{Color.GREEN}chown{Color.RESET} --from=current_user:new_user filename", "description": "Cambia el propietario solo si coincide con el propietario actual especificado"},
    {"command": f"{Color.GREEN}chown{Color.RESET} --reference=ref_file filename", "description": "Cambia el propietario y grupo del archivo para que coincidan con 'ref_file'"},
]

print(f"\nComandos de CHOWN con ejemplos y descripciones:\n")
print(f"{'Comando':<46} | {'Descripción'}")
print("-" * 128)
for cmd in chown_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<55} | {description}")

