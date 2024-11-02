
# Configuración de colores
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

fd_commands = [
    {"command": f"{GREEN}command{RESET} > file{RESET}", "description": "Redirige la salida estándar (stdout) a un archivo"},
    {"command": f"{GREEN}command{RESET} >> file{RESET}", "description": "Agrega la salida estándar al final de un archivo"},
    {"command": f"{GREEN}command{RESET} 2> file{RESET}", "description": "Redirige la salida de error (stderr) a un archivo"},
    {"command": f"{GREEN}command{RESET} 2>> file{RESET}", "description": "Agrega la salida de error al final de un archivo"},
    {"command": f"{GREEN}command{RESET} > file 2>&1{RESET}", "description": "Redirige stdout y stderr al mismo archivo"},
    {"command": f"{GREEN}command{RESET} &> file{RESET}", "description": "Redirige tanto stdout como stderr a un archivo (forma abreviada)"},
    {"command": f"{GREEN}command{RESET} < file{RESET}", "description": "Usa un archivo como entrada estándar (stdin)"},
    {"command": f"{GREEN}command{RESET} 0< file{RESET}", "description": "Otra forma de redirigir el archivo como entrada estándar"},
    {"command": f"{GREEN}command{RESET} 1> file{RESET}", "description": "Redirige explícitamente stdout a un archivo"},
    {"command": f"{GREEN}command{RESET} 2> /dev/null{RESET}", "description": "Descarta la salida de error (stderr)"},
    {"command": f"{GREEN}command{RESET} > /dev/null{RESET}", "description": "Descarta la salida estándar (stdout)"},
    {"command": f"{GREEN}command{RESET} > /dev/null 2>&1{RESET}", "description": "Descarta tanto stdout como stderr"},
    {"command": f"{GREEN}command{RESET} 3> file{RESET}", "description": "Redirige el descriptor de archivo 3 a un archivo"},
    {"command": f"{GREEN}command{RESET} 3>&- {RESET}", "description": "Cierra el descriptor de archivo 3"},
    {"command": f"{GREEN}command{RESET} 3<&- {RESET}", "description": "Cierra el descriptor de entrada de archivo 3"},
    {"command": f"{GREEN}exec{RESET} 3> file{RESET}", "description": "Abre un nuevo descriptor de archivo 3 para escritura en un archivo"},
    {"command": f"{GREEN}exec{RESET} 3< file{RESET}", "description": "Abre un nuevo descriptor de archivo 3 para lectura desde un archivo"},
    {"command": f"{GREEN}exec{RESET} 3>&1{RESET}", "description": "Redirige el descriptor de archivo 3 a stdout"},
    {"command": f"{GREEN}exec{RESET} 3>&-{RESET}", "description": "Cierra el descriptor de archivo 3"},
    {"command": f"{GREEN}command1 {RESET}| command2{RESET}", "description": "Conecta stdout de command1 a stdin de command2 (pipe)"},
    {"command": f"{GREEN}command {RESET}| tee file{RESET}", "description": "Escribe stdout en un archivo y lo muestra en pantalla"},
    {"command": f"{GREEN}command {RESET}| tee -a file{RESET}", "description": "Agrega stdout al archivo y lo muestra en pantalla"},
]

print(f"\nDescriptores de Archivos y Redirecciones con ejemplos y descripciones:\n")
print(f"{'Comando':<37} | {'Descripción'}")
print("-" * 107)
for cmd in fd_commands:
    command = cmd["command"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<50} | {description}")

