
# Configuración de colores
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

lxc_commands = [
    {"command": f"{GREEN}lxc-ls{RESET}", "description": "Lista todos los contenedores existentes"},
    {"command": f"{GREEN}lxc-stop{RESET} -n container_name", "description": "Detiene un contenedor en ejecución"},
    {"command": f"{GREEN}lxc-start{RESET} -n container_name", "description": "Inicia un contenedor detenido"},
    {"command": f"{GREEN}lxc-restart{RESET} -n container_name", "description": "Reinicia un contenedor en ejecución"},
    {"command": f"{GREEN}lxc-config{RESET} -n container_name -s storage", "description": "Administra el almacenamiento del contenedor"},
    {"command": f"{GREEN}lxc-config{RESET} -n container_name -s network", "description": "Administra la configuración de red del contenedor"},
    {"command": f"{GREEN}lxc-config{RESET} -n container_name -s security", "description": "Administra la configuración de seguridad del contenedor"},
    {"command": f"{GREEN}lxc-attach{RESET} -n container_name", "description": "Conecta al contenedor especificado"},
    {"command": f"{GREEN}lxc-attach{RESET} -n container_name -f /path/to/share", "description": "Conecta al contenedor y comparte un directorio o archivo específico"},
]

print(f"\nOpciones de LXC con ejemplos y descripciones:\n")
print(f"{'Comando':<51} | {'Descripción'}")
print("-" * 121)
for cmd in lxc_commands:
    command = cmd["command"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<60} | {description}")
