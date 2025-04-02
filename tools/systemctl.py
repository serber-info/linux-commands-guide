from shellcolorize import Color

systemctl_commands = [
    {"command": f"{Color.GREEN}systemctl{Color.RESET} start service", "description": "Inicia el servicio especificado"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} stop service", "description": "Detiene el servicio especificado"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} restart service", "description": "Reinicia el servicio especificado"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} reload service", "description": "Recarga la configuración del servicio sin detenerlo"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} enable service", "description": "Habilita el servicio para que se inicie automáticamente al arrancar el sistema"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} disable service", "description": "Deshabilita el inicio automático del servicio al arrancar el sistema"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} status service", "description": "Muestra el estado actual del servicio especificado"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} is-active service", "description": "Verifica si el servicio está activo"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} is-enabled service", "description": "Verifica si el servicio está habilitado para el inicio automático"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} list-units --type=service", "description": "Lista todos los servicios activos"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} list-unit-files --type=service", "description": "Lista todos los archivos de unidad de servicios"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} daemon-reload", "description": "Recarga el gestor de servicios systemd después de cambios en archivos de servicio"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} isolate multi-user.target", "description": "Cambia el sistema al modo multiusuario (sin GUI)"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} isolate graphical.target", "description": "Cambia el sistema al modo gráfico (con GUI)"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} mask service", "description": "Enmascara (bloquea) un servicio para evitar que sea iniciado"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} unmask service", "description": "Desenmascara un servicio previamente bloqueado"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} show service", "description": "Muestra los detalles de configuración del servicio especificado"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} cat service", "description": "Muestra el archivo de unidad del servicio"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} edit service", "description": "Edita el archivo de unidad del servicio"},
    {"command": f"{Color.GREEN}systemctl{Color.RESET} set-property service StartLimitBurst=10", "description": "Modifica propiedades de un servicio (ej. límite de inicio)"},
]

print(f"\nOpciones de SYSTEMCTL con ejemplos y descripciones:\n")
print(f"{'Comando':<56} | {'Descripción'}")
print("-" * 140)
for cmd in systemctl_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<65} | {description}")

