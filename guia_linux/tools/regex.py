from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Expresiones Regulares"
TITLE_EN = "Regular Expressions"
BRIEF = "Patrones de búsqueda con regex"
BRIEF_EN = "Regex search patterns"

COMMANDS = [
    {"pattern": f"{Color.YELLOW}^word{Color.RESET}", "description": "Coincide con 'word' al inicio de la línea", "description_en": "Match 'word' at the start of the line"},
    {"pattern": f"{Color.YELLOW}word${Color.RESET}", "description": "Coincide con 'word' al final de la línea", "description_en": "Match 'word' at the end of the line"},
    {"pattern": f"{Color.YELLOW}\\bword\\b{Color.RESET}", "description": "Coincide con 'word' como palabra completa", "description_en": "Match 'word' as a whole word"},
    {"pattern": f"{Color.YELLOW}.{Color.RESET}", "description": "Cualquier carácter excepto nueva línea", "description_en": "Any character except newline"},
    {"pattern": f"{Color.YELLOW}\\d{Color.RESET}", "description": "Cualquier dígito (equivale a [0-9])", "description_en": "Any digit (equivalent to [0-9])"},
    {"pattern": f"{Color.YELLOW}\\D{Color.RESET}", "description": "Cualquier carácter que NO sea dígito", "description_en": "Any non-digit character"},
    {"pattern": f"{Color.YELLOW}\\w{Color.RESET}", "description": "Letra, dígito o guion bajo", "description_en": "Word character: letter, digit or underscore"},
    {"pattern": f"{Color.YELLOW}\\W{Color.RESET}", "description": "Carácter que NO sea de palabra", "description_en": "Non-word character"},
    {"pattern": f"{Color.YELLOW}\\s{Color.RESET}", "description": "Espacio en blanco (espacio, tabulación, nueva línea)", "description_en": "Whitespace (space, tab, newline)"},
    {"pattern": f"{Color.YELLOW}\\S{Color.RESET}", "description": "Carácter que NO sea espacio en blanco", "description_en": "Non-whitespace character"},
    {"pattern": f"{Color.YELLOW}[aeiou]{Color.RESET}", "description": "Cualquier vocal minúscula", "description_en": "Any lowercase vowel"},
    {"pattern": f"{Color.YELLOW}[^aeiou]{Color.RESET}", "description": "Cualquier carácter que NO sea vocal minúscula", "description_en": "Any character that is NOT a lowercase vowel"},
    {"pattern": f"{Color.YELLOW}[A-Za-z]{Color.RESET}", "description": "Cualquier letra mayúscula o minúscula", "description_en": "Any uppercase or lowercase letter"},
    {"pattern": f"{Color.YELLOW}word{{3}}{Color.RESET}", "description": "Exactamente 3 repeticiones de 'word'", "description_en": "Exactly 3 repetitions of 'word'"},
    {"pattern": f"{Color.YELLOW}word{{2,5}}{Color.RESET}", "description": "Entre 2 y 5 repeticiones de 'word'", "description_en": "Between 2 and 5 repetitions of 'word'"},
    {"pattern": f"{Color.YELLOW}word*{Color.RESET}", "description": "0 o más repeticiones", "description_en": "0 or more repetitions"},
    {"pattern": f"{Color.YELLOW}word+{Color.RESET}", "description": "1 o más repeticiones", "description_en": "1 or more repetitions"},
    {"pattern": f"{Color.YELLOW}word?{Color.RESET}", "description": "0 o 1 repetición", "description_en": "0 or 1 repetition"},
    {"pattern": f"{Color.YELLOW}(w1|w2){Color.RESET}", "description": "Coincide con 'w1' o 'w2'", "description_en": "Match 'w1' or 'w2'"},
    {"pattern": f"{Color.YELLOW}(?<=@)\\w+{Color.RESET}", "description": "Palabra precedida de '@' (lookbehind positivo)", "description_en": "Word preceded by '@' (positive lookbehind)"},
    {"pattern": f"{Color.YELLOW}\\w+(?=\\.com){Color.RESET}", "description": "Palabra seguida de '.com' (lookahead positivo)", "description_en": "Word followed by '.com' (positive lookahead)"},
    {"pattern": f"{Color.YELLOW}(?i)word{Color.RESET}", "description": "Coincide ignorando mayúsculas/minúsculas", "description_en": "Case-insensitive match"},
    {"pattern": f"{Color.YELLOW}^${Color.RESET}", "description": "Línea vacía", "description_en": "Empty line"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
