from shellcolorize import Color

top_commands = [
    {"command": f"{Color.GREEN}top{Color.RESET}", "description": "Inicia la interfaz interactiva de top con configuración predeterminada"},
    {"command": f"{Color.GREEN}top{Color.RESET} -b", "description": "Ejecuta top en modo batch (no interactivo), útil para scripts"},
    {"command": f"{Color.GREEN}top{Color.RESET} -d <delay>", "description": "Establece el retardo entre actualizaciones en segundos (ej. -d 2 para cada 2 segundos)"},
    {"command": f"{Color.GREEN}top{Color.RESET} -n <num>", "description": "Especifica el número de iteraciones de actualización antes de salir"},
    {"command": f"{Color.GREEN}top{Color.RESET} -p <pid>[,<pid>...]", "description": "Muestra solo los procesos con los PIDs especificados"},
    {"command": f"{Color.GREEN}top{Color.RESET} -u <user>", "description": "Filtra para mostrar solo procesos del usuario especificado"},
    {"command": f"{Color.GREEN}top{Color.RESET} -s", "description": "Ejecuta top en modo seguro, minimizando cambios al terminal"},
    {"command": f"{Color.GREEN}top{Color.RESET} -i", "description": "Omite los procesos inactivos (idle) de la lista de procesos mostrados"},
    {"command": f"{Color.GREEN}top{Color.RESET} -c", "description": "Muestra la línea completa del comando de cada proceso en lugar del nombre base"},
    {"command": f"{Color.GREEN}top{Color.RESET} -o <column>", "description": "Ordena la lista de procesos según la columna especificada (ej. %CPU)"},
    {"command": f"{Color.GREEN}top{Color.RESET} -H", "description": "Muestra cada hilo individual en lugar de agrupar por proceso"},
    {"command": f"{Color.GREEN}top{Color.RESET} -k <pid>", "description": "En modo interactivo, envía una señal de terminación a un proceso específico"},
    {"command": f"{Color.GREEN}top{Color.RESET} -w [num]", "description": "Define el ancho de pantalla; 'num' establece el número de columnas"},
    {"command": f"{Color.GREEN}top{Color.RESET} -1", "description": "Muestra cada CPU por separado en lugar de una vista agregada"},
    {"command": f"{Color.GREEN}top{Color.RESET} -x", "description": "Incluye todas las variables de entorno en el comando completo mostrado"},

    # Interactive commands
    {"command": f"{Color.GREEN}top{Color.RESET} q", "description": "Salir de la sesión de top"},
    {"command": f"{Color.GREEN}top{Color.RESET} h", "description": "Muestra la ayuda interactiva de top con todas las opciones disponibles"},
    {"command": f"{Color.GREEN}top{Color.RESET} Space", "description": "Fuerza una actualización inmediata de la pantalla"},
    {"command": f"{Color.GREEN}top{Color.RESET} k <pid>", "description": "Envía una señal a un proceso específico"},
    {"command": f"{Color.GREEN}top{Color.RESET} r <pid> <priority>", "description": "Cambia la prioridad (renice) de un proceso especificado"},
    {"command": f"{Color.GREEN}top{Color.RESET} z", "description": "Cambia el esquema de color de top (modo monocromático y color)"},
    {"command": f"{Color.GREEN}top{Color.RESET} i", "description": "Activa o desactiva la visualización de procesos inactivos"},
    {"command": f"{Color.GREEN}top{Color.RESET} u <user>", "description": "Filtra para mostrar solo procesos de un usuario especificado"},
    {"command": f"{Color.GREEN}top{Color.RESET} M", "description": "Ordena la lista de procesos por uso de memoria"},
    {"command": f"{Color.GREEN}top{Color.RESET} P", "description": "Ordena la lista de procesos por uso de CPU"},
    {"command": f"{Color.GREEN}top{Color.RESET} N", "description": "Ordena la lista de procesos por PID"},
    {"command": f"{Color.GREEN}top{Color.RESET} T", "description": "Ordena la lista de procesos por tiempo acumulado de CPU"},
    {"command": f"{Color.GREEN}top{Color.RESET} c", "description": "Alterna entre el nombre base del comando y la línea completa del comando"},
    {"command": f"{Color.GREEN}top{Color.RESET} V", "description": "Activa o desactiva el modo de árbol para visualizar procesos"},
    {"command": f"{Color.GREEN}top{Color.RESET} l", "description": "Muestra u oculta la primera línea de encabezado con la información de carga"},
    {"command": f"{Color.GREEN}top{Color.RESET} t", "description": "Muestra u oculta la segunda línea de encabezado con estadísticas de tareas"},
    {"command": f"{Color.GREEN}top{Color.RESET} m", "description": "Muestra u oculta la tercera línea de encabezado con estadísticas de memoria"},
    {"command": f"{Color.GREEN}top{Color.RESET} f", "description": "Abre el menú de campos para elegir las columnas de la lista de procesos"},
    {"command": f"{Color.GREEN}top{Color.RESET} W", "description": "Guarda las configuraciones actuales de top en el archivo de configuración"},
]

print(f"\nComandos de TOP con ejemplos y descripciones:\n")
print(f"{'Comando':<31} | {'Descripción'}")
print("-" * 120)
for cmd in top_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<40} | {description}")
