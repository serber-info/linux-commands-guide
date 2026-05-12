from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de TEE"
TITLE_EN = "TEE Options"
BRIEF = "Lee stdin y escribe en stdout y archivos"
BRIEF_EN = "Read stdin and write to stdout and files"

COMMANDS = [
    {"command": f"{Color.GREEN}ls{Color.RESET} | {Color.GREEN}tee{Color.RESET} output.txt", "description": "Guarda la salida en un archivo y la muestra en pantalla", "description_en": "Save output to file and display on screen"},
    {"command": f"{Color.GREEN}ls{Color.RESET} | {Color.GREEN}tee{Color.RESET} -a output.txt", "description": "Agrega la salida al final del archivo", "description_en": "Append output to file"},
    {"command": f"{Color.GREEN}cmd{Color.RESET} | {Color.GREEN}tee{Color.RESET} /dev/tty output.txt", "description": "Envía la salida tanto a la consola como al archivo", "description_en": "Send output to both console and file"},
    {"command": f"{Color.GREEN}cmd{Color.RESET} | {Color.GREEN}tee{Color.RESET} file1.txt file2.txt", "description": "Escribe la salida en múltiples archivos a la vez", "description_en": "Write output to multiple files at once"},
    {"command": f"{Color.GREEN}cmd{Color.RESET} | {Color.GREEN}tee{Color.RESET} >(other_cmd)", "description": "Redirige la salida a otro comando con sustitución de proceso", "description_en": "Redirect output to another command via process substitution"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
