from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Descriptores de Archivo y Redirecciones"
TITLE_EN = "File Descriptors and Redirections"
BRIEF = "Redirecciones de stdin, stdout y stderr"
BRIEF_EN = "stdin, stdout and stderr redirections"

COMMANDS = [
    {"command": f"{Color.GREEN}command{Color.RESET} > file", "description": "Redirige stdout a un archivo (sobreescribe)", "description_en": "Redirect stdout to file (overwrite)"},
    {"command": f"{Color.GREEN}command{Color.RESET} >> file", "description": "Agrega stdout al final de un archivo", "description_en": "Append stdout to file"},
    {"command": f"{Color.GREEN}command{Color.RESET} 2> file", "description": "Redirige stderr a un archivo", "description_en": "Redirect stderr to file"},
    {"command": f"{Color.GREEN}command{Color.RESET} 2>> file", "description": "Agrega stderr al final de un archivo", "description_en": "Append stderr to file"},
    {"command": f"{Color.GREEN}command{Color.RESET} > file 2>&1", "description": "Redirige stdout y stderr al mismo archivo", "description_en": "Redirect both stdout and stderr to file"},
    {"command": f"{Color.GREEN}command{Color.RESET} &> file", "description": "Redirige stdout y stderr (forma corta)", "description_en": "Redirect stdout and stderr (shorthand)"},
    {"command": f"{Color.GREEN}command{Color.RESET} < file", "description": "Usa un archivo como stdin", "description_en": "Use file as stdin"},
    {"command": f"{Color.GREEN}command{Color.RESET} 2> /dev/null", "description": "Descarta stderr", "description_en": "Discard stderr"},
    {"command": f"{Color.GREEN}command{Color.RESET} > /dev/null", "description": "Descarta stdout", "description_en": "Discard stdout"},
    {"command": f"{Color.GREEN}command{Color.RESET} > /dev/null 2>&1", "description": "Descarta stdout y stderr", "description_en": "Discard both stdout and stderr"},
    {"command": f"{Color.GREEN}command{Color.RESET} 3> file", "description": "Redirige el descriptor 3 a un archivo", "description_en": "Redirect file descriptor 3 to file"},
    {"command": f"{Color.GREEN}command{Color.RESET} 3>&-", "description": "Cierra el descriptor de archivo 3", "description_en": "Close file descriptor 3"},
    {"command": f"{Color.GREEN}exec{Color.RESET} 3> file", "description": "Abre el descriptor 3 para escritura", "description_en": "Open fd 3 for writing"},
    {"command": f"{Color.GREEN}exec{Color.RESET} 3< file", "description": "Abre el descriptor 3 para lectura", "description_en": "Open fd 3 for reading"},
    {"command": f"{Color.GREEN}command1{Color.RESET} | command2", "description": "Conecta stdout de command1 a stdin de command2", "description_en": "Pipe stdout of command1 to stdin of command2"},
    {"command": f"{Color.GREEN}command{Color.RESET} | tee file", "description": "Escribe stdout en un archivo y en pantalla", "description_en": "Write stdout to file and screen simultaneously"},
    {"command": f"{Color.GREEN}command{Color.RESET} | tee -a file", "description": "Agrega stdout al archivo y lo muestra en pantalla", "description_en": "Append stdout to file and display on screen"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
