from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Comandos de VIM"
TITLE_EN = "VIM Commands"
BRIEF = "Editor de texto modal en terminal"
BRIEF_EN = "Modal terminal text editor"

COMMANDS = [
    {"section": "Archivos", "section_en": "Files"},
    {"command": f"{Color.GREEN}:w{Color.RESET}", "description": "Guarda el archivo actual", "description_en": "Save the current file"},
    {"command": f"{Color.GREEN}:q{Color.RESET}", "description": "Cierra si no hay cambios sin guardar", "description_en": "Close if no unsaved changes"},
    {"command": f"{Color.GREEN}:q!{Color.RESET}", "description": "Fuerza la salida sin guardar", "description_en": "Force quit without saving"},
    {"command": f"{Color.GREEN}:wq{Color.RESET}", "description": "Guarda y cierra el archivo", "description_en": "Save and quit"},
    {"command": f"{Color.GREEN}:e filename{Color.RESET}", "description": "Abre un archivo para editar", "description_en": "Open a file for editing"},
    {"command": f"{Color.GREEN}:w filename{Color.RESET}", "description": "Guarda con un nombre de archivo diferente", "description_en": "Save with a different filename"},

    {"section": "Modos", "section_en": "Modes"},
    {"command": f"{Color.GREEN}i{Color.RESET}", "description": "Entra en modo inserción en la posición actual", "description_en": "Enter insert mode at cursor position"},
    {"command": f"{Color.GREEN}I{Color.RESET}", "description": "Entra en modo inserción al inicio de la línea", "description_en": "Enter insert mode at line start"},
    {"command": f"{Color.GREEN}a{Color.RESET}", "description": "Entra en modo inserción después del cursor", "description_en": "Enter insert mode after cursor"},
    {"command": f"{Color.GREEN}A{Color.RESET}", "description": "Entra en modo inserción al final de la línea", "description_en": "Enter insert mode at line end"},
    {"command": f"{Color.GREEN}o{Color.RESET}", "description": "Abre una nueva línea debajo y entra en inserción", "description_en": "Open new line below and enter insert mode"},
    {"command": f"{Color.GREEN}O{Color.RESET}", "description": "Abre una nueva línea arriba y entra en inserción", "description_en": "Open new line above and enter insert mode"},
    {"command": f"{Color.GREEN}v{Color.RESET}", "description": "Entra en modo visual (selección)", "description_en": "Enter visual mode (selection)"},
    {"command": f"{Color.GREEN}V{Color.RESET}", "description": "Entra en modo visual de línea completa", "description_en": "Enter visual line mode"},
    {"command": f"{Color.GREEN}ESC{Color.RESET}", "description": "Regresa al modo normal", "description_en": "Return to normal mode"},

    {"section": "Navegación", "section_en": "Navigation"},
    {"command": f"{Color.GREEN}gg{Color.RESET}", "description": "Va al inicio del archivo", "description_en": "Go to beginning of file"},
    {"command": f"{Color.GREEN}G{Color.RESET}", "description": "Va al final del archivo", "description_en": "Go to end of file"},
    {"command": f"{Color.GREEN}:N{Color.RESET}", "description": "Va a la línea N", "description_en": "Go to line N"},
    {"command": f"{Color.GREEN}0{Color.RESET}", "description": "Va al inicio de la línea", "description_en": "Go to start of line"},
    {"command": f"{Color.GREEN}${Color.RESET}", "description": "Va al final de la línea", "description_en": "Go to end of line"},
    {"command": f"{Color.GREEN}w{Color.RESET}", "description": "Salta al inicio de la siguiente palabra", "description_en": "Jump to start of next word"},
    {"command": f"{Color.GREEN}b{Color.RESET}", "description": "Salta al inicio de la palabra anterior", "description_en": "Jump to start of previous word"},

    {"section": "Edición", "section_en": "Editing"},
    {"command": f"{Color.GREEN}dd{Color.RESET}", "description": "Elimina (corta) la línea actual", "description_en": "Delete (cut) current line"},
    {"command": f"{Color.GREEN}yy{Color.RESET}", "description": "Copia la línea actual", "description_en": "Yank (copy) current line"},
    {"command": f"{Color.GREEN}p{Color.RESET}", "description": "Pega después del cursor", "description_en": "Paste after cursor"},
    {"command": f"{Color.GREEN}u{Color.RESET}", "description": "Deshace el último cambio", "description_en": "Undo last change"},
    {"command": f"{Color.GREEN}CTRL+r{Color.RESET}", "description": "Rehace el último cambio deshecho", "description_en": "Redo last undone change"},
    {"command": f"{Color.GREEN}x{Color.RESET}", "description": "Elimina el carácter bajo el cursor", "description_en": "Delete character under cursor"},

    {"section": "Búsqueda y sustitución", "section_en": "Search and Replace"},
    {"command": f"{Color.GREEN}/word{Color.RESET}", "description": "Busca 'word' hacia adelante", "description_en": "Search for 'word' forward"},
    {"command": f"{Color.GREEN}?word{Color.RESET}", "description": "Busca 'word' hacia atrás", "description_en": "Search for 'word' backward"},
    {"command": f"{Color.GREEN}n{Color.RESET}", "description": "Va a la siguiente coincidencia", "description_en": "Go to next match"},
    {"command": f"{Color.GREEN}N{Color.RESET}", "description": "Va a la coincidencia anterior", "description_en": "Go to previous match"},
    {"command": f"{Color.GREEN}:%s/old/new/g{Color.RESET}", "description": "Reemplaza 'old' por 'new' en todo el archivo", "description_en": "Replace 'old' with 'new' throughout the file"},
    {"command": f"{Color.GREEN}:%s/old/new/gc{Color.RESET}", "description": "Reemplaza con confirmación", "description_en": "Replace with confirmation"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
