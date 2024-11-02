
# Configuración de colores
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

awk_commands = [
    {"command": f"{GREEN}awk{RESET}", "options": f"{YELLOW}'{{print $1}}'{RESET} filename", "description": "Imprime solo la primera columna de cada línea del archivo"},
    {"command": f"{GREEN}awk{RESET}", "options": f"{YELLOW}'{{print $1, $3}}'{RESET} filename", "description": "Imprime la primera y tercera columna de cada línea"},
    {"command": f"{GREEN}awk{RESET}", "options": f"{YELLOW}$3 > 100{RESET} filename", "description": "Imprime las líneas donde la tercera columna es mayor a 100"},
    {"command": f"{GREEN}awk{RESET}", "options": f"{YELLOW}-F',' '{{print $1}}'{RESET} filename", "description": "Define ',' como delimitador de campo y muestra la primera columna"},
    {"command": f"{GREEN}awk{RESET}", "options": f"{YELLOW}NR==5{RESET} filename", "description": "Imprime solo la quinta línea del archivo"},
    {"command": f"{GREEN}awk{RESET}", "options": f"{YELLOW}NR>5 && NR<10{RESET} filename", "description": "Imprime las líneas del 6 al 9"},
    {"command": f"{GREEN}awk{RESET}", "options": f"{YELLOW}/palabra/{RESET} filename", "description": "Imprime las líneas que contienen 'palabra'"},
    {"command": f"{GREEN}awk{RESET}", "options": f"{YELLOW}!/palabra/{RESET} filename", "description": "Imprime las líneas que NO contienen 'palabra'"},
    {"command": f"{GREEN}awk{RESET}", "options": f"{YELLOW}'{{sum += $1}} END {{print sum}}'{RESET} filename", "description": "Suma la primera columna y muestra el resultado al final"},
    {"command": f"{GREEN}awk{RESET}", "options": f"{YELLOW}'{{count++}} END {{print count}}'{RESET} filename", "description": "Cuenta el número de líneas en el archivo"},
    {"command": f"{GREEN}awk{RESET}", "options": f"{YELLOW}BEGIN '{{print \"Inicio\"}}'{RESET} filename", "description": "Imprime 'Inicio' antes de procesar cualquier línea del archivo"},
    {"command": f"{GREEN}awk{RESET}", "options": f"{YELLOW}END '{{print \"Fin\"}}'{RESET} filename", "description": "Imprime 'Fin' después de procesar todas las líneas"},
    {"command": f"{GREEN}awk{RESET}", "options": f"{YELLOW}'{{print NR, $0}}'{RESET} filename", "description": "Imprime el número de línea seguido de la línea completa"},
    {"command": f"{GREEN}awk{RESET}", "options": f"{YELLOW}'{{print NF}}'{RESET} filename", "description": "Imprime el número de campos (columnas) en cada línea"},
    {"command": f"{GREEN}awk{RESET}", "options": f"{YELLOW}$1 ~ /regex/{RESET} filename", "description": "Imprime las líneas donde la primera columna coincide con la expresión regular"},
    {"command": f"{GREEN}awk{RESET}", "options": f"{YELLOW}$1 !~ /regex/{RESET} filename", "description": "Imprime las líneas donde la primera columna NO coincide con la expresión regular"},
    {"command": f"{GREEN}awk{RESET}", "options": f"{YELLOW}'length($0) > 20'{RESET} filename", "description": "Imprime las líneas que tienen más de 20 caracteres"},
    {"command": f"{GREEN}awk{RESET}", "options": f"{YELLOW}'{{print tolower($0)}}'{RESET} filename", "description": "Convierte todas las letras a minúsculas en cada línea"},
    {"command": f"{GREEN}awk{RESET}", "options": f"{YELLOW}'{{print toupper($0)}}'{RESET} filename", "description": "Convierte todas las letras a mayúsculas en cada línea"},
    {"command": f"{GREEN}awk{RESET}", "options": f"{YELLOW}'{{sub(/viejo/, \"nuevo\"); print}}'{RESET} filename", "description": "Reemplaza la primera aparición de 'viejo' por 'nuevo' en cada línea"},
    {"command": f"{GREEN}awk{RESET}", "options": f"{YELLOW}'{{gsub(/viejo/, \"nuevo\"); print}}'{RESET} filename", "description": "Reemplaza todas las apariciones de 'viejo' por 'nuevo' en cada línea"},
    {"command": f"{GREEN}awk{RESET}", "options": f"{YELLOW}'{{if ($1 > 50) print $1}}'{RESET} filename", "description": "Imprime la primera columna solo si su valor es mayor a 50"},
    {"command": f"{GREEN}awk{RESET}", "options": f"{YELLOW}'{{if ($1 > 50) print \"Mayor\"; else print \"Menor\"}}'{RESET} filename", "description": "Imprime 'Mayor' o 'Menor' dependiendo del valor de la primera columna"},
    {"command": f"{GREEN}awk{RESET}", "options": f"{YELLOW}BEGIN {{OFS=\",\"}} '{{print $1, $2}}'{RESET} filename", "description": "Establece ',' como el separador de salida y muestra las primeras dos columnas"},
    {"command": f"{GREEN}awk{RESET}", "options": f"{YELLOW}'{{total += $3}} END {{print total/NR}}'{RESET} filename", "description": "Calcula el promedio de la tercera columna"},
    {"command": f"{GREEN}awk{RESET}", "options": f"{YELLOW}'{{a[NR]=$1}} END {{for (i=NR; i>0; i--) print a[i]}}'{RESET} filename", "description": "Imprime la primera columna en orden inverso"},
    {"command": f"{GREEN}awk{RESET}", "options": f"{YELLOW}'{{if ($2 > max) max=$2}} END {{print max}}'{RESET} filename", "description": "Encuentra el valor máximo en la segunda columna"},
    {"command": f"{GREEN}awk{RESET}", "options": f"{YELLOW}'{{if ($2 < min || NR==1) min=$2}} END {{print min}}'{RESET} filename", "description": "Encuentra el valor mínimo en la segunda columna"},
    {"command": f"{GREEN}awk{RESET}", "options": f"{YELLOW}BEGIN '{{srand(); print int(rand()*100)}}'{RESET}", "description": "Genera un número aleatorio entre 0 y 100"},
]

print(f"\nOpciones de AWK con ejemplos y descripciones:\n")
print(f"{'Comando':<10} {'Opciones':<59} | {'Descripción'}")
print("-" * 155)
for cmd in awk_commands:
    command = cmd["command"]
    options = cmd["options"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<10} {options:<75} | {description}")

