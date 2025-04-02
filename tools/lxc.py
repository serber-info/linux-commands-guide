from shellcolorize import Color

lxc_commands = [
    {"command": f"{Color.GREEN}lxc-ls{Color.RESET}", "description": "Lista todos los contenedores existentes"},
    {"command": f"{Color.GREEN}lxc-stop{Color.RESET} -n container_name", "description": "Detiene un contenedor en ejecución"},
    {"command": f"{Color.GREEN}lxc-start{Color.RESET} -n container_name", "description": "Inicia un contenedor detenido"},
    {"command": f"{Color.GREEN}lxc-restart{Color.RESET} -n container_name", "description": "Reinicia un contenedor en ejecución"},
    {"command": f"{Color.GREEN}lxc-config{Color.RESET} -n container_name -s storage", "description": "Administra el almacenamiento del contenedor"},
    {"command": f"{Color.GREEN}lxc-config{Color.RESET} -n container_name -s network", "description": "Administra la configuración de red del contenedor"},
    {"command": f"{Color.GREEN}lxc-config{Color.RESET} -n container_name -s security", "description": "Administra la configuración de seguridad del contenedor"},
    {"command": f"{Color.GREEN}lxc-attach{Color.RESET} -n container_name", "description": "Conecta al contenedor especificado"},
    {"command": f"{Color.GREEN}lxc-attach{Color.RESET} -n container_name -f /path/to/share", "description": "Conecta al contenedor y comparte un directorio o archivo específico"},
]

print(f"\nOpciones de LXC con ejemplos y descripciones:\n")
print(f"{'Comando':<51} | {'Descripción'}")
print("-" * 121)
for cmd in lxc_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<60} | {description}")
