from shellcolorize import Color

fd_commands = [
    {"command": f"{Color.GREEN}command{Color.RESET} > file{Color.RESET}", "description": "Redirige la salida estándar (stdout) a un archivo"},
    {"command": f"{Color.GREEN}command{Color.RESET} >> file{Color.RESET}", "description": "Agrega la salida estándar al final de un archivo"},
    {"command": f"{Color.GREEN}command{Color.RESET} 2> file{Color.RESET}", "description": "Redirige la salida de error (stderr) a un archivo"},
    {"command": f"{Color.GREEN}command{Color.RESET} 2>> file{Color.RESET}", "description": "Agrega la salida de error al final de un archivo"},
    {"command": f"{Color.GREEN}command{Color.RESET} > file 2>&1{Color.RESET}", "description": "Redirige stdout y stderr al mismo archivo"},
    {"command": f"{Color.GREEN}command{Color.RESET} &> file{Color.RESET}", "description": "Redirige tanto stdout como stderr a un archivo (forma abreviada)"},
    {"command": f"{Color.GREEN}command{Color.RESET} < file{Color.RESET}", "description": "Usa un archivo como entrada estándar (stdin)"},
    {"command": f"{Color.GREEN}command{Color.RESET} 0< file{Color.RESET}", "description": "Otra forma de redirigir el archivo como entrada estándar"},
    {"command": f"{Color.GREEN}command{Color.RESET} 1> file{Color.RESET}", "description": "Redirige explícitamente stdout a un archivo"},
    {"command": f"{Color.GREEN}command{Color.RESET} 2> /dev/null{Color.RESET}", "description": "Descarta la salida de error (stderr)"},
    {"command": f"{Color.GREEN}command{Color.RESET} > /dev/null{Color.RESET}", "description": "Descarta la salida estándar (stdout)"},
    {"command": f"{Color.GREEN}command{Color.RESET} > /dev/null 2>&1{Color.RESET}", "description": "Descarta tanto stdout como stderr"},
    {"command": f"{Color.GREEN}command{Color.RESET} 3> file{Color.RESET}", "description": "Redirige el descriptor de archivo 3 a un archivo"},
    {"command": f"{Color.GREEN}command{Color.RESET} 3>&- {Color.RESET}", "description": "Cierra el descriptor de archivo 3"},
    {"command": f"{Color.GREEN}command{Color.RESET} 3<&- {Color.RESET}", "description": "Cierra el descriptor de entrada de archivo 3"},
    {"command": f"{Color.GREEN}exec{Color.RESET} 3> file{Color.RESET}", "description": "Abre un nuevo descriptor de archivo 3 para escritura en un archivo"},
    {"command": f"{Color.GREEN}exec{Color.RESET} 3< file{Color.RESET}", "description": "Abre un nuevo descriptor de archivo 3 para lectura desde un archivo"},
    {"command": f"{Color.GREEN}exec{Color.RESET} 3>&1{Color.RESET}", "description": "Redirige el descriptor de archivo 3 a stdout"},
    {"command": f"{Color.GREEN}exec{Color.RESET} 3>&-{Color.RESET}", "description": "Cierra el descriptor de archivo 3"},
    {"command": f"{Color.GREEN}command1 {Color.RESET}| command2{Color.RESET}", "description": "Conecta stdout de command1 a stdin de command2 (pipe)"},
    {"command": f"{Color.GREEN}command {Color.RESET}| tee file{Color.RESET}", "description": "Escribe stdout en un archivo y lo muestra en pantalla"},
    {"command": f"{Color.GREEN}command {Color.RESET}| tee -a file{Color.RESET}", "description": "Agrega stdout al archivo y lo muestra en pantalla"},
]

print(f"\nDescriptores de Archivos y Redirecciones con ejemplos y descripciones:\n")
print(f"{'Comando':<37} | {'Descripción'}")
print("-" * 107)
for cmd in fd_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<50} | {description}")

