from shellcolorize import Color

curl_commands = [
    {"command": f"{Color.GREEN}curl {Color.YELLOW}{Color.RESET}https://example.com", "description": "Realiza una petición HTTP GET a una URL"},
    {"command": f"{Color.GREEN}curl {Color.YELLOW}-I {Color.RESET}https://example.com", "description": "Realiza una petición HEAD para ver solo los encabezados"},
    {"command": f"{Color.GREEN}curl {Color.YELLOW}-o {Color.RESET}file.txt https://example.com/file", "description": "Guarda el archivo descargado como 'file.txt'"},
    {"command": f"{Color.GREEN}curl {Color.YELLOW}-L {Color.RESET}https://example.com", "description": "Sigue redirecciones HTTP"},
    {"command": f"{Color.GREEN}curl {Color.YELLOW}-u user:pass {Color.RESET}https://example.com", "description": "Autenticación básica con usuario:contraseña"},
    {"command": f"{Color.GREEN}curl {Color.YELLOW}-d 'key=value' {Color.RESET}https://example.com", "description": "Envía datos POST en el cuerpo de la solicitud"},
]

print(f"\nOpciones de CURL con ejemplos y descripciones:\n")
print(f"{'Comando':<46} | {'Descripción'}")
print("-" * 104)
for cmd in curl_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<60} | {description}")

