from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de AWK"
TITLE_EN = "AWK Options"
BRIEF = "Procesamiento de texto por columnas"
BRIEF_EN = "Column-based text processing"

COMMANDS = [
    {"command": f"{Color.GREEN}awk{Color.RESET} '{{print $1}}' filename", "description": "Imprime la primera columna de cada línea", "description_en": "Print the first column of each line"},
    {"command": f"{Color.GREEN}awk{Color.RESET} '{{print $1, $3}}' filename", "description": "Imprime la primera y tercera columna", "description_en": "Print the first and third columns"},
    {"command": f"{Color.GREEN}awk{Color.RESET} '$3 > 100' filename", "description": "Imprime líneas donde la tercera columna > 100", "description_en": "Print lines where the third column > 100"},
    {"command": f"{Color.GREEN}awk{Color.RESET} -F',' '{{print $1}}' filename", "description": "Usa ',' como delimitador de campo", "description_en": "Use ',' as field delimiter"},
    {"command": f"{Color.GREEN}awk{Color.RESET} 'NR==5' filename", "description": "Imprime solo la quinta línea", "description_en": "Print only the fifth line"},
    {"command": f"{Color.GREEN}awk{Color.RESET} 'NR>5 && NR<10' filename", "description": "Imprime las líneas del 6 al 9", "description_en": "Print lines 6 through 9"},
    {"command": f"{Color.GREEN}awk{Color.RESET} '/word/' filename", "description": "Imprime líneas que contienen 'word'", "description_en": "Print lines containing 'word'"},
    {"command": f"{Color.GREEN}awk{Color.RESET} '!/word/' filename", "description": "Imprime líneas que NO contienen 'word'", "description_en": "Print lines NOT containing 'word'"},
    {"command": f"{Color.GREEN}awk{Color.RESET} '{{sum+=$1}} END {{print sum}}' filename", "description": "Suma la primera columna", "description_en": "Sum the first column"},
    {"command": f"{Color.GREEN}awk{Color.RESET} '{{count++}} END {{print count}}' filename", "description": "Cuenta el número de líneas", "description_en": "Count the number of lines"},
    {"command": f"{Color.GREEN}awk{Color.RESET} 'BEGIN {{print \"Start\"}}' filename", "description": "Imprime texto antes de procesar", "description_en": "Print text before processing"},
    {"command": f"{Color.GREEN}awk{Color.RESET} 'END {{print \"End\"}}' filename", "description": "Imprime texto después de procesar", "description_en": "Print text after processing"},
    {"command": f"{Color.GREEN}awk{Color.RESET} '{{print NR, $0}}' filename", "description": "Imprime número de línea seguido de la línea completa", "description_en": "Print line number followed by full line"},
    {"command": f"{Color.GREEN}awk{Color.RESET} '{{print NF}}' filename", "description": "Imprime el número de campos de cada línea", "description_en": "Print the number of fields per line"},
    {"command": f"{Color.GREEN}awk{Color.RESET} '$1 ~ /regex/' filename", "description": "Imprime líneas donde el campo 1 coincide con regex", "description_en": "Print lines where field 1 matches regex"},
    {"command": f"{Color.GREEN}awk{Color.RESET} 'length($0) > 20' filename", "description": "Imprime líneas con más de 20 caracteres", "description_en": "Print lines longer than 20 characters"},
    {"command": f"{Color.GREEN}awk{Color.RESET} '{{print tolower($0)}}' filename", "description": "Convierte a minúsculas", "description_en": "Convert to lowercase"},
    {"command": f"{Color.GREEN}awk{Color.RESET} '{{print toupper($0)}}' filename", "description": "Convierte a mayúsculas", "description_en": "Convert to uppercase"},
    {"command": f"{Color.GREEN}awk{Color.RESET} '{{sub(/old/,\"new\"); print}}' filename", "description": "Reemplaza la primera ocurrencia de 'old' por 'new'", "description_en": "Replace first occurrence of 'old' with 'new'"},
    {"command": f"{Color.GREEN}awk{Color.RESET} '{{gsub(/old/,\"new\"); print}}' filename", "description": "Reemplaza todas las ocurrencias de 'old' por 'new'", "description_en": "Replace all occurrences of 'old' with 'new'"},
    {"command": f"{Color.GREEN}awk{Color.RESET} '{{if ($1>50) print $1}}' filename", "description": "Imprime campo 1 solo si es mayor a 50", "description_en": "Print field 1 only if greater than 50"},
    {"command": f"{Color.GREEN}awk{Color.RESET} 'BEGIN {{OFS=\",\"}} {{print $1,$2}}' filename", "description": "Usa ',' como separador de salida", "description_en": "Use ',' as output field separator"},
    {"command": f"{Color.GREEN}awk{Color.RESET} '{{total+=$3}} END {{print total/NR}}' filename", "description": "Calcula el promedio de la tercera columna", "description_en": "Calculate the average of the third column"},
    {"command": f"{Color.GREEN}awk{Color.RESET} '{{if ($2>max) max=$2}} END {{print max}}' filename", "description": "Encuentra el valor máximo de la segunda columna", "description_en": "Find the maximum value of the second column"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
