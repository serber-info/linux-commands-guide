
# Configuración de colores
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

vim_commands = [
    {"command": f"{GREEN}:w{RESET}", "description": "Guarda el archivo actual"},
    {"command": f"{GREEN}:q{RESET}", "description": "Cierra el editor si no hay cambios sin guardar"},
    {"command": f"{GREEN}:q!{RESET}", "description": "Forza la salida sin guardar los cambios"},
    {"command": f"{GREEN}:wq{RESET}", "description": "Guarda y cierra el archivo"},
    {"command": f"{GREEN}:e {RESET}filename", "description": "Abre un archivo especificado"},
    {"command": f"{GREEN}i{RESET}", "description": "Entra en modo de inserción para escribir texto"},
    {"command": f"{GREEN}ESC{RESET}", "description": "Vuelve al modo normal desde el modo de inserción"},
    {"command": f"{GREEN}dd{RESET}", "description": "Elimina la línea actual"},
    {"command": f"{GREEN}yy{RESET}", "description": "Copia (yanks) la línea actual"},
    {"command": f"{GREEN}p{RESET}", "description": "Pega el contenido copiado o cortado"},
    {"command": f"{GREEN}u{RESET}", "description": "Deshace el último cambio"},
    {"command": f"{GREEN}Ctrl + r{RESET}", "description": "Rehace el último cambio deshecho"},
    {"command": f"{GREEN}/palabra{RESET}", "description": "Busca 'palabra' en el archivo"},
    {"command": f"{GREEN}n{RESET}", "description": "Navega a la siguiente coincidencia de búsqueda"},
    {"command": f"{GREEN}N{RESET}", "description": "Navega a la coincidencia de búsqueda anterior"},
    {"command": f"{GREEN}:%s/old/new/g{RESET}", "description": "Reemplaza todas las ocurrencias de 'old' por 'new' en todo el archivo"},
    {"command": f"{GREEN}gg{RESET}", "description": "Mueve el cursor al inicio del archivo"},
    {"command": f"{GREEN}G{RESET}", "description": "Mueve el cursor al final del archivo"},
    {"command": f"{GREEN}0{RESET}", "description": "Mueve el cursor al inicio de la línea actual"},
    {"command": f"{GREEN}$ {RESET}", "description": "Mueve el cursor al final de la línea actual"},
    {"command": f"{GREEN}:%d{RESET}", "description": "Elimina todo el contenido del archivo"},
    {"command": f"{GREEN}v{RESET}", "description": "Entra en modo visual para seleccionar texto"},
    {"command": f"{GREEN}V{RESET}", "description": "Entra en modo visual de línea para seleccionar líneas completas"},
    {"command": f"{GREEN}Ctrl + v{RESET}", "description": "Entra en modo visual en bloque (selección en columna)"},
    {"command": f"{GREEN}>G{RESET}", "description": "Indenta todas las líneas desde la actual hasta el final del archivo"},
    {"command": f"{GREEN}:!command{RESET}", "description": "Ejecuta un comando de shell sin salir de vim"},
    {"command": f"{GREEN}:syntax on{RESET}", "description": "Activa el resaltado de sintaxis"},
    {"command": f"{GREEN}:set number{RESET}", "description": "Muestra los números de línea"},
    {"command": f"{GREEN}:set nohlsearch{RESET}", "description": "Desactiva el resaltado de búsqueda"},
    {"command": f"{GREEN}:split {RESET}filename", "description": "Divide la ventana actual y abre un archivo en la nueva división"},
    {"command": f"{GREEN}:vsplit {RESET}filename", "description": "Divide la ventana verticalmente y abre un archivo en la nueva división"},
]

print(f"\nOpciones de VIM con ejemplos y descripciones:\n")
print(f"{'Comando':<21} | {'Descripción'}")
print("-" * 94)
for cmd in vim_commands:
    command = cmd["command"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<30} | {description}")
