# Configuración de colores
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

system_commands = [
    # Navigation Commands
    {"category": f"{RED}Comandos de Navegación de Directorios{RESET}", "command": "", "description": ""},
    {"command": f"{GREEN}cd{RESET} <directory>", "description": f"{RED}Cambia el directorio actual al especificado{RESET}"},
    {"command": f"{GREEN}pwd{RESET}", "description": f"{RED}Imprime el directorio de trabajo actual{RESET}"},
    {"command": f"{GREEN}pushd{RESET} <directory>", "description": f"{RED}Guarda el directorio actual en la pila y cambia al directorio especificado{RESET}"},
    {"command": f"{GREEN}popd{RESET}", "description": f"{RED}Elimina el directorio superior de la pila y cambia a ese directorio{RESET}"},
    {"command": f"{GREEN}dirs{RESET}", "description": f"{RED}Muestra la pila de directorios actual{RESET}"},
    
    # File and Directory Management
    {"category": f"{RED}Comandos de Gestión de Archivos y Directorios{RESET}", "command": "", "description": ""},
    {"command": f"{GREEN}touch{RESET} <file>", "description": f"{RED}Crea un archivo vacío o actualiza la fecha y hora de acceso/modificación de un archivo existente{RESET}"},
    {"command": f"{GREEN}mkdir{RESET} <directory>", "description": f"{RED}Crea un nuevo directorio{RESET}"},
    {"command": f"{GREEN}mkdir{RESET} -p <path>", "description": f"{RED}Crea un directorio y todos sus directorios padres necesarios{RESET}"},
    {"command": f"{GREEN}rm{RESET} <file>", "description": f"{RED}Elimina un archivo{RESET}"},
    {"command": f"{GREEN}rm{RESET} -r <directory>", "description": f"{RED}Elimina un directorio y su contenido de forma recursiva{RESET}"},
    {"command": f"{GREEN}cp{RESET} <source> <destination>", "description": f"{RED}Copia un archivo de origen a destino{RESET}"},
    {"command": f"{GREEN}cp{RESET} -r <source_directory> <destination>", "description": f"{RED}Copia un directorio completo de forma recursiva{RESET}"},
    {"command": f"{GREEN}mv{RESET} <source> <destination>", "description": f"{RED}Mueve o renombra un archivo o directorio{RESET}"},
    {"command": f"{GREEN}ln{RESET} <target> <link>", "description": f"{RED}Crea un enlace físico (hard link) al archivo de destino{RESET}"},
    {"command": f"{GREEN}ln{RESET} -s <target> <link>", "description": f"{RED}Crea un enlace simbólico (alias) al archivo o directorio de destino{RESET}"},
    {"command": f"{GREEN}find{RESET} <path> -name <pattern>", "description": f"{RED}Busca archivos o directorios en un camino específico según un patrón de nombre{RESET}"},
    {"command": f"{GREEN}locate{RESET} <filename>", "description": f"{RED}Busca archivos rápidamente mediante la base de datos de `locate`{RESET}"},
    
    # File Viewing and Basic Editing
    {"category": f"{RED}Comandos de Visualización de Archivos{RESET}", "command": "", "description": ""},
    {"command": f"{GREEN}cat{RESET} <file>", "description": f"{RED}Muestra el contenido de un archivo{RESET}"},
    {"command": f"{GREEN}less{RESET} <file>", "description": f"{RED}Muestra el contenido de un archivo de forma interactiva, permitiendo desplazarse{RESET}"},
    {"command": f"{GREEN}more{RESET} <file>", "description": f"{RED}Muestra el contenido de un archivo página por página{RESET}"},
    {"command": f"{GREEN}nl{RESET} <file>", "description": f"{RED}Muestra el contenido de un archivo, numerando las líneas{RESET}"},
    
    # Touch and Modification Timestamps
    {"category": f"{RED}Comandos de Tiempos de Modificación{RESET}", "command": "", "description": ""},
    {"command": f"{GREEN}touch{RESET} <file>", "description": f"{RED}Crea un archivo vacío o actualiza las marcas de tiempo de un archivo existente{RESET}"},
    {"command": f"{GREEN}stat{RESET} <file>", "description": f"{RED}Muestra detalles del archivo, incluidas las marcas de tiempo y permisos{RESET}"},
    {"command": f"{GREEN}date{RESET}", "description": f"{RED}Muestra la fecha y hora actuales del sistema{RESET}"},
    {"command": f"{GREEN}date{RESET} -s <date_string>", "description": f"{RED}Establece la fecha y hora del sistema a la especificada{RESET}"},
    
    # Directory Listing and Information
    {"category": f"{RED}Comandos de Información de Directorios{RESET}", "command": "", "description": ""},
    {"command": f"{GREEN}ls{RESET}", "description": f"{RED}Lista los contenidos del directorio actual{RESET}"},
    {"command": f"{GREEN}ls{RESET} -a", "description": f"{RED}Lista todos los archivos, incluyendo los ocultos{RESET}"},
    {"command": f"{GREEN}ls{RESET} -l", "description": f"{RED}Lista los archivos en formato largo, mostrando detalles adicionales{RESET}"},
    {"command": f"{GREEN}ls{RESET} -lh", "description": f"{RED}Lista los archivos en formato largo con tamaños legibles por humanos{RESET}"},
    {"command": f"{GREEN}ll{RESET}", "description": f"{RED}Lista los archivos en formato largo con tamaños legibles por humanos{RESET}"},
    {"command": f"{GREEN}tree{RESET}", "description": f"{RED}Muestra el contenido de directorios y subdirectorios en forma de árbol (si está instalado){RESET}"},
]

# Display formatted table
print(f"\nComandos del Sistema de Archivos en Linux con ejemplos y descripciones:\n")
print(f"{'Comando':<41} | {'Descripción'}")
print("-" * 140)
for cmd in system_commands:
    if "category" in cmd:
        print(f"\n{cmd['category']}\n" + "-" * 140)
    else:
        command = cmd["command"]
        description = cmd["description"]
        print(f"{command:<50} | {description}")
