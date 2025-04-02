from shellcolorize import Color

regex_patterns = [
    {"pattern": f"{Color.YELLOW}^palabra{Color.RESET}", "description": "Coincide con 'palabra' al inicio de la línea"},
    {"pattern": f"{Color.YELLOW}palabra${Color.RESET}", "description": "Coincide con 'palabra' al final de la línea"},
    {"pattern": f"{Color.YELLOW}\\bpalabra\\b{Color.RESET}", "description": "Coincide con 'palabra' como una palabra completa"},
    {"pattern": f"{Color.YELLOW}.{Color.RESET}", "description": "Coincide con cualquier carácter excepto nueva línea"},
    {"pattern": f"{Color.YELLOW}\\d{Color.RESET}", "description": "Coincide con cualquier dígito (equivalente a [0-9])"},
    {"pattern": f"{Color.YELLOW}\\D{Color.RESET}", "description": "Coincide con cualquier carácter que NO sea un dígito"},
    {"pattern": f"{Color.YELLOW}\\w{Color.RESET}", "description": "Coincide con cualquier carácter de palabra (letras, dígitos o guion bajo)"},
    {"pattern": f"{Color.YELLOW}\\W{Color.RESET}", "description": "Coincide con cualquier carácter que NO sea de palabra"},
    {"pattern": f"{Color.YELLOW}\\s{Color.RESET}", "description": "Coincide con cualquier espacio en blanco (espacio, tabulación, nueva línea)"},
    {"pattern": f"{Color.YELLOW}\\S{Color.RESET}", "description": "Coincide con cualquier carácter que NO sea un espacio en blanco"},
    {"pattern": f"{Color.YELLOW}[aeiou]{Color.RESET}", "description": "Coincide con cualquier vocal minúscula"},
    {"pattern": f"{Color.YELLOW}[^aeiou]{Color.RESET}", "description": "Coincide con cualquier carácter que NO sea una vocal minúscula"},
    {"pattern": f"{Color.YELLOW}[A-Za-z]{Color.RESET}", "description": "Coincide con cualquier letra mayúscula o minúscula"},
    {"pattern": f"{Color.YELLOW}[0-9]{Color.RESET}", "description": "Coincide con cualquier dígito"},
    {"pattern": f"{Color.YELLOW}palabra{{3}}{Color.RESET}", "description": "Coincide con exactamente 3 repeticiones de 'palabra'"},
    {"pattern": f"{Color.YELLOW}palabra{{2,5}}{Color.RESET}", "description": "Coincide con entre 2 y 5 repeticiones de 'palabra'"},
    {"pattern": f"{Color.YELLOW}palabra*{Color.RESET}", "description": "Coincide con 0 o más repeticiones de 'palabra'"},
    {"pattern": f"{Color.YELLOW}palabra+{Color.RESET}", "description": "Coincide con 1 o más repeticiones de 'palabra'"},
    {"pattern": f"{Color.YELLOW}palabra?{Color.RESET}", "description": "Coincide con 0 o 1 repetición de 'palabra'"},
    {"pattern": f"{Color.YELLOW}(palabra1|palabra2){Color.RESET}", "description": "Coincide con 'palabra1' o 'palabra2'"},
    {"pattern": f"{Color.YELLOW}(?<=@)\\w+{Color.RESET}", "description": "Coincide con cualquier palabra precedida de '@' (lookbehind positivo)"},
    {"pattern": f"{Color.YELLOW}(?<!@)\\w+{Color.RESET}", "description": "Coincide con cualquier palabra que NO esté precedida de '@' (lookbehind negativo)"},
    {"pattern": f"{Color.YELLOW}\\w+(?=\\.com){Color.RESET}", "description": "Coincide con cualquier palabra seguida de '.com' (lookahead positivo)"},
    {"pattern": f"{Color.YELLOW}\\w+(?!\\.com){Color.RESET}", "description": "Coincide con cualquier palabra que NO esté seguida de '.com' (lookahead negativo)"},
    {"pattern": f"{Color.YELLOW}(?i)palabra{Color.RESET}", "description": "Coincide con 'palabra' ignorando mayúsculas y minúsculas"},
    {"pattern": f"{Color.YELLOW}\\\\{Color.RESET}", "description": "Coincide con el carácter de barra invertida '\\'"},
    {"pattern": f"{Color.YELLOW}\\n{Color.RESET}", "description": "Coincide con el carácter de nueva línea"},
    {"pattern": f"{Color.YELLOW}\\t{Color.RESET}", "description": "Coincide con el carácter de tabulación"},
    {"pattern": f"{Color.YELLOW}^${Color.RESET}", "description": "Coincide con una línea vacía"},
    {"pattern": f"{Color.YELLOW}(?<=\\d)\\s(?=\\d){Color.RESET}", "description": "Coincide con espacios entre dígitos (usado para números grandes separados por espacio)"},
]

print(f"\nPatrones de expresiones regulares con ejemplos y descripciones:\n")
print(f"{'Patrón':<21} | {'Descripción'}")
print("-" * 110)
for cmd in regex_patterns:
    pattern = cmd["pattern"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{pattern:<30} | {description}")

