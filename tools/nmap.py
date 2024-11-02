
# Configuración de colores
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

nmap_commands = [
    {"command": f"{GREEN}nmap {YELLOW}{RESET}host", "description": "Realiza un escaneo básico de puertos en un host"},
    {"command": f"{GREEN}nmap {YELLOW}-sS {RESET}host", "description": "Realiza un escaneo SYN (común para detectar puertos abiertos)"},
    {"command": f"{GREEN}nmap {YELLOW}-sT {RESET}host", "description": "Realiza un escaneo TCP completo (menos sigiloso que SYN)"},
    {"command": f"{GREEN}nmap {YELLOW}-sU {RESET}host", "description": "Realiza un escaneo de puertos UDP"},
    {"command": f"{GREEN}nmap {YELLOW}-sV {RESET}host", "description": "Detecta versiones de servicios en los puertos abiertos"},
    {"command": f"{GREEN}nmap {YELLOW}-O {RESET}host", "description": "Detecta el sistema operativo del host"},
    {"command": f"{GREEN}nmap {YELLOW}-A {RESET}host", "description": "Realiza escaneo completo (servicios, SO, traceroute, scripts)"},
    {"command": f"{GREEN}nmap {YELLOW}-p 80,443 {RESET}host", "description": "Escanea puertos específicos (80 y 443)"},
    {"command": f"{GREEN}nmap {YELLOW}-p- {RESET}host", "description": "Escanea todos los puertos (1-65535)"},
    {"command": f"{GREEN}nmap {YELLOW}-T4 {RESET}host", "description": "Configura el nivel de agresividad (T4 para escaneo rápido)"},
    {"command": f"{GREEN}nmap {YELLOW}--open {RESET}host", "description": "Muestra solo puertos abiertos"},
    {"command": f"{GREEN}nmap {YELLOW}-Pn {RESET}host", "description": "Escanea el host sin hacer ping (útil si el ping está bloqueado)"},
    {"command": f"{GREEN}nmap {YELLOW}--script=http-title {RESET}host", "description": "Ejecuta un script específico (en este caso, obtiene títulos HTTP)"},
    {"command": f"{GREEN}nmap {YELLOW}-sC {RESET}host", "description": "Ejecuta scripts básicos de nmap para detectar vulnerabilidades"},
    {"command": f"{GREEN}nmap {YELLOW}-iL {RESET}targets.txt", "description": "Escanea una lista de objetivos desde el archivo 'targets.txt'"},
    {"command": f"{GREEN}nmap {YELLOW}-oN {RESET}scan.txt host", "description": "Guarda la salida del escaneo en formato normal en 'scan.txt'"},
    {"command": f"{GREEN}nmap {YELLOW}-oX {RESET}scan.xml host", "description": "Guarda la salida del escaneo en formato XML"},
    {"command": f"{GREEN}nmap {YELLOW}--traceroute {RESET}host", "description": "Realiza un traceroute al host escaneado"},
]

print(f"\nOpciones de NMAP con ejemplos y descripciones:\n")
print(f"{'Comando':<31} | {'Descripción'}")
print("-" * 99)
for cmd in nmap_commands:
    command = cmd["command"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<45} | {description}")

