from shellcolorize import Color

nmap_commands = [
    {"command": f"{Color.GREEN}nmap {Color.YELLOW}{Color.RESET}host", "description": "Realiza un escaneo básico de puertos en un host"},
    {"command": f"{Color.GREEN}nmap {Color.YELLOW}-sS {Color.RESET}host", "description": "Realiza un escaneo SYN (común para detectar puertos abiertos)"},
    {"command": f"{Color.GREEN}nmap {Color.YELLOW}-sT {Color.RESET}host", "description": "Realiza un escaneo TCP completo (menos sigiloso que SYN)"},
    {"command": f"{Color.GREEN}nmap {Color.YELLOW}-sU {Color.RESET}host", "description": "Realiza un escaneo de puertos UDP"},
    {"command": f"{Color.GREEN}nmap {Color.YELLOW}-sV {Color.RESET}host", "description": "Detecta versiones de servicios en los puertos abiertos"},
    {"command": f"{Color.GREEN}nmap {Color.YELLOW}-O {Color.RESET}host", "description": "Detecta el sistema operativo del host"},
    {"command": f"{Color.GREEN}nmap {Color.YELLOW}-A {Color.RESET}host", "description": "Realiza escaneo completo (servicios, SO, traceroute, scripts)"},
    {"command": f"{Color.GREEN}nmap {Color.YELLOW}-p 80,443 {Color.RESET}host", "description": "Escanea puertos específicos (80 y 443)"},
    {"command": f"{Color.GREEN}nmap {Color.YELLOW}-p- {Color.RESET}host", "description": "Escanea todos los puertos (1-65535)"},
    {"command": f"{Color.GREEN}nmap {Color.YELLOW}-T4 {Color.RESET}host", "description": "Configura el nivel de agresividad (T4 para escaneo rápido)"},
    {"command": f"{Color.GREEN}nmap {Color.YELLOW}--open {Color.RESET}host", "description": "Muestra solo puertos abiertos"},
    {"command": f"{Color.GREEN}nmap {Color.YELLOW}-Pn {Color.RESET}host", "description": "Escanea el host sin hacer ping (útil si el ping está bloqueado)"},
    {"command": f"{Color.GREEN}nmap {Color.YELLOW}--script=http-title {Color.RESET}host", "description": "Ejecuta un script específico (en este caso, obtiene títulos HTTP)"},
    {"command": f"{Color.GREEN}nmap {Color.YELLOW}-sC {Color.RESET}host", "description": "Ejecuta scripts básicos de nmap para detectar vulnerabilidades"},
    {"command": f"{Color.GREEN}nmap {Color.YELLOW}-iL {Color.RESET}targets.txt", "description": "Escanea una lista de objetivos desde el archivo 'targets.txt'"},
    {"command": f"{Color.GREEN}nmap {Color.YELLOW}-oN {Color.RESET}scan.txt host", "description": "Guarda la salida del escaneo en formato normal en 'scan.txt'"},
    {"command": f"{Color.GREEN}nmap {Color.YELLOW}-oX {Color.RESET}scan.xml host", "description": "Guarda la salida del escaneo en formato XML"},
    {"command": f"{Color.GREEN}nmap {Color.YELLOW}--traceroute {Color.RESET}host", "description": "Realiza un traceroute al host escaneado"},
]

print(f"\nOpciones de NMAP con ejemplos y descripciones:\n")
print(f"{'Comando':<31} | {'Descripción'}")
print("-" * 99)
for cmd in nmap_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<45} | {description}")

