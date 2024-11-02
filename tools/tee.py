
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

tee_commands = [
    {"command": f"{GREEN}ls {RESET}| {GREEN}tee {RESET}output.txt", "description": "Guarda la salida en 'output.txt' y la muestra en pantalla"},
    {"command": f"{GREEN}ls {RESET}| {GREEN}tee {RESET}-a output.txt", "description": "Agrega la salida al final de 'output.txt'"},
    {"command": f"{GREEN}echo {YELLOW}'data' {RESET}| {GREEN}tee {RESET}/dev/tty output.txt", "description": "Envía la salida tanto a la consola como al archivo"},
]

print(f"\nOpciones de TEE con ejemplos y descripciones:\n")
print(f"{'Comando':<37} | {'Descripción'}")
print("-" * 97)
for cmd in tee_commands:
    command = cmd["command"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<55} | {description}")

