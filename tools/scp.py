from shellcolorize import Color

scp_commands = [
    {"command": f"{Color.GREEN}scp{Color.RESET} <source> <destination>", "description": "Copia un archivo o directorio desde el origen al destino"},
    {"command": f"{Color.GREEN}scp{Color.RESET} -r <source> <destination>", "description": "Copia un directorio completo de forma recursiva"},
    {"command": f"{Color.GREEN}scp{Color.RESET} -p", "description": "Preserva las marcas de tiempo y permisos del archivo original"},
    {"command": f"{Color.GREEN}scp{Color.RESET} -P <port>", "description": "Especifica el puerto SSH a utilizar para la conexión"},
    {"command": f"{Color.GREEN}scp{Color.RESET} -i <identity_file>", "description": "Especifica un archivo de clave privada para la autenticación"},
    {"command": f"{Color.GREEN}scp{Color.RESET} -C", "description": "Habilita la compresión de datos durante la transferencia"},
    {"command": f"{Color.GREEN}scp{Color.RESET} -v", "description": "Muestra salida detallada de la transferencia (modo verbose)"},
    {"command": f"{Color.GREEN}scp{Color.RESET} -q", "description": "Silencia la salida de errores y progreso de transferencia"},
    {"command": f"{Color.GREEN}scp{Color.RESET} -l <limit>", "description": "Limita el ancho de banda a <limit> Kbit/s para la transferencia"},
    {"command": f"{Color.GREEN}scp{Color.RESET} -o <option>", "description": "Pasa opciones de configuración SSH adicionales (ej. -o StrictHostKeyChecking=no)"},
    {"command": f"{Color.GREEN}scp{Color.RESET} -3 <source> <destination>", "description": "Realiza la transferencia a través de la máquina local (útil para reenvíos)"},
    {"command": f"{Color.GREEN}scp{Color.RESET} -B", "description": "Desactiva la solicitud de contraseña, útil en scripts"},
    {"command": f"{Color.GREEN}scp{Color.RESET} --help", "description": "Muestra la ayuda de SCP con todas las opciones disponibles"},
]

print(f"\nComandos de SCP con ejemplos y descripciones:\n")
print(f"{'Comando':<36} | {'Descripción'}")
print("-" * 119)
for cmd in scp_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<45} | {description}")
