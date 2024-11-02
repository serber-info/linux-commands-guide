# Configuración de colores
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

top_commands = [
    {"command": f"{GREEN}top{RESET}", "description": "Inicia la interfaz interactiva de top con configuración predeterminada"},
    {"command": f"{GREEN}top{RESET} -b", "description": "Ejecuta top en modo batch (no interactivo), útil para scripts"},
    {"command": f"{GREEN}top{RESET} -d <delay>", "description": "Establece el retardo entre actualizaciones en segundos (ej. -d 2 para cada 2 segundos)"},
    {"command": f"{GREEN}top{RESET} -n <num>", "description": "Especifica el número de iteraciones de actualización antes de salir"},
    {"command": f"{GREEN}top{RESET} -p <pid>[,<pid>...]", "description": "Muestra solo los procesos con los PIDs especificados"},
    {"command": f"{GREEN}top{RESET} -u <user>", "description": "Filtra para mostrar solo procesos del usuario especificado"},
    {"command": f"{GREEN}top{RESET} -s", "description": "Ejecuta top en modo seguro, minimizando cambios al terminal"},
    {"command": f"{GREEN}top{RESET} -i", "description": "Omite los procesos inactivos (idle) de la lista de procesos mostrados"},
    {"command": f"{GREEN}top{RESET} -c", "description": "Muestra la línea completa del comando de cada proceso en lugar del nombre base"},
    {"command": f"{GREEN}top{RESET} -o <column>", "description": "Ordena la lista de procesos según la columna especificada (ej. %CPU)"},
    {"command": f"{GREEN}top{RESET} -H", "description": "Muestra cada hilo individual en lugar de agrupar por proceso"},
    {"command": f"{GREEN}top{RESET} -k <pid>", "description": "En modo interactivo, envía una señal de terminación a un proceso específico"},
    {"command": f"{GREEN}top{RESET} -w [num]", "description": "Define el ancho de pantalla; 'num' establece el número de columnas"},
    {"command": f"{GREEN}top{RESET} -1", "description": "Muestra cada CPU por separado en lugar de una vista agregada"},
    {"command": f"{GREEN}top{RESET} -x", "description": "Incluye todas las variables de entorno en el comando completo mostrado"},

    # Interactive commands
    {"command": f"{GREEN}top{RESET} q", "description": "Salir de la sesión de top"},
    {"command": f"{GREEN}top{RESET} h", "description": "Muestra la ayuda interactiva de top con todas las opciones disponibles"},
    {"command": f"{GREEN}top{RESET} Space", "description": "Fuerza una actualización inmediata de la pantalla"},
    {"command": f"{GREEN}top{RESET} k <pid>", "description": "Envía una señal a un proceso específico"},
    {"command": f"{GREEN}top{RESET} r <pid> <priority>", "description": "Cambia la prioridad (renice) de un proceso especificado"},
    {"command": f"{GREEN}top{RESET} z", "description": "Cambia el esquema de color de top (modo monocromático y color)"},
    {"command": f"{GREEN}top{RESET} i", "description": "Activa o desactiva la visualización de procesos inactivos"},
    {"command": f"{GREEN}top{RESET} u <user>", "description": "Filtra para mostrar solo procesos de un usuario especificado"},
    {"command": f"{GREEN}top{RESET} M", "description": "Ordena la lista de procesos por uso de memoria"},
    {"command": f"{GREEN}top{RESET} P", "description": "Ordena la lista de procesos por uso de CPU"},
    {"command": f"{GREEN}top{RESET} N", "description": "Ordena la lista de procesos por PID"},
    {"command": f"{GREEN}top{RESET} T", "description": "Ordena la lista de procesos por tiempo acumulado de CPU"},
    {"command": f"{GREEN}top{RESET} c", "description": "Alterna entre el nombre base del comando y la línea completa del comando"},
    {"command": f"{GREEN}top{RESET} V", "description": "Activa o desactiva el modo de árbol para visualizar procesos"},
    {"command": f"{GREEN}top{RESET} l", "description": "Muestra u oculta la primera línea de encabezado con la información de carga"},
    {"command": f"{GREEN}top{RESET} t", "description": "Muestra u oculta la segunda línea de encabezado con estadísticas de tareas"},
    {"command": f"{GREEN}top{RESET} m", "description": "Muestra u oculta la tercera línea de encabezado con estadísticas de memoria"},
    {"command": f"{GREEN}top{RESET} f", "description": "Abre el menú de campos para elegir las columnas de la lista de procesos"},
    {"command": f"{GREEN}top{RESET} W", "description": "Guarda las configuraciones actuales de top en el archivo de configuración"},
]

print(f"\nComandos de TOP con ejemplos y descripciones:\n")
print(f"{'Comando':<31} | {'Descripción'}")
print("-" * 120)
for cmd in top_commands:
    command = cmd["command"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<40} | {description}")
