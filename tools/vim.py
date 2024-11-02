from shellcolorize import Color

vim_commands = [
    {"command": f"{Color.GREEN}:w{Color.RESET}", "description": "Guarda el archivo actual"},
    {"command": f"{Color.GREEN}:q{Color.RESET}", "description": "Cierra el editor si no hay cambios sin guardar"},
    {"command": f"{Color.GREEN}:q!{Color.RESET}", "description": "Forza la salida sin guardar los cambios"},
    {"command": f"{Color.GREEN}:wq{Color.RESET}", "description": "Guarda y cierra el archivo"},
    {"command": f"{Color.GREEN}:e {Color.RESET}filename", "description": "Abre un archivo especificado"},
    {"command": f"{Color.GREEN}i{Color.RESET}", "description": "Entra en modo de inserción para escribir texto"},
    {"command": f"{Color.GREEN}ESC{Color.RESET}", "description": "Vuelve al modo normal desde el modo de inserción"},
    {"command": f"{Color.GREEN}dd{Color.RESET}", "description": "Elimina la línea actual"},
    {"command": f"{Color.GREEN}yy{Color.RESET}", "description": "Copia (yanks) la línea actual"},
    {"command": f"{Color.GREEN}p{Color.RESET}", "description": "Pega el contenido copiado o cortado"},
    {"command": f"{Color.GREEN}u{Color.RESET}", "description": "Deshace el último cambio"},
    {"command": f"{Color.GREEN}Ctrl + r{Color.RESET}", "description": "Rehace el último cambio deshecho"},
    {"command": f"{Color.GREEN}/palabra{Color.RESET}", "description": "Busca 'palabra' en el archivo"},
    {"command": f"{Color.GREEN}n{Color.RESET}", "description": "Navega a la siguiente coincidencia de búsqueda"},
    {"command": f"{Color.GREEN}N{Color.RESET}", "description": "Navega a la coincidencia de búsqueda anterior"},
    {"command": f"{Color.GREEN}:%s/old/new/g{Color.RESET}", "description": "Reemplaza todas las ocurrencias de 'old' por 'new' en todo el archivo"},
    {"command": f"{Color.GREEN}gg{Color.RESET}", "description": "Mueve el cursor al inicio del archivo"},
    {"command": f"{Color.GREEN}G{Color.RESET}", "description": "Mueve el cursor al final del archivo"},
    {"command": f"{Color.GREEN}0{Color.RESET}", "description": "Mueve el cursor al inicio de la línea actual"},
    {"command": f"{Color.GREEN}$ {Color.RESET}", "description": "Mueve el cursor al final de la línea actual"},
    {"command": f"{Color.GREEN}:%d{Color.RESET}", "description": "Elimina todo el contenido del archivo"},
    {"command": f"{Color.GREEN}v{Color.RESET}", "description": "Entra en modo visual para seleccionar texto"},
    {"command": f"{Color.GREEN}V{Color.RESET}", "description": "Entra en modo visual de línea para seleccionar líneas completas"},
    {"command": f"{Color.GREEN}Ctrl + v{Color.RESET}", "description": "Entra en modo visual en bloque (selección en columna)"},
    {"command": f"{Color.GREEN}>G{Color.RESET}", "description": "Indenta todas las líneas desde la actual hasta el final del archivo"},
    {"command": f"{Color.GREEN}:!command{Color.RESET}", "description": "Ejecuta un comando de shell sin salir de vim"},
    {"command": f"{Color.GREEN}:syntax on{Color.RESET}", "description": "Activa el resaltado de sintaxis"},
    {"command": f"{Color.GREEN}:set number{Color.RESET}", "description": "Muestra los números de línea"},
    {"command": f"{Color.GREEN}:set nohlsearch{Color.RESET}", "description": "Desactiva el resaltado de búsqueda"},
    {"command": f"{Color.GREEN}:split {Color.RESET}filename", "description": "Divide la ventana actual y abre un archivo en la nueva división"},
    {"command": f"{Color.GREEN}:vsplit {Color.RESET}filename", "description": "Divide la ventana verticalmente y abre un archivo en la nueva división"},
]

print(f"\nOpciones de VIM con ejemplos y descripciones:\n")
print(f"{'Comando':<21} | {'Descripción'}")
print("-" * 94)
for cmd in vim_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<30} | {description}")
