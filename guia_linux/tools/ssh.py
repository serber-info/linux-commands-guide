from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de SSH"
TITLE_EN = "SSH Options"
BRIEF = "Cliente de shell seguro (Secure Shell)"
BRIEF_EN = "Secure Shell client"

COMMANDS = [
    {"command": f"{Color.GREEN}ssh{Color.RESET} user@host", "description": "Conecta al host como el usuario dado", "description_en": "Connect to host as the given user"},
    {"command": f"{Color.GREEN}ssh{Color.RESET} -p <port> user@host", "description": "Conecta usando el puerto especificado", "description_en": "Connect using the specified port"},
    {"command": f"{Color.GREEN}ssh{Color.RESET} -i key.pem user@host", "description": "Usa una clave privada para autenticación", "description_en": "Use a private key for authentication"},
    {"command": f"{Color.GREEN}ssh{Color.RESET} -L 8080:localhost:80 user@host", "description": "Túnel local: redirige el puerto local 8080 al 80 del host", "description_en": "Local tunnel: forward local port 8080 to host port 80"},
    {"command": f"{Color.GREEN}ssh{Color.RESET} -R 9090:localhost:8080 user@host", "description": "Túnel remoto: redirige el puerto 9090 del host al local 8080", "description_en": "Remote tunnel: forward host port 9090 to local port 8080"},
    {"command": f"{Color.GREEN}ssh{Color.RESET} -D 1080 user@host", "description": "Crea un proxy SOCKS dinámico en el puerto 1080", "description_en": "Create a dynamic SOCKS proxy on port 1080"},
    {"command": f"{Color.GREEN}ssh{Color.RESET} -N user@host", "description": "No ejecuta comandos — solo túneles", "description_en": "Do not execute commands — tunnels only"},
    {"command": f"{Color.GREEN}ssh{Color.RESET} -X user@host", "description": "Habilita el reenvío de X11 (GUI remota)", "description_en": "Enable X11 forwarding (remote GUI)"},
    {"command": f"{Color.GREEN}ssh{Color.RESET} -A user@host", "description": "Habilita el reenvío del agente SSH", "description_en": "Enable SSH agent forwarding"},
    {"command": f"{Color.GREEN}ssh{Color.RESET} -v user@host", "description": "Modo verbose — útil para depurar conexiones", "description_en": "Verbose mode — useful for debugging"},
    {"command": f"{Color.GREEN}ssh{Color.RESET} -o StrictHostKeyChecking=no user@host", "description": "Desactiva la verificación de clave del host", "description_en": "Disable host key checking"},
    {"command": f"{Color.GREEN}ssh{Color.RESET} user@host 'command'", "description": "Ejecuta un comando remoto sin shell interactiva", "description_en": "Run a remote command without interactive shell"},
    {"command": f"{Color.GREEN}ssh-keygen{Color.RESET} -t ed25519", "description": "Genera un par de claves SSH (algoritmo moderno)", "description_en": "Generate an SSH key pair (modern algorithm)"},
    {"command": f"{Color.GREEN}ssh-copy-id{Color.RESET} user@host", "description": "Copia la clave pública al host remoto", "description_en": "Copy the public key to the remote host"},
    {"command": f"{Color.GREEN}ssh-add{Color.RESET} key.pem", "description": "Añade una clave privada al agente SSH", "description_en": "Add a private key to the SSH agent"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
