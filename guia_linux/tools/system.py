from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Comandos básicos del sistema"
TITLE_EN = "Basic System Commands"
BRIEF = "Navegación, archivos y gestión del sistema"
BRIEF_EN = "Navigation, files and system management"

COMMANDS = [
    {"section": "Navegación de directorios", "section_en": "Directory Navigation"},
    {"command": f"{Color.GREEN}cd{Color.RESET} <directory>", "description": "Cambia al directorio especificado", "description_en": "Change to the specified directory"},
    {"command": f"{Color.GREEN}pwd{Color.RESET}", "description": "Imprime el directorio de trabajo actual", "description_en": "Print the current working directory"},
    {"command": f"{Color.GREEN}pushd{Color.RESET} <directory>", "description": "Guarda el directorio actual y cambia al indicado", "description_en": "Save current directory and switch to the given one"},
    {"command": f"{Color.GREEN}popd{Color.RESET}", "description": "Vuelve al directorio guardado anteriormente", "description_en": "Return to the previously saved directory"},
    {"command": f"{Color.GREEN}dirs{Color.RESET}", "description": "Muestra la pila de directorios", "description_en": "Show the directory stack"},

    {"section": "Gestión de archivos y directorios", "section_en": "File and Directory Management"},
    {"command": f"{Color.GREEN}touch{Color.RESET} <file>", "description": "Crea un archivo vacío o actualiza su timestamp", "description_en": "Create an empty file or update its timestamp"},
    {"command": f"{Color.GREEN}mkdir{Color.RESET} <directory>", "description": "Crea un nuevo directorio", "description_en": "Create a new directory"},
    {"command": f"{Color.GREEN}mkdir{Color.RESET} -p <path>", "description": "Crea directorios incluyendo los padres necesarios", "description_en": "Create directory and all parent directories"},
    {"command": f"{Color.GREEN}rm{Color.RESET} <file>", "description": "Elimina un archivo", "description_en": "Remove a file"},
    {"command": f"{Color.GREEN}rm{Color.RESET} -r <directory>", "description": "Elimina un directorio y su contenido", "description_en": "Remove a directory and its contents"},
    {"command": f"{Color.GREEN}cp{Color.RESET} <src> <dst>", "description": "Copia un archivo", "description_en": "Copy a file"},
    {"command": f"{Color.GREEN}cp{Color.RESET} -r <src_dir> <dst>", "description": "Copia un directorio de forma recursiva", "description_en": "Copy a directory recursively"},
    {"command": f"{Color.GREEN}mv{Color.RESET} <src> <dst>", "description": "Mueve o renombra un archivo o directorio", "description_en": "Move or rename a file or directory"},
    {"command": f"{Color.GREEN}ln{Color.RESET} -s <target> <link>", "description": "Crea un enlace simbólico", "description_en": "Create a symbolic link"},
    {"command": f"{Color.GREEN}locate{Color.RESET} <filename>", "description": "Busca archivos usando la base de datos de locate", "description_en": "Find files using the locate database"},

    {"section": "Visualización de archivos", "section_en": "File Viewing"},
    {"command": f"{Color.GREEN}cat{Color.RESET} <file>", "description": "Muestra el contenido de un archivo", "description_en": "Display file contents"},
    {"command": f"{Color.GREEN}less{Color.RESET} <file>", "description": "Muestra el contenido de forma interactiva", "description_en": "Display file contents interactively"},
    {"command": f"{Color.GREEN}more{Color.RESET} <file>", "description": "Muestra el contenido página por página", "description_en": "Display file contents page by page"},
    {"command": f"{Color.GREEN}nl{Color.RESET} <file>", "description": "Muestra el contenido con números de línea", "description_en": "Display file contents with line numbers"},

    {"section": "Información del sistema", "section_en": "System Information"},
    {"command": f"{Color.GREEN}stat{Color.RESET} <file>", "description": "Muestra detalles del archivo (timestamps, permisos)", "description_en": "Show file details (timestamps, permissions)"},
    {"command": f"{Color.GREEN}date{Color.RESET}", "description": "Muestra la fecha y hora actuales", "description_en": "Show current date and time"},
    {"command": f"{Color.GREEN}uptime{Color.RESET}", "description": "Muestra el tiempo que lleva encendido el sistema", "description_en": "Show how long the system has been running"},
    {"command": f"{Color.GREEN}whoami{Color.RESET}", "description": "Muestra el usuario actual", "description_en": "Show the current user"},
    {"command": f"{Color.GREEN}id{Color.RESET}", "description": "Muestra el UID, GID y grupos del usuario actual", "description_en": "Show UID, GID and groups of current user"},
    {"command": f"{Color.GREEN}hostname{Color.RESET}", "description": "Muestra o establece el nombre del host", "description_en": "Show or set the hostname"},

    {"section": "Listado de directorios", "section_en": "Directory Listing"},
    {"command": f"{Color.GREEN}ls{Color.RESET}", "description": "Lista el contenido del directorio actual", "description_en": "List the current directory contents"},
    {"command": f"{Color.GREEN}ls{Color.RESET} -a", "description": "Incluye archivos ocultos", "description_en": "Include hidden files"},
    {"command": f"{Color.GREEN}ls{Color.RESET} -l", "description": "Formato largo con detalles", "description_en": "Long format with details"},
    {"command": f"{Color.GREEN}ls{Color.RESET} -lh", "description": "Formato largo con tamaños legibles", "description_en": "Long format with human-readable sizes"},
    {"command": f"{Color.GREEN}tree{Color.RESET}", "description": "Muestra directorios en forma de árbol", "description_en": "Display directories as a tree"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
