from shellcolorize import Color

lsblk_commands = [
    {"command": f"{Color.GREEN}lsblk{Color.RESET}", "description": "Lista información de todos los dispositivos de bloque del sistema"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} -a", "description": "Muestra todos los dispositivos, incluidos los vacíos"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} -b", "description": "Muestra tamaños en bytes en lugar de valores humanamente legibles"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} -d", "description": "Muestra solo las unidades de disco, excluyendo las particiones"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} -e <n>", "description": "Excluye dispositivos con un tipo de dispositivo específico, identificado por <n>"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} -f", "description": "Muestra la información del sistema de archivos, incluyendo UUID y etiqueta"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} -h", "description": "Muestra ayuda y opciones del comando"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} -i", "description": "Omite la columna de alineación de E/S (I/O alignment)"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} -J", "description": "Salida en formato JSON para una fácil interpretación por programas"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} -l", "description": "Muestra la información en formato de lista plana en lugar de árbol"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} -m", "description": "Incluye la información de permisos de cada dispositivo"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} -n", "description": "Suprime la fila de encabezado de la salida"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} -o <columns>", "description": "Especifica columnas a mostrar, separadas por comas. Usa -o NAME,SIZE para especificar múltiples"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} -O", "description": "Muestra información adicional de caché y otras opciones avanzadas"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} -P", "description": "Formato de salida en formato parseable (clave=valor)"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} -r", "description": "Produce una salida que es compatible para un reordenamiento (reordenable)"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} -s", "description": "Ordena la salida por la jerarquía de dispositivos (discos primero, particiones después)"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} -t", "description": "Muestra el árbol completo de dispositivos, incluso si hay duplicados"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} -u <unit>", "description": "Define la unidad de tamaño (ej. k, m, g) para los valores mostrados"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} -x <sort>", "description": "Ordena la salida de acuerdo con el criterio especificado (ej. -x SIZE)"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} --help", "description": "Muestra la ayuda con todas las opciones disponibles"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} --json", "description": "Muestra la salida en formato JSON, alias para -J"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} --list", "description": "Muestra la salida en formato de lista (similar a -l)"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} --output-all", "description": "Muestra todas las columnas disponibles en la salida"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} --pairs", "description": "Muestra la salida en formato parseable (clave=valor), similar a -P"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} --paths", "description": "Muestra nombres completos de dispositivos en la columna NAME"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} --fs", "description": "Muestra la información del sistema de archivos de cada dispositivo"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} --noheadings", "description": "Suprime el encabezado de columna en la salida (similar a -n)"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} --nodeps", "description": "Muestra solo dispositivos principales (similar a -d)"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} --raw", "description": "Formato de salida RAW para análisis programático"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} --scsi", "description": "Incluye información SCSI específica del dispositivo"},
    {"command": f"{Color.GREEN}lsblk{Color.RESET} --sysroot <dir>", "description": "Cambia la raíz del sistema para analizar dispositivos en otro sistema"},
]

print(f"\nComandos de LSBLK con ejemplos y descripciones:\n")
print(f"{'Comando':<31} | {'Descripción'}")
print("-" * 129)
for cmd in lsblk_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<40} | {description}")
