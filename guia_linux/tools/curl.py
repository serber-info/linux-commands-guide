from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de CURL"
TITLE_EN = "CURL Options"
BRIEF = "Transfiere datos con URLs"
BRIEF_EN = "Transfer data with URLs"

COMMANDS = [
    {"command": f"{Color.GREEN}curl{Color.RESET} https://example.com", "description": "Realiza una petición HTTP GET", "description_en": "Perform an HTTP GET request"},
    {"command": f"{Color.GREEN}curl{Color.RESET} -I https://example.com", "description": "Muestra solo los encabezados de respuesta (HEAD)", "description_en": "Show only response headers (HEAD)"},
    {"command": f"{Color.GREEN}curl{Color.RESET} -o file.txt https://example.com/file", "description": "Guarda la respuesta en un archivo", "description_en": "Save response to a file"},
    {"command": f"{Color.GREEN}curl{Color.RESET} -O https://example.com/file.zip", "description": "Guarda con el nombre original del archivo", "description_en": "Save with the original filename"},
    {"command": f"{Color.GREEN}curl{Color.RESET} -L https://example.com", "description": "Sigue redirecciones HTTP", "description_en": "Follow HTTP redirects"},
    {"command": f"{Color.GREEN}curl{Color.RESET} -u user:pass https://example.com", "description": "Autenticación básica HTTP", "description_en": "HTTP basic authentication"},
    {"command": f"{Color.GREEN}curl{Color.RESET} -d 'key=value' https://example.com", "description": "Envía datos POST", "description_en": "Send POST data"},
    {"command": f"{Color.GREEN}curl{Color.RESET} -H 'Content-Type: application/json' URL", "description": "Añade una cabecera personalizada", "description_en": "Add a custom request header"},
    {"command": f"{Color.GREEN}curl{Color.RESET} -X PUT https://example.com", "description": "Usa el método HTTP especificado", "description_en": "Use the specified HTTP method"},
    {"command": f"{Color.GREEN}curl{Color.RESET} -s https://example.com", "description": "Modo silencioso — sin barra de progreso", "description_en": "Silent mode — no progress bar"},
    {"command": f"{Color.GREEN}curl{Color.RESET} -v https://example.com", "description": "Modo verbose — muestra detalles de la conexión", "description_en": "Verbose mode — show connection details"},
    {"command": f"{Color.GREEN}curl{Color.RESET} -k https://self-signed.example.com", "description": "Acepta certificados SSL no verificados", "description_en": "Accept unverified SSL certificates"},
    {"command": f"{Color.GREEN}curl{Color.RESET} --limit-rate 100K https://example.com", "description": "Limita la velocidad de transferencia", "description_en": "Limit transfer speed"},
    {"command": f"{Color.GREEN}curl{Color.RESET} -x proxy:8080 https://example.com", "description": "Usa un proxy HTTP", "description_en": "Use an HTTP proxy"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
