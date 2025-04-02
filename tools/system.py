from shellcolorize import Color

system_commands = [
    # Navigation Commands
    {"category": f"{Color.RED}Comandos de Navegación de Directorios{Color.RESET}", "command": "", "description": ""},
    {"command": f"{Color.GREEN}cd{Color.RESET} <directory>", "description": f"{Color.RED}Cambia el directorio actual al especificado{Color.RESET}"},
    {"command": f"{Color.GREEN}pwd{Color.RESET}", "description": f"{Color.RED}Imprime el directorio de trabajo actual{Color.RESET}"},
    {"command": f"{Color.GREEN}pushd{Color.RESET} <directory>", "description": f"{Color.RED}Guarda el directorio actual en la pila y cambia al directorio especificado{Color.RESET}"},
    {"command": f"{Color.GREEN}popd{Color.RESET}", "description": f"{Color.RED}Elimina el directorio superior de la pila y cambia a ese directorio{Color.RESET}"},
    {"command": f"{Color.GREEN}dirs{Color.RESET}", "description": f"{Color.RED}Muestra la pila de directorios actual{Color.RESET}"},
    
    # File and Directory Management
    {"category": f"{Color.RED}Comandos de Gestión de Archivos y Directorios{Color.RESET}", "command": "", "description": ""},
    {"command": f"{Color.GREEN}touch{Color.RESET} <file>", "description": f"{Color.RED}Crea un archivo vacío o actualiza la fecha y hora de acceso/modificación de un archivo existente{Color.RESET}"},
    {"command": f"{Color.GREEN}mkdir{Color.RESET} <directory>", "description": f"{Color.RED}Crea un nuevo directorio{Color.RESET}"},
    {"command": f"{Color.GREEN}mkdir{Color.RESET} -p <path>", "description": f"{Color.RED}Crea un directorio y todos sus directorios padres necesarios{Color.RESET}"},
    {"command": f"{Color.GREEN}rm{Color.RESET} <file>", "description": f"{Color.RED}Elimina un archivo{Color.RESET}"},
    {"command": f"{Color.GREEN}rm{Color.RESET} -r <directory>", "description": f"{Color.RED}Elimina un directorio y su contenido de forma recursiva{Color.RESET}"},
    {"command": f"{Color.GREEN}cp{Color.RESET} <source> <destination>", "description": f"{Color.RED}Copia un archivo de origen a destino{Color.RESET}"},
    {"command": f"{Color.GREEN}cp{Color.RESET} -r <source_directory> <destination>", "description": f"{Color.RED}Copia un directorio completo de forma recursiva{Color.RESET}"},
    {"command": f"{Color.GREEN}mv{Color.RESET} <source> <destination>", "description": f"{Color.RED}Mueve o renombra un archivo o directorio{Color.RESET}"},
    {"command": f"{Color.GREEN}ln{Color.RESET} <target> <link>", "description": f"{Color.RED}Crea un enlace físico (hard link) al archivo de destino{Color.RESET}"},
    {"command": f"{Color.GREEN}ln{Color.RESET} -s <target> <link>", "description": f"{Color.RED}Crea un enlace simbólico (alias) al archivo o directorio de destino{Color.RESET}"},
    {"command": f"{Color.GREEN}find{Color.RESET} <path> -name <pattern>", "description": f"{Color.RED}Busca archivos o directorios en un camino específico según un patrón de nombre{Color.RESET}"},
    {"command": f"{Color.GREEN}locate{Color.RESET} <filename>", "description": f"{Color.RED}Busca archivos rápidamente mediante la base de datos de `locate`{Color.RESET}"},
    
    # File Viewing and Basic Editing
    {"category": f"{Color.RED}Comandos de Visualización de Archivos{Color.RESET}", "command": "", "description": ""},
    {"command": f"{Color.GREEN}cat{Color.RESET} <file>", "description": f"{Color.RED}Muestra el contenido de un archivo{Color.RESET}"},
    {"command": f"{Color.GREEN}less{Color.RESET} <file>", "description": f"{Color.RED}Muestra el contenido de un archivo de forma interactiva, permitiendo desplazarse{Color.RESET}"},
    {"command": f"{Color.GREEN}more{Color.RESET} <file>", "description": f"{Color.RED}Muestra el contenido de un archivo página por página{Color.RESET}"},
    {"command": f"{Color.GREEN}nl{Color.RESET} <file>", "description": f"{Color.RED}Muestra el contenido de un archivo, numerando las líneas{Color.RESET}"},
    
    # Touch and Modification Timestamps
    {"category": f"{Color.RED}Comandos de Tiempos de Modificación{Color.RESET}", "command": "", "description": ""},
    {"command": f"{Color.GREEN}touch{Color.RESET} <file>", "description": f"{Color.RED}Crea un archivo vacío o actualiza las marcas de tiempo de un archivo existente{Color.RESET}"},
    {"command": f"{Color.GREEN}stat{Color.RESET} <file>", "description": f"{Color.RED}Muestra detalles del archivo, incluidas las marcas de tiempo y permisos{Color.RESET}"},
    {"command": f"{Color.GREEN}date{Color.RESET}", "description": f"{Color.RED}Muestra la fecha y hora actuales del sistema{Color.RESET}"},
    {"command": f"{Color.GREEN}date{Color.RESET} -s <date_string>", "description": f"{Color.RED}Establece la fecha y hora del sistema a la especificada{Color.RESET}"},
    
    # Directory Listing and Information
    {"category": f"{Color.RED}Comandos de Información de Directorios{Color.RESET}", "command": "", "description": ""},
    {"command": f"{Color.GREEN}ls{Color.RESET}", "description": f"{Color.RED}Lista los contenidos del directorio actual{Color.RESET}"},
    {"command": f"{Color.GREEN}ls{Color.RESET} -a", "description": f"{Color.RED}Lista todos los archivos, incluyendo los ocultos{Color.RESET}"},
    {"command": f"{Color.GREEN}ls{Color.RESET} -l", "description": f"{Color.RED}Lista los archivos en formato largo, mostrando detalles adicionales{Color.RESET}"},
    {"command": f"{Color.GREEN}ls{Color.RESET} -lh", "description": f"{Color.RED}Lista los archivos en formato largo con tamaños legibles por humanos{Color.RESET}"},
    {"command": f"{Color.GREEN}ll{Color.RESET}", "description": f"{Color.RED}Lista los archivos en formato largo con tamaños legibles por humanos{Color.RESET}"},
    {"command": f"{Color.GREEN}tree{Color.RESET}", "description": f"{Color.RED}Muestra el contenido de directorios y subdirectorios en forma de árbol (si está instalado){Color.RESET}"},
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
