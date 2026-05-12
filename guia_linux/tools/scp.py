from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de SCP"
TITLE_EN = "SCP Options"
BRIEF = "Copia segura de archivos via SSH"
BRIEF_EN = "Secure file copy over SSH"

COMMANDS = [
    {"command": f"{Color.GREEN}scp{Color.RESET} file user@host:/path", "description": "Copia un archivo al servidor remoto", "description_en": "Copy a file to the remote server"},
    {"command": f"{Color.GREEN}scp{Color.RESET} user@host:/path/file .", "description": "Descarga un archivo del servidor remoto", "description_en": "Download a file from the remote server"},
    {"command": f"{Color.GREEN}scp{Color.RESET} -r dir user@host:/path", "description": "Copia un directorio completo de forma recursiva", "description_en": "Copy a directory recursively"},
    {"command": f"{Color.GREEN}scp{Color.RESET} -p file user@host:/path", "description": "Preserva permisos y marcas de tiempo", "description_en": "Preserve permissions and timestamps"},
    {"command": f"{Color.GREEN}scp{Color.RESET} -P <port> file user@host:/path", "description": "Usa el puerto SSH especificado", "description_en": "Use the specified SSH port"},
    {"command": f"{Color.GREEN}scp{Color.RESET} -i key.pem file user@host:/path", "description": "Usa una clave privada para la autenticación", "description_en": "Use a private key for authentication"},
    {"command": f"{Color.GREEN}scp{Color.RESET} -C file user@host:/path", "description": "Habilita la compresión de datos", "description_en": "Enable data compression"},
    {"command": f"{Color.GREEN}scp{Color.RESET} -v file user@host:/path", "description": "Modo verbose — salida detallada", "description_en": "Verbose mode — detailed output"},
    {"command": f"{Color.GREEN}scp{Color.RESET} -q file user@host:/path", "description": "Silencia errores y progreso", "description_en": "Quiet mode — suppress errors and progress"},
    {"command": f"{Color.GREEN}scp{Color.RESET} -l <limit> file user@host:/path", "description": "Limita el ancho de banda en Kbit/s", "description_en": "Limit bandwidth in Kbit/s"},
    {"command": f"{Color.GREEN}scp{Color.RESET} -o StrictHostKeyChecking=no file user@host:/path", "description": "Desactiva la verificación del host", "description_en": "Disable host key checking"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
