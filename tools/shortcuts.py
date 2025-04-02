from shellcolorize import Color

shortcuts = [
    {"command": f"{Color.GREEN}[TAB]{Color.RESET}", "description": "Autocompleta comandos, rutas u opciones posibles según el contexto"},
    
    {"command": f"{Color.GREEN}[CTRL] + A{Color.RESET}", "description": "Mueve el cursor al inicio de la línea actual"},
    {"command": f"{Color.GREEN}[CTRL] + E{Color.RESET}", "description": "Mueve el cursor al final de la línea actual"},
    {"command": f"{Color.GREEN}[CTRL] + [←] / [→]{Color.RESET}", "description": "Salta al principio de la palabra anterior/siguiente"},
    {"command": f"{Color.GREEN}[ALT] + B / F{Color.RESET}", "description": "Retrocede/avanza una palabra"},

    {"command": f"{Color.GREEN}[CTRL] + U{Color.RESET}", "description": "Elimina desde el cursor hasta el inicio de la línea"},
    {"command": f"{Color.GREEN}[CTRL] + K{Color.RESET}", "description": "Elimina desde el cursor hasta el final de la línea"},
    {"command": f"{Color.GREEN}[CTRL] + W{Color.RESET}", "description": "Elimina la palabra anterior al cursor"},

    {"command": f"{Color.GREEN}[CTRL] + Y{Color.RESET}", "description": "Pega el último contenido eliminado con CTRL+U, CTRL+K o CTRL+W"},

    {"command": f"{Color.GREEN}[CTRL] + C{Color.RESET}", "description": "Termina el proceso en ejecución (envía SIGINT)"},
    {"command": f"{Color.GREEN}[CTRL] + D{Color.RESET}", "description": "Cierra la entrada estándar (STDIN). También conocido como EOF"},
    {"command": f"{Color.GREEN}[CTRL] + L{Color.RESET}", "description": "Limpia la terminal (equivalente al comando 'clear')"},
    {"command": f"{Color.GREEN}[CTRL] + Z{Color.RESET}", "description": "Suspende el proceso actual (envía señal SIGTSTP)"},

    {"command": f"{Color.GREEN}[CTRL] + R{Color.RESET}", "description": "Busca en el historial de comandos mientras escribes"},
    {"command": f"{Color.GREEN}[↑] / [↓]{Color.RESET}", "description": "Navega por el historial de comandos anterior/siguiente"},

    {"command": f"{Color.GREEN}[ALT] + [TAB]{Color.RESET}", "description": "Cambia entre aplicaciones abiertas"},
    
    {"command": f"{Color.GREEN}[CTRL] + [+]{Color.RESET}", "description": "Aumenta el zoom del terminal o aplicación compatible"},
    {"command": f"{Color.GREEN}[CTRL] + [-]{Color.RESET}", "description": "Disminuye el zoom del terminal o aplicación compatible"},
]

print(f"\nAtajos de teclado en Linux con descripciones:\n")
print(f"{'Combinación':<26} | {'Descripción'}")
print("-" * 100)
for s in shortcuts:
    print(f"{s['command']:<35} | {Color.RED}{s['description']}{Color.RESET}")
