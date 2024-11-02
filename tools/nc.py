# Configuración de colores
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

netcat_commands = [
    {"command": f"{GREEN}nc{RESET} -l -p <port>", "description": "Inicia Netcat en modo servidor, escuchando en el puerto especificado"},
    {"command": f"{GREEN}nc{RESET} -l <port>", "description": "Escucha en el puerto especificado (modo servidor, sin espera de cierre)"},
    {"command": f"{GREEN}nc{RESET} -lp <port>", "description": "Escucha en el puerto especificado y permanece abierto (alias de -l -p)"},
    {"command": f"{GREEN}nc{RESET} <host> <port>", "description": "Establece una conexión al host y puerto especificados (modo cliente)"},
    {"command": f"{GREEN}nc{RESET} -z <host> <port>", "description": "Escanea puertos en el host especificado sin enviar datos"},
    {"command": f"{GREEN}nc{RESET} -v", "description": "Muestra salida detallada (modo verbose)"},
    {"command": f"{GREEN}nc{RESET} -vv", "description": "Muestra salida aún más detallada (modo muy verbose)"},
    {"command": f"{GREEN}nc{RESET} -u", "description": "Usa el protocolo UDP en lugar de TCP"},
    {"command": f"{GREEN}nc{RESET} -n", "description": "Omite la resolución de DNS (usa solo direcciones IP numéricas)"},
    {"command": f"{GREEN}nc{RESET} -k", "description": "Mantiene la conexión abierta después de que el cliente se desconecte (modo persistente)"},
    {"command": f"{GREEN}nc{RESET} -w <timeout>", "description": "Especifica el tiempo de espera en segundos para conexiones y lectura/escritura"},
    {"command": f"{GREEN}nc{RESET} -i <interval>", "description": "Introduce un intervalo de segundos entre envíos y reconexiones"},
    {"command": f"{GREEN}nc{RESET} -c <command>", "description": "Ejecuta un comando al recibir una conexión (solo en algunas versiones de netcat)"},
    {"command": f"{GREEN}nc{RESET} -e <command>", "description": "Ejecuta un comando en el lado servidor después de la conexión (en versiones que soportan -e)"},
    {"command": f"{GREEN}nc{RESET} -q <seconds>", "description": "Espera el número de segundos especificado tras EOF antes de cerrar"},
    {"command": f"{GREEN}nc{RESET} -o <file>", "description": "Guarda la comunicación en un archivo de registro (útil para análisis)"},
    {"command": f"{GREEN}nc{RESET} -r", "description": "Usa puertos aleatorios para la conexión en lugar de una secuencia fija"},
    {"command": f"{GREEN}nc{RESET} -x <proxy>", "description": "Usa un servidor proxy SOCKS para la conexión"},
    {"command": f"{GREEN}nc{RESET} --help", "description": "Muestra la ayuda de Netcat con todas las opciones disponibles"},
]

print(f"\nComandos de NETCAT (NC) con ejemplos y descripciones:\n")
print(f"{'Comando':<26} | {'Descripción'}")
print("-" * 121)
for cmd in netcat_commands:
    command = cmd["command"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<35} | {description}")
