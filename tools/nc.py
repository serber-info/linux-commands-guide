from shellcolorize import Color

netcat_commands = [
    {"command": f"{Color.GREEN}nc{Color.RESET} -l -p <port>", "description": "Inicia Netcat en modo servidor, escuchando en el puerto especificado"},
    {"command": f"{Color.GREEN}nc{Color.RESET} -l <port>", "description": "Escucha en el puerto especificado (modo servidor, sin espera de cierre)"},
    {"command": f"{Color.GREEN}nc{Color.RESET} -lp <port>", "description": "Escucha en el puerto especificado y permanece abierto (alias de -l -p)"},
    {"command": f"{Color.GREEN}nc{Color.RESET} <host> <port>", "description": "Establece una conexión al host y puerto especificados (modo cliente)"},
    {"command": f"{Color.GREEN}nc{Color.RESET} -z <host> <port>", "description": "Escanea puertos en el host especificado sin enviar datos"},
    {"command": f"{Color.GREEN}nc{Color.RESET} -v", "description": "Muestra salida detallada (modo verbose)"},
    {"command": f"{Color.GREEN}nc{Color.RESET} -vv", "description": "Muestra salida aún más detallada (modo muy verbose)"},
    {"command": f"{Color.GREEN}nc{Color.RESET} -u", "description": "Usa el protocolo UDP en lugar de TCP"},
    {"command": f"{Color.GREEN}nc{Color.RESET} -n", "description": "Omite la resolución de DNS (usa solo direcciones IP numéricas)"},
    {"command": f"{Color.GREEN}nc{Color.RESET} -k", "description": "Mantiene la conexión abierta después de que el cliente se desconecte (modo persistente)"},
    {"command": f"{Color.GREEN}nc{Color.RESET} -w <timeout>", "description": "Especifica el tiempo de espera en segundos para conexiones y lectura/escritura"},
    {"command": f"{Color.GREEN}nc{Color.RESET} -i <interval>", "description": "Introduce un intervalo de segundos entre envíos y reconexiones"},
    {"command": f"{Color.GREEN}nc{Color.RESET} -c <command>", "description": "Ejecuta un comando al recibir una conexión (solo en algunas versiones de netcat)"},
    {"command": f"{Color.GREEN}nc{Color.RESET} -e <command>", "description": "Ejecuta un comando en el lado servidor después de la conexión (en versiones que soportan -e)"},
    {"command": f"{Color.GREEN}nc{Color.RESET} -q <seconds>", "description": "Espera el número de segundos especificado tras EOF antes de cerrar"},
    {"command": f"{Color.GREEN}nc{Color.RESET} -o <file>", "description": "Guarda la comunicación en un archivo de registro (útil para análisis)"},
    {"command": f"{Color.GREEN}nc{Color.RESET} -r", "description": "Usa puertos aleatorios para la conexión en lugar de una secuencia fija"},
    {"command": f"{Color.GREEN}nc{Color.RESET} -x <proxy>", "description": "Usa un servidor proxy SOCKS para la conexión"},
    {"command": f"{Color.GREEN}nc{Color.RESET} --help", "description": "Muestra la ayuda de Netcat con todas las opciones disponibles"},
]

print(f"\nComandos de NETCAT (NC) con ejemplos y descripciones:\n")
print(f"{'Comando':<26} | {'Descripción'}")
print("-" * 121)
for cmd in netcat_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<35} | {description}")
