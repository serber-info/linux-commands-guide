from shellcolorize import Color

from shellcolorize import Color


awk_commands = [
    {"command": f"{Color.GREEN}awk{Color.RESET}", "options": f"{Color.YELLOW}'{{print $1}}'{Color.RESET} filename", "description": "Imprime solo la primera columna de cada línea del archivo"},
    {"command": f"{Color.GREEN}awk{Color.RESET}", "options": f"{Color.YELLOW}'{{print $1, $3}}'{Color.RESET} filename", "description": "Imprime la primera y tercera columna de cada línea"},
    {"command": f"{Color.GREEN}awk{Color.RESET}", "options": f"{Color.YELLOW}$3 > 100{Color.RESET} filename", "description": "Imprime las líneas donde la tercera columna es mayor a 100"},
    {"command": f"{Color.GREEN}awk{Color.RESET}", "options": f"{Color.YELLOW}-F',' '{{print $1}}'{Color.RESET} filename", "description": "Define ',' como delimitador de campo y muestra la primera columna"},
    {"command": f"{Color.GREEN}awk{Color.RESET}", "options": f"{Color.YELLOW}NR==5{Color.RESET} filename", "description": "Imprime solo la quinta línea del archivo"},
    {"command": f"{Color.GREEN}awk{Color.RESET}", "options": f"{Color.YELLOW}NR>5 && NR<10{Color.RESET} filename", "description": "Imprime las líneas del 6 al 9"},
    {"command": f"{Color.GREEN}awk{Color.RESET}", "options": f"{Color.YELLOW}/palabra/{Color.RESET} filename", "description": "Imprime las líneas que contienen 'palabra'"},
    {"command": f"{Color.GREEN}awk{Color.RESET}", "options": f"{Color.YELLOW}!/palabra/{Color.RESET} filename", "description": "Imprime las líneas que NO contienen 'palabra'"},
    {"command": f"{Color.GREEN}awk{Color.RESET}", "options": f"{Color.YELLOW}'{{sum += $1}} END {{print sum}}'{Color.RESET} filename", "description": "Suma la primera columna y muestra el resultado al final"},
    {"command": f"{Color.GREEN}awk{Color.RESET}", "options": f"{Color.YELLOW}'{{count++}} END {{print count}}'{Color.RESET} filename", "description": "Cuenta el número de líneas en el archivo"},
    {"command": f"{Color.GREEN}awk{Color.RESET}", "options": f"{Color.YELLOW}BEGIN '{{print \"Inicio\"}}'{Color.RESET} filename", "description": "Imprime 'Inicio' antes de procesar cualquier línea del archivo"},
    {"command": f"{Color.GREEN}awk{Color.RESET}", "options": f"{Color.YELLOW}END '{{print \"Fin\"}}'{Color.RESET} filename", "description": "Imprime 'Fin' después de procesar todas las líneas"},
    {"command": f"{Color.GREEN}awk{Color.RESET}", "options": f"{Color.YELLOW}'{{print NR, $0}}'{Color.RESET} filename", "description": "Imprime el número de línea seguido de la línea completa"},
    {"command": f"{Color.GREEN}awk{Color.RESET}", "options": f"{Color.YELLOW}'{{print NF}}'{Color.RESET} filename", "description": "Imprime el número de campos (columnas) en cada línea"},
    {"command": f"{Color.GREEN}awk{Color.RESET}", "options": f"{Color.YELLOW}$1 ~ /regex/{Color.RESET} filename", "description": "Imprime las líneas donde la primera columna coincide con la expresión regular"},
    {"command": f"{Color.GREEN}awk{Color.RESET}", "options": f"{Color.YELLOW}$1 !~ /regex/{Color.RESET} filename", "description": "Imprime las líneas donde la primera columna NO coincide con la expresión regular"},
    {"command": f"{Color.GREEN}awk{Color.RESET}", "options": f"{Color.YELLOW}'length($0) > 20'{Color.RESET} filename", "description": "Imprime las líneas que tienen más de 20 caracteres"},
    {"command": f"{Color.GREEN}awk{Color.RESET}", "options": f"{Color.YELLOW}'{{print tolower($0)}}'{Color.RESET} filename", "description": "Convierte todas las letras a minúsculas en cada línea"},
    {"command": f"{Color.GREEN}awk{Color.RESET}", "options": f"{Color.YELLOW}'{{print toupper($0)}}'{Color.RESET} filename", "description": "Convierte todas las letras a mayúsculas en cada línea"},
    {"command": f"{Color.GREEN}awk{Color.RESET}", "options": f"{Color.YELLOW}'{{sub(/viejo/, \"nuevo\"); print}}'{Color.RESET} filename", "description": "Reemplaza la primera aparición de 'viejo' por 'nuevo' en cada línea"},
    {"command": f"{Color.GREEN}awk{Color.RESET}", "options": f"{Color.YELLOW}'{{gsub(/viejo/, \"nuevo\"); print}}'{Color.RESET} filename", "description": "Reemplaza todas las apariciones de 'viejo' por 'nuevo' en cada línea"},
    {"command": f"{Color.GREEN}awk{Color.RESET}", "options": f"{Color.YELLOW}'{{if ($1 > 50) print $1}}'{Color.RESET} filename", "description": "Imprime la primera columna solo si su valor es mayor a 50"},
    {"command": f"{Color.GREEN}awk{Color.RESET}", "options": f"{Color.YELLOW}'{{if ($1 > 50) print \"Mayor\"; else print \"Menor\"}}'{Color.RESET} filename", "description": "Imprime 'Mayor' o 'Menor' dependiendo del valor de la primera columna"},
    {"command": f"{Color.GREEN}awk{Color.RESET}", "options": f"{Color.YELLOW}BEGIN {{OFS=\",\"}} '{{print $1, $2}}'{Color.RESET} filename", "description": "Establece ',' como el separador de salida y muestra las primeras dos columnas"},
    {"command": f"{Color.GREEN}awk{Color.RESET}", "options": f"{Color.YELLOW}'{{total += $3}} END {{print total/NR}}'{Color.RESET} filename", "description": "Calcula el promedio de la tercera columna"},
    {"command": f"{Color.GREEN}awk{Color.RESET}", "options": f"{Color.YELLOW}'{{a[NR]=$1}} END {{for (i=NR; i>0; i--) print a[i]}}'{Color.RESET} filename", "description": "Imprime la primera columna en orden inverso"},
    {"command": f"{Color.GREEN}awk{Color.RESET}", "options": f"{Color.YELLOW}'{{if ($2 > max) max=$2}} END {{print max}}'{Color.RESET} filename", "description": "Encuentra el valor máximo en la segunda columna"},
    {"command": f"{Color.GREEN}awk{Color.RESET}", "options": f"{Color.YELLOW}'{{if ($2 < min || NR==1) min=$2}} END {{print min}}'{Color.RESET} filename", "description": "Encuentra el valor mínimo en la segunda columna"},
    {"command": f"{Color.GREEN}awk{Color.RESET}", "options": f"{Color.YELLOW}BEGIN '{{srand(); print int(rand()*100)}}'{Color.RESET}", "description": "Genera un número aleatorio entre 0 y 100"},
]

print(f"\nOpciones de AWK con ejemplos y descripciones:\n")
print(f"{'Comando':<10} {'Opciones':<59} | {'Descripción'}")
print("-" * 155)
for cmd in awk_commands:
    command = cmd["command"]
    options = cmd["options"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<10} {options:<75} | {description}")

