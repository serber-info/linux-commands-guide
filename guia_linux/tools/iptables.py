from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de IPTABLES"
TITLE_EN = "IPTABLES Options"
BRIEF = "Gestión de reglas de firewall del kernel"
BRIEF_EN = "Kernel firewall rule management"

COMMANDS = [
    {"command": f"{Color.GREEN}iptables{Color.RESET} -L", "description": "Lista todas las reglas de las cadenas", "description_en": "List all rules in all chains"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -F", "description": "Limpia todas las reglas de las cadenas", "description_en": "Flush all rules from all chains"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -A INPUT -s IP -j ACCEPT", "description": "Permite tráfico de una IP en INPUT", "description_en": "Allow traffic from an IP in INPUT"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -A INPUT -p tcp --dport 80 -j ACCEPT", "description": "Permite tráfico HTTP entrante (puerto 80)", "description_en": "Allow incoming HTTP traffic (port 80)"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -A INPUT -p tcp --dport 443 -j ACCEPT", "description": "Permite tráfico HTTPS entrante (puerto 443)", "description_en": "Allow incoming HTTPS traffic (port 443)"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -A OUTPUT -d IP -j DROP", "description": "Bloquea el tráfico saliente hacia una IP", "description_en": "Block outgoing traffic to an IP"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -A INPUT -p icmp --icmp-type 8 -j ACCEPT", "description": "Permite ping (ICMP tipo 8)", "description_en": "Allow ping (ICMP type 8)"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT", "description": "Permite tráfico de conexiones existentes", "description_en": "Allow traffic from established connections"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -P INPUT DROP", "description": "Política por defecto DROP en INPUT", "description_en": "Set default DROP policy for INPUT"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -P OUTPUT ACCEPT", "description": "Política por defecto ACCEPT en OUTPUT", "description_en": "Set default ACCEPT policy for OUTPUT"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -D INPUT -s IP -j ACCEPT", "description": "Elimina una regla específica de INPUT", "description_en": "Delete a specific rule from INPUT"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -I INPUT 1 -s IP -j ACCEPT", "description": "Inserta una regla al inicio de INPUT", "description_en": "Insert a rule at the top of INPUT"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -A INPUT -p udp --dport 53 -j ACCEPT", "description": "Permite DNS entrante (UDP 53)", "description_en": "Allow incoming DNS (UDP port 53)"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -t nat -A POSTROUTING -o eth0 -j MASQUERADE", "description": "Habilita NAT en la interfaz de salida", "description_en": "Enable NAT on the outgoing interface"},
    {"command": f"{Color.GREEN}iptables{Color.RESET} -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080", "description": "Redirige el puerto 80 al 8080", "description_en": "Redirect port 80 to 8080"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
