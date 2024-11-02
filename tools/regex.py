
# Configuración de colores
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

regex_patterns = [
    {"pattern": f"{YELLOW}^palabra{RESET}", "description": "Coincide con 'palabra' al inicio de la línea"},
    {"pattern": f"{YELLOW}palabra${RESET}", "description": "Coincide con 'palabra' al final de la línea"},
    {"pattern": f"{YELLOW}\\bpalabra\\b{RESET}", "description": "Coincide con 'palabra' como una palabra completa"},
    {"pattern": f"{YELLOW}.{RESET}", "description": "Coincide con cualquier carácter excepto nueva línea"},
    {"pattern": f"{YELLOW}\\d{RESET}", "description": "Coincide con cualquier dígito (equivalente a [0-9])"},
    {"pattern": f"{YELLOW}\\D{RESET}", "description": "Coincide con cualquier carácter que NO sea un dígito"},
    {"pattern": f"{YELLOW}\\w{RESET}", "description": "Coincide con cualquier carácter de palabra (letras, dígitos o guion bajo)"},
    {"pattern": f"{YELLOW}\\W{RESET}", "description": "Coincide con cualquier carácter que NO sea de palabra"},
    {"pattern": f"{YELLOW}\\s{RESET}", "description": "Coincide con cualquier espacio en blanco (espacio, tabulación, nueva línea)"},
    {"pattern": f"{YELLOW}\\S{RESET}", "description": "Coincide con cualquier carácter que NO sea un espacio en blanco"},
    {"pattern": f"{YELLOW}[aeiou]{RESET}", "description": "Coincide con cualquier vocal minúscula"},
    {"pattern": f"{YELLOW}[^aeiou]{RESET}", "description": "Coincide con cualquier carácter que NO sea una vocal minúscula"},
    {"pattern": f"{YELLOW}[A-Za-z]{RESET}", "description": "Coincide con cualquier letra mayúscula o minúscula"},
    {"pattern": f"{YELLOW}[0-9]{RESET}", "description": "Coincide con cualquier dígito"},
    {"pattern": f"{YELLOW}palabra{{3}}{RESET}", "description": "Coincide con exactamente 3 repeticiones de 'palabra'"},
    {"pattern": f"{YELLOW}palabra{{2,5}}{RESET}", "description": "Coincide con entre 2 y 5 repeticiones de 'palabra'"},
    {"pattern": f"{YELLOW}palabra*{RESET}", "description": "Coincide con 0 o más repeticiones de 'palabra'"},
    {"pattern": f"{YELLOW}palabra+{RESET}", "description": "Coincide con 1 o más repeticiones de 'palabra'"},
    {"pattern": f"{YELLOW}palabra?{RESET}", "description": "Coincide con 0 o 1 repetición de 'palabra'"},
    {"pattern": f"{YELLOW}(palabra1|palabra2){RESET}", "description": "Coincide con 'palabra1' o 'palabra2'"},
    {"pattern": f"{YELLOW}(?<=@)\\w+{RESET}", "description": "Coincide con cualquier palabra precedida de '@' (lookbehind positivo)"},
    {"pattern": f"{YELLOW}(?<!@)\\w+{RESET}", "description": "Coincide con cualquier palabra que NO esté precedida de '@' (lookbehind negativo)"},
    {"pattern": f"{YELLOW}\\w+(?=\\.com){RESET}", "description": "Coincide con cualquier palabra seguida de '.com' (lookahead positivo)"},
    {"pattern": f"{YELLOW}\\w+(?!\\.com){RESET}", "description": "Coincide con cualquier palabra que NO esté seguida de '.com' (lookahead negativo)"},
    {"pattern": f"{YELLOW}(?i)palabra{RESET}", "description": "Coincide con 'palabra' ignorando mayúsculas y minúsculas"},
    {"pattern": f"{YELLOW}\\\\{RESET}", "description": "Coincide con el carácter de barra invertida '\\'"},
    {"pattern": f"{YELLOW}\\n{RESET}", "description": "Coincide con el carácter de nueva línea"},
    {"pattern": f"{YELLOW}\\t{RESET}", "description": "Coincide con el carácter de tabulación"},
    {"pattern": f"{YELLOW}^${RESET}", "description": "Coincide con una línea vacía"},
    {"pattern": f"{YELLOW}(?<=\\d)\\s(?=\\d){RESET}", "description": "Coincide con espacios entre dígitos (usado para números grandes separados por espacio)"},
]

print(f"\nPatrones de expresiones regulares con ejemplos y descripciones:\n")
print(f"{'Patrón':<21} | {'Descripción'}")
print("-" * 110)
for cmd in regex_patterns:
    pattern = cmd["pattern"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{pattern:<30} | {description}")

