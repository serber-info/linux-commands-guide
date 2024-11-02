
# Configuración de colores
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

chmod_commands = [
    {"command": f"{GREEN}chmod{RESET} 755 filename", "description": "Otorga permisos de lectura, escritura y ejecución al propietario; solo lectura y ejecución al grupo y otros"},
    {"command": f"{GREEN}chmod{RESET} 644 filename", "description": "Otorga permisos de lectura y escritura al propietario; solo lectura al grupo y otros"},
    {"command": f"{GREEN}chmod{RESET} +x filename", "description": "Agrega permisos de ejecución para todos los usuarios"},
    {"command": f"{GREEN}chmod{RESET} -x filename", "description": "Revoca permisos de ejecución para todos los usuarios"},
    {"command": f"{GREEN}chmod{RESET} u+w filename", "description": "Agrega permisos de escritura solo al propietario (usuario)"},
    {"command": f"{GREEN}chmod{RESET} g-w filename", "description": "Revoca permisos de escritura solo para el grupo"},
    {"command": f"{GREEN}chmod{RESET} o+r filename", "description": "Agrega permisos de lectura solo para otros"},
    {"command": f"{GREEN}chmod{RESET} u=rwx,g=rx,o= filename", "description": "Otorga permisos de lectura, escritura y ejecución al propietario; solo lectura y ejecución al grupo; sin permisos para otros"},
    {"command": f"{GREEN}chmod{RESET} -R 755 directory", "description": "Aplica permisos 755 recursivamente a un directorio y su contenido"},
    {"command": f"{GREEN}chmod{RESET} a+x filename", "description": "Agrega permisos de ejecución para todos los usuarios"},
    {"command": f"{GREEN}chmod{RESET} ug=rw filename", "description": "Otorga permisos de lectura y escritura al propietario y al grupo"},
    {"command": f"{GREEN}chmod{RESET} 400 filename", "description": "Otorga permisos de solo lectura al propietario; sin permisos para grupo y otros"},
    {"command": f"{GREEN}chmod{RESET} 777 filename", "description": "Otorga todos los permisos (lectura, escritura y ejecución) a todos los usuarios"},
]

print(f"\nComandos de CHMOD con ejemplos y descripciones:\n")
print(f"{'Comando':<31} | {'Descripción'}")
print("-" * 158)
for cmd in chmod_commands:
    command = cmd["command"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<40} | {description}")
