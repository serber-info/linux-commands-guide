
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

curl_commands = [
    {"command": f"{GREEN}curl {YELLOW}{RESET}https://example.com", "description": "Realiza una petición HTTP GET a una URL"},
    {"command": f"{GREEN}curl {YELLOW}-I {RESET}https://example.com", "description": "Realiza una petición HEAD para ver solo los encabezados"},
    {"command": f"{GREEN}curl {YELLOW}-o {RESET}file.txt https://example.com/file", "description": "Guarda el archivo descargado como 'file.txt'"},
    {"command": f"{GREEN}curl {YELLOW}-L {RESET}https://example.com", "description": "Sigue redirecciones HTTP"},
    {"command": f"{GREEN}curl {YELLOW}-u user:pass {RESET}https://example.com", "description": "Autenticación básica con usuario:contraseña"},
    {"command": f"{GREEN}curl {YELLOW}-d 'key=value' {RESET}https://example.com", "description": "Envía datos POST en el cuerpo de la solicitud"},
]

print(f"\nOpciones de CURL con ejemplos y descripciones:\n")
print(f"{'Comando':<46} | {'Descripción'}")
print("-" * 104)
for cmd in curl_commands:
    command = cmd["command"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<60} | {description}")

