from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de UNAME"
TITLE_EN = "UNAME Options"
BRIEF = "Información del sistema y kernel"
BRIEF_EN = "System and kernel information"

COMMANDS = [
    {"command": f"{Color.GREEN}uname{Color.RESET}", "description": "Muestra el nombre del kernel", "description_en": "Show the kernel name"},
    {"command": f"{Color.GREEN}uname{Color.RESET} -a", "description": "Muestra toda la información del sistema", "description_en": "Show all system information"},
    {"command": f"{Color.GREEN}uname{Color.RESET} -s", "description": "Muestra el nombre del kernel", "description_en": "Show the kernel name"},
    {"command": f"{Color.GREEN}uname{Color.RESET} -n", "description": "Muestra el nombre de red del host", "description_en": "Show the network hostname"},
    {"command": f"{Color.GREEN}uname{Color.RESET} -r", "description": "Muestra la versión del kernel", "description_en": "Show the kernel release"},
    {"command": f"{Color.GREEN}uname{Color.RESET} -v", "description": "Muestra la fecha de compilación del kernel", "description_en": "Show the kernel build date"},
    {"command": f"{Color.GREEN}uname{Color.RESET} -m", "description": "Muestra el tipo de hardware de la máquina", "description_en": "Show the machine hardware type"},
    {"command": f"{Color.GREEN}uname{Color.RESET} -p", "description": "Muestra el tipo de procesador", "description_en": "Show the processor type"},
    {"command": f"{Color.GREEN}uname{Color.RESET} -o", "description": "Muestra el sistema operativo", "description_en": "Show the operating system"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
