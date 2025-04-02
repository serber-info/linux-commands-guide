from shellcolorize import Color

tee_commands = [
    {"command": f"{Color.GREEN}ls {Color.RESET}| {Color.GREEN}tee {Color.RESET}output.txt", "description": "Guarda la salida en 'output.txt' y la muestra en pantalla"},
    {"command": f"{Color.GREEN}ls {Color.RESET}| {Color.GREEN}tee {Color.RESET}-a output.txt", "description": "Agrega la salida al final de 'output.txt'"},
    {"command": f"{Color.GREEN}echo {Color.YELLOW}'data' {Color.RESET}| {Color.GREEN}tee {Color.RESET}/dev/tty output.txt", "description": "Envía la salida tanto a la consola como al archivo"},
]

print(f"\nOpciones de TEE con ejemplos y descripciones:\n")
print(f"{'Comando':<37} | {'Descripción'}")
print("-" * 97)
for cmd in tee_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<55} | {description}")

