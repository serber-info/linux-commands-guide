# Configuración de colores
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

netstat_commands = [
    {"command": f"{GREEN}netstat{RESET}", "description": "Muestra todas las conexiones de red activas"},
    {"command": f"{GREEN}netstat{RESET} -a", "description": "Muestra todas las conexiones y puertos en escucha"},
    {"command": f"{GREEN}netstat{RESET} -t", "description": "Muestra solo conexiones TCP"},
    {"command": f"{GREEN}netstat{RESET} -u", "description": "Muestra solo conexiones UDP"},
    {"command": f"{GREEN}netstat{RESET} -l", "description": "Muestra solo puertos en escucha"},
    {"command": f"{GREEN}netstat{RESET} -p", "description": "Muestra el proceso (PID y nombre) que utiliza cada conexión"},
    {"command": f"{GREEN}netstat{RESET} -n", "description": "Muestra direcciones IP y números de puerto en formato numérico"},
    {"command": f"{GREEN}netstat{RESET} -r", "description": "Muestra la tabla de enrutamiento del sistema"},
    {"command": f"{GREEN}netstat{RESET} -i", "description": "Muestra estadísticas de interfaz de red"},
    {"command": f"{GREEN}netstat{RESET} -c", "description": "Actualiza la información de red en intervalos continuos"},
    {"command": f"{GREEN}netstat{RESET} -s", "description": "Muestra estadísticas de red detalladas por protocolo"},
    {"command": f"{GREEN}netstat{RESET} -M", "description": "Muestra conexiones de enmascaramiento (masquerading)"},
    {"command": f"{GREEN}netstat{RESET} -g", "description": "Muestra la tabla de membresía multicast"},
    {"command": f"{GREEN}netstat{RESET} -w", "description": "Muestra las estadísticas de RAW de la red"},
    {"command": f"{GREEN}netstat{RESET} --ip", "description": "Filtra y muestra solo conexiones IPv4"},
    {"command": f"{GREEN}netstat{RESET} --tcp", "description": "Alias para -t; muestra solo conexiones TCP"},
    {"command": f"{GREEN}netstat{RESET} --udp", "description": "Alias para -u; muestra solo conexiones UDP"},
    {"command": f"{GREEN}netstat{RESET} --listening", "description": "Alias para -l; muestra solo puertos en escucha"},
    {"command": f"{GREEN}netstat{RESET} --numeric", "description": "Alias para -n; muestra direcciones en formato numérico"},
    {"command": f"{GREEN}netstat{RESET} --program", "description": "Alias para -p; muestra el proceso asociado a cada conexión"},
    {"command": f"{GREEN}netstat{RESET} --route", "description": "Alias para -r; muestra la tabla de enrutamiento"},
    {"command": f"{GREEN}netstat{RESET} --interfaces", "description": "Alias para -i; muestra estadísticas de interfaz de red"},
    {"command": f"{GREEN}netstat{RESET} --continuous", "description": "Alias para -c; actualiza en intervalos continuos"},
    {"command": f"{GREEN}netstat{RESET} --statistics", "description": "Alias para -s; muestra estadísticas detalladas por protocolo"},
    {"command": f"{GREEN}netstat{RESET} --masquerade", "description": "Alias para -M; muestra conexiones de enmascaramiento"},
    {"command": f"{GREEN}netstat{RESET} --help", "description": "Muestra la ayuda del comando netstat con todas las opciones disponibles"},
]

print(f"\nComandos de NETSTAT con ejemplos y descripciones:\n")
print(f"{'Comando':<26} | {'Descripción'}")
print("-" * 100)
for cmd in netstat_commands:
    command = cmd["command"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<35} | {description}")
