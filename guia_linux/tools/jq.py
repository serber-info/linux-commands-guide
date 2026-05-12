from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de JQ"
TITLE_EN = "JQ Options"
BRIEF = "Procesador de JSON en línea de comandos"
BRIEF_EN = "Command-line JSON processor"

COMMANDS = [
    {"command": f"{Color.GREEN}jq{Color.RESET} '.' file.json", "description": "Formatea y colorea el JSON de entrada", "description_en": "Pretty-print and colorize JSON input"},
    {"command": f"{Color.GREEN}jq{Color.RESET} '.key' file.json", "description": "Extrae el valor de una clave", "description_en": "Extract the value of a key"},
    {"command": f"{Color.GREEN}jq{Color.RESET} '.key.nested' file.json", "description": "Accede a una clave anidada", "description_en": "Access a nested key"},
    {"command": f"{Color.GREEN}jq{Color.RESET} '.array[]' file.json", "description": "Itera sobre los elementos de un array", "description_en": "Iterate over array elements"},
    {"command": f"{Color.GREEN}jq{Color.RESET} '.array[0]' file.json", "description": "Accede al primer elemento de un array", "description_en": "Access the first array element"},
    {"command": f"{Color.GREEN}jq{Color.RESET} '.[] | .name' file.json", "description": "Extrae 'name' de cada objeto del array", "description_en": "Extract 'name' from each array object"},
    {"command": f"{Color.GREEN}jq{Color.RESET} 'keys' file.json", "description": "Lista las claves del objeto JSON", "description_en": "List the keys of the JSON object"},
    {"command": f"{Color.GREEN}jq{Color.RESET} 'length' file.json", "description": "Devuelve la longitud del array u objeto", "description_en": "Return the length of array or object"},
    {"command": f"{Color.GREEN}jq{Color.RESET} 'select(.age > 18)' file.json", "description": "Filtra objetos por condición", "description_en": "Filter objects by condition"},
    {"command": f"{Color.GREEN}jq{Color.RESET} '{{name, age}}' file.json", "description": "Proyecta solo los campos seleccionados", "description_en": "Project only selected fields"},
    {"command": f"{Color.GREEN}jq{Color.RESET} '.[] | .name' file.json | {Color.GREEN}sort{Color.RESET}", "description": "Extrae y ordena valores", "description_en": "Extract and sort values"},
    {"command": f"{Color.GREEN}jq{Color.RESET} -r '.name' file.json", "description": "Salida en texto plano (sin comillas)", "description_en": "Raw string output (no quotes)"},
    {"command": f"{Color.GREEN}jq{Color.RESET} -c '.' file.json", "description": "Salida compacta en una sola línea", "description_en": "Compact single-line output"},
    {"command": f"{Color.GREEN}jq{Color.RESET} -n '{{a: 1, b: 2}}'", "description": "Crea un objeto JSON sin entrada", "description_en": "Create a JSON object without input"},
    {"command": f"{Color.GREEN}curl{Color.RESET} -s URL | {Color.GREEN}jq{Color.RESET} '.data'", "description": "Procesa la respuesta JSON de una API", "description_en": "Process JSON response from an API"},
    {"command": f"{Color.GREEN}jq{Color.RESET} '. + {{\"new_key\": \"value\"}}' file.json", "description": "Añade un campo nuevo al objeto", "description_en": "Add a new field to the object"},
    {"command": f"{Color.GREEN}jq{Color.RESET} 'del(.key)' file.json", "description": "Elimina un campo del objeto", "description_en": "Remove a field from the object"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
