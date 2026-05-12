from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de TMUX"
TITLE_EN = "TMUX Options"
BRIEF = "Multiplexor de terminal"
BRIEF_EN = "Terminal multiplexer"

COMMANDS = [
    {"section": "Sesiones", "section_en": "Sessions"},
    {"command": f"{Color.GREEN}tmux{Color.RESET}", "description": "Inicia una nueva sesión tmux", "description_en": "Start a new tmux session"},
    {"command": f"{Color.GREEN}tmux{Color.RESET} new -s name", "description": "Crea una nueva sesión con nombre", "description_en": "Create a new named session"},
    {"command": f"{Color.GREEN}tmux{Color.RESET} ls", "description": "Lista las sesiones activas", "description_en": "List active sessions"},
    {"command": f"{Color.GREEN}tmux{Color.RESET} attach -t name", "description": "Se conecta a una sesión existente", "description_en": "Attach to an existing session"},
    {"command": f"{Color.GREEN}tmux{Color.RESET} kill-session -t name", "description": "Cierra una sesión", "description_en": "Kill a session"},
    {"command": f"{Color.GREEN}tmux{Color.RESET} rename-session -t old new", "description": "Renombra una sesión", "description_en": "Rename a session"},

    {"section": "Atajos de teclado  (prefijo: Ctrl+B)", "section_en": "Keyboard Shortcuts  (prefix: Ctrl+B)"},
    {"command": f"{Color.GREEN}Ctrl+B  d{Color.RESET}", "description": "Desconecta (detach) de la sesión actual", "description_en": "Detach from the current session"},
    {"command": f"{Color.GREEN}Ctrl+B  c{Color.RESET}", "description": "Crea una nueva ventana", "description_en": "Create a new window"},
    {"command": f"{Color.GREEN}Ctrl+B  n / p{Color.RESET}", "description": "Cambia a la ventana siguiente / anterior", "description_en": "Switch to next / previous window"},
    {"command": f"{Color.GREEN}Ctrl+B  N{Color.RESET}", "description": "Cambia a la ventana número N", "description_en": "Switch to window number N"},
    {"command": f"{Color.GREEN}Ctrl+B  ,{Color.RESET}", "description": "Renombra la ventana actual", "description_en": "Rename the current window"},
    {"command": f"{Color.GREEN}Ctrl+B  &{Color.RESET}", "description": "Cierra la ventana actual", "description_en": "Close the current window"},
    {"command": f"{Color.GREEN}Ctrl+B  %{Color.RESET}", "description": "Divide el panel verticalmente", "description_en": "Split pane vertically"},
    {"command": f'{Color.GREEN}Ctrl+B  "{Color.RESET}', "description": "Divide el panel horizontalmente", "description_en": "Split pane horizontally"},
    {"command": f"{Color.GREEN}Ctrl+B  ←↑→↓{Color.RESET}", "description": "Navega entre paneles", "description_en": "Navigate between panes"},
    {"command": f"{Color.GREEN}Ctrl+B  z{Color.RESET}", "description": "Alterna el zoom del panel actual", "description_en": "Toggle zoom on current pane"},
    {"command": f"{Color.GREEN}Ctrl+B  x{Color.RESET}", "description": "Cierra el panel actual", "description_en": "Close the current pane"},
    {"command": f"{Color.GREEN}Ctrl+B  [{Color.RESET}", "description": "Entra en modo copiar/desplazamiento", "description_en": "Enter copy/scroll mode"},
    {"command": f"{Color.GREEN}Ctrl+B  ?{Color.RESET}", "description": "Muestra la lista de atajos de teclado", "description_en": "Show all keyboard shortcuts"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
