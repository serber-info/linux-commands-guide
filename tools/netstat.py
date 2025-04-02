from shellcolorize import Color

netstat_commands = [
    {"command": f"{Color.GREEN}netstat{Color.RESET}", "description": "Muestra todas las conexiones de red activas"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} -a", "description": "Muestra todas las conexiones y puertos en escucha"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} -t", "description": "Muestra solo conexiones TCP"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} -u", "description": "Muestra solo conexiones UDP"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} -l", "description": "Muestra solo puertos en escucha"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} -p", "description": "Muestra el proceso (PID y nombre) que utiliza cada conexión"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} -n", "description": "Muestra direcciones IP y números de puerto en formato numérico"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} -r", "description": "Muestra la tabla de enrutamiento del sistema"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} -i", "description": "Muestra estadísticas de interfaz de red"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} -c", "description": "Actualiza la información de red en intervalos continuos"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} -s", "description": "Muestra estadísticas de red detalladas por protocolo"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} -M", "description": "Muestra conexiones de enmascaramiento (masquerading)"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} -g", "description": "Muestra la tabla de membresía multicast"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} -w", "description": "Muestra las estadísticas de RAW de la red"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} --ip", "description": "Filtra y muestra solo conexiones IPv4"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} --tcp", "description": "Alias para -t; muestra solo conexiones TCP"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} --udp", "description": "Alias para -u; muestra solo conexiones UDP"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} --listening", "description": "Alias para -l; muestra solo puertos en escucha"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} --numeric", "description": "Alias para -n; muestra direcciones en formato numérico"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} --program", "description": "Alias para -p; muestra el proceso asociado a cada conexión"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} --route", "description": "Alias para -r; muestra la tabla de enrutamiento"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} --interfaces", "description": "Alias para -i; muestra estadísticas de interfaz de red"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} --continuous", "description": "Alias para -c; actualiza en intervalos continuos"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} --statistics", "description": "Alias para -s; muestra estadísticas detalladas por protocolo"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} --masquerade", "description": "Alias para -M; muestra conexiones de enmascaramiento"},
    {"command": f"{Color.GREEN}netstat{Color.RESET} --help", "description": "Muestra la ayuda del comando netstat con todas las opciones disponibles"},
]

print(f"\nComandos de NETSTAT con ejemplos y descripciones:\n")
print(f"{'Comando':<26} | {'Descripción'}")
print("-" * 100)
for cmd in netstat_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<35} | {description}")
