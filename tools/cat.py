# Configuración de colores
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

cat_commands = [
    {"command": f"{GREEN}cat{RESET} filename", "description": "Muestra el contenido del archivo especificado"},
    {"command": f"{GREEN}cat{RESET} file1 file2 > output_file", "description": "Concatena los contenidos de 'file1' y 'file2' en 'output_file'"},
    {"command": f"{GREEN}cat{RESET} -n filename", "description": "Muestra el contenido del archivo con números de línea para cada línea"},
    {"command": f"{GREEN}cat{RESET} -b filename", "description": "Muestra el contenido del archivo numerando solo las líneas no vacías"},
    {"command": f"{GREEN}cat{RESET} -s filename", "description": "Suprime líneas vacías consecutivas, dejando solo una"},
    {"command": f"{GREEN}cat{RESET} -T filename", "description": "Muestra los caracteres de tabulación como ^I"},
    {"command": f"{GREEN}cat{RESET} -E filename", "description": "Muestra el carácter de fin de línea $ al final de cada línea"},
    {"command": f"{GREEN}cat{RESET} -v filename", "description": "Muestra caracteres no imprimibles, excepto tabulación y nueva línea"},
    
    # Additional batcat options adapted for cat alias
    {"command": f"{GREEN}cat{RESET} -A, --show-all filename", "description": "Muestra caracteres no imprimibles como espacios y tabulaciones"},
    {"command": f"{GREEN}cat{RESET} --nonprintable-notation <notation>", "description": "Define el formato para caracteres no imprimibles (unicode o caret)"},
    {"command": f"{GREEN}cat{RESET} -p, --plain filename", "description": "Muestra el contenido sin decoraciones, estilo plano"},
    {"command": f"{GREEN}cat{RESET} -l, --language <language>", "description": "Define explícitamente el lenguaje para resaltado de sintaxis"},
    {"command": f"{GREEN}cat{RESET} -H, --highlight-line <N:M>", "description": "Resalta líneas específicas con un fondo diferente"},
    {"command": f"{GREEN}cat{RESET} --file-name <name>", "description": "Especifica el nombre para mostrar (útil al leer de STDIN)"},
    {"command": f"{GREEN}cat{RESET} -d, --diff filename", "description": "Muestra solo líneas que difieren del índice de Git"},
    {"command": f"{GREEN}cat{RESET} --diff-context <N>", "description": "Define el contexto alrededor de las líneas modificadas en modo diff"},
    {"command": f"{GREEN}cat{RESET} --tabs <T>", "description": "Establece el tamaño de tabulación en T espacios"},
    {"command": f"{GREEN}cat{RESET} --wrap <mode>", "description": "Define el modo de ajuste de texto (auto, never, character)"},
    {"command": f"{GREEN}cat{RESET} -S, --chop-long-lines filename", "description": "Corta las líneas que exceden el ancho de pantalla"},
    {"command": f"{GREEN}cat{RESET} --terminal-width <width>", "description": "Define explícitamente el ancho de terminal"},
    {"command": f"{GREEN}cat{RESET} -n, --number filename", "description": "Muestra solo números de línea, sin decoraciones adicionales"},
    {"command": f"{GREEN}cat{RESET} --color <when>", "description": "Define cuándo usar colores en la salida (auto, never, always)"},
    {"command": f"{GREEN}cat{RESET} --italic-text <when>", "description": "Define el uso de texto en cursiva (always, never)"},
    {"command": f"{GREEN}cat{RESET} --decorations <when>", "description": "Define cuándo usar decoraciones adicionales (auto, never, always)"},
    {"command": f"{GREEN}cat{RESET} -f, --force-colorization filename", "description": "Forza la coloración y decoraciones en salida pipelined"},
    {"command": f"{GREEN}cat{RESET} --paging <when>", "description": "Define cuándo usar el paginador (auto, never, always)"},
    {"command": f"{GREEN}cat{RESET} --pager <command>", "description": "Especifica el paginador a utilizar (por defecto 'less')"},
    {"command": f"{GREEN}cat{RESET} -m, --map-syntax <glob:syntax>", "description": "Mapea un patrón de archivo a un lenguaje para resaltado de sintaxis"},
    {"command": f"{GREEN}cat{RESET} --ignored-suffix <suffix>", "description": "Ignora un sufijo en el nombre de archivo para determinar el tipo de sintaxis"},
    {"command": f"{GREEN}cat{RESET} --theme <theme>", "description": "Establece el tema para resaltado de sintaxis"},
    {"command": f"{GREEN}cat{RESET} --list-themes", "description": "Muestra una lista de temas disponibles para resaltado de sintaxis"},
    {"command": f"{GREEN}cat{RESET} --style <components>", "description": "Define qué elementos mostrar (líneas, encabezados, grid)"},
    {"command": f"{GREEN}cat{RESET} -r, --line-range <N:M> filename", "description": "Muestra solo las líneas N a M"},
    {"command": f"{GREEN}cat{RESET} -L, --list-languages", "description": "Muestra una lista de lenguajes soportados para resaltado de sintaxis"},
    {"command": f"{GREEN}cat{RESET} -u, --unbuffered", "description": "Desactiva el buffering (existe por compatibilidad POSIX)"},
    {"command": f"{GREEN}cat{RESET} --diagnostic", "description": "Muestra información diagnóstica para reportes de bugs"},
    {"command": f"{GREEN}cat{RESET} --acknowledgements", "description": "Muestra reconocimientos a los desarrolladores"},
    {"command": f"{GREEN}cat{RESET} -h, --help", "description": "Muestra esta ayuda de uso"},
    {"command": f"{GREEN}cat{RESET} -V, --version", "description": "Muestra la versión actual de cat (batcat alias)"},
]

print(f"\nComandos de CAT con ejemplos y descripciones:\n")
print(f"{'Comando':<41} | {'Descripción'}")
print("-" * 120)
for cmd in cat_commands:
    command = cmd["command"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<50} | {description}")
