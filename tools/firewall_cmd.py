
# Configuración de colores
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

firewall_cmd_commands = [
    {"command": f"{GREEN}firewall-cmd{RESET} --state", "description": "Muestra el estado del firewall (activo o inactivo)"},
    {"command": f"{GREEN}firewall-cmd{RESET} --get-default-zone", "description": "Muestra la zona por defecto"},
    {"command": f"{GREEN}firewall-cmd{RESET} --list-all", "description": "Lista todas las reglas de firewall de la zona por defecto"},
    {"command": f"{GREEN}firewall-cmd{RESET} --list-all-zones", "description": "Lista todas las zonas y sus configuraciones"},
    {"command": f"{GREEN}firewall-cmd{RESET} --zone=zone --add-port=80/tcp --permanent", "description": "Abre el puerto 80 en la zona especificada de forma permanente"},
    {"command": f"{GREEN}firewall-cmd{RESET} --zone=zone --remove-port=80/tcp --permanent", "description": "Cierra el puerto 80 en la zona especificada de forma permanente"},
    {"command": f"{GREEN}firewall-cmd{RESET} --zone=zone --add-service=http --permanent", "description": "Permite el servicio HTTP en la zona especificada de forma permanente"},
    {"command": f"{GREEN}firewall-cmd{RESET} --zone=zone --remove-service=http --permanent", "description": "Bloquea el servicio HTTP en la zona especificada de forma permanente"},
    {"command": f"{GREEN}firewall-cmd{RESET} --reload", "description": "Recarga las configuraciones de firewall (necesario para aplicar cambios)"},
    {"command": f"{GREEN}firewall-cmd{RESET} --runtime-to-permanent", "description": "Guarda los cambios en tiempo de ejecución como permanentes"},
    {"command": f"{GREEN}firewall-cmd{RESET} --zone=zone --add-interface=eth0", "description": "Asocia la interfaz eth0 a una zona específica"},
    {"command": f"{GREEN}firewall-cmd{RESET} --zone=zone --remove-interface=eth0", "description": "Desasocia la interfaz eth0 de una zona específica"},
    {"command": f"{GREEN}firewall-cmd{RESET} --get-zones", "description": "Lista todas las zonas disponibles"},
    {"command": f"{GREEN}firewall-cmd{RESET} --new-zone=custom_zone --permanent", "description": "Crea una nueva zona de firewall personalizada"},
    {"command": f"{GREEN}firewall-cmd{RESET} --delete-zone=custom_zone --permanent", "description": "Elimina una zona personalizada de firewall"},
]

print(f"\nOpciones de FIREWALL-CMD con ejemplos y descripciones:\n")
print(f"{'Comando':<61} | {'Descripción'}")
print("-" * 136)
for cmd in firewall_cmd_commands:
    command = cmd["command"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<70} | {description}")

