from shellcolorize import Color

iptables_commands = [
    {"command": f"{Color.GREEN}iptables{Color.RESET} -L", "description": "Lista todas las reglas en las cadenas"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -F", "description": "Limpia todas las reglas en las cadenas"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -A INPUT -s IP_ADDRESS -j ACCEPT", "description": "Permite tráfico de una IP específica en la cadena INPUT"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -A INPUT -p tcp --dport 80 -j ACCEPT", "description": "Permite tráfico HTTP entrante en el puerto 80"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -A INPUT -p tcp --dport 443 -j ACCEPT", "description": "Permite tráfico HTTPS entrante en el puerto 443"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -A OUTPUT -d IP_ADDRESS -j DROP", "description": "Bloquea el tráfico saliente hacia una IP específica"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -A FORWARD -p tcp --dport 22 -j DROP", "description": "Bloquea el reenvío de tráfico SSH en el puerto 22"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -A INPUT -p icmp --icmp-type 8 -j ACCEPT", "description": "Permite tráfico ICMP de tipo 8 (ping)"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT", "description": "Permite tráfico relacionado con conexiones existentes"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -P INPUT DROP", "description": "Establece la política por defecto de la cadena INPUT en DROP"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -P OUTPUT ACCEPT", "description": "Establece la política por defecto de la cadena OUTPUT en ACCEPT"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -D INPUT -s IP_ADDRESS -j ACCEPT", "description": "Elimina una regla específica en la cadena INPUT"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -I INPUT 1 -s IP_ADDRESS -j ACCEPT", "description": "Inserta una regla al inicio de la cadena INPUT para permitir una IP"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -R INPUT 1 -s IP_ADDRESS -j DROP", "description": "Reemplaza la regla 1 en la cadena INPUT para bloquear una IP"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -A INPUT -p tcp --dport 8080 -j ACCEPT", "description": "Permite tráfico HTTP alternativo en el puerto 8080"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -A INPUT -p udp --dport 53 -j ACCEPT", "description": "Permite tráfico DNS entrante en el puerto 53 (UDP)"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080", "description": "Redirecciona el tráfico del puerto 80 al puerto 8080"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -t nat -A POSTROUTING -o eth0 -j MASQUERADE", "description": "Habilita NAT para la interfaz de salida eth0"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -A INPUT -p tcp --dport 22 -m recent --set --name SSH --rsource", "description": "Establece un límite en el tráfico SSH"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -A INPUT -p tcp --dport 22 -m recent --update --seconds 60 --hitcount 4 --rttl --name SSH -j DROP", "description": "Limita el tráfico SSH a 3 intentos por minuto"},
]

print(f"\nOpciones de IPTABLES con ejemplos y descripciones:\n")
print(f"{'Comando':<106} | {'Descripción'}")
print("-" * 176)
for cmd in iptables_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<115} | {description}")
