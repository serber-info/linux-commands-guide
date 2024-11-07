from shellcolorize import Color

lsof_commands = [
    {"command": f"{Color.GREEN}lsof{Color.RESET}", "description": "Muestra todos los archivos abiertos por todos los procesos"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} -u username", "description": "Muestra archivos abiertos por un usuario específico"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} -c process_name", "description": "Filtra por archivos abiertos por un proceso específico"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} -p PID", "description": "Muestra archivos abiertos por un proceso específico con el ID de proceso (PID) dado"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} -i", "description": "Muestra archivos abiertos de red (TCP/UDP)"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} -i :80", "description": "Muestra archivos abiertos relacionados con el puerto 80"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} -i TCP", "description": "Muestra solo conexiones TCP abiertas"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} -i UDP", "description": "Muestra solo conexiones UDP abiertas"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} -i @IP_ADDRESS", "description": "Muestra archivos abiertos relacionados con una dirección IP específica"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} +D /path/to/dir", "description": "Muestra archivos abiertos en un directorio específico"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} +d /path/to/dir", "description": "Muestra archivos abiertos en el directorio especificado, sin buscar en subdirectorios"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} -t", "description": "Muestra solo los PID de los procesos que tienen archivos abiertos"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} -n", "description": "No resuelve nombres de host, muestra direcciones IP en su lugar"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} -P", "description": "No convierte números de puerto a nombres de servicio"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} -l", "description": "Muestra nombres de usuario numéricos en lugar de nombres de usuario"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} -r N", "description": "Refresca el comando cada N segundos"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} -a -u username -c process_name", "description": "Combina múltiples opciones (AND lógico) para mostrar archivos abiertos por un usuario y proceso específicos"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} -s SIZE", "description": "Muestra archivos abiertos con un tamaño específico o superior"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} -T", "description": "Muestra información de tiempo en una conexión de red"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} -X", "description": "Muestra archivos abiertos específicos del sistema operativo (no en todos los sistemas)"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} -b", "description": "Ejecuta en modo 'buried' para evitar bloqueos en archivos abiertos por sistemas de archivos"},
    {"command": f"{Color.GREEN}lsof{Color.RESET} -V", "description": "Muestra la versión de lsof"},
]

print(f"\nComandos de LSOF con ejemplos y descripciones:\n")
print(f"{'Comando':<36} | {'Descripción'}")
print("-" * 125)
for cmd in lsof_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<45} | {description}")

