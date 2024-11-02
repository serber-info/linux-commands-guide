# Configuración de colores
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

lsblk_commands = [
    {"command": f"{GREEN}lsblk{RESET}", "description": "Lista información de todos los dispositivos de bloque del sistema"},
    {"command": f"{GREEN}lsblk{RESET} -a", "description": "Muestra todos los dispositivos, incluidos los vacíos"},
    {"command": f"{GREEN}lsblk{RESET} -b", "description": "Muestra tamaños en bytes en lugar de valores humanamente legibles"},
    {"command": f"{GREEN}lsblk{RESET} -d", "description": "Muestra solo las unidades de disco, excluyendo las particiones"},
    {"command": f"{GREEN}lsblk{RESET} -e <n>", "description": "Excluye dispositivos con un tipo de dispositivo específico, identificado por <n>"},
    {"command": f"{GREEN}lsblk{RESET} -f", "description": "Muestra la información del sistema de archivos, incluyendo UUID y etiqueta"},
    {"command": f"{GREEN}lsblk{RESET} -h", "description": "Muestra ayuda y opciones del comando"},
    {"command": f"{GREEN}lsblk{RESET} -i", "description": "Omite la columna de alineación de E/S (I/O alignment)"},
    {"command": f"{GREEN}lsblk{RESET} -J", "description": "Salida en formato JSON para una fácil interpretación por programas"},
    {"command": f"{GREEN}lsblk{RESET} -l", "description": "Muestra la información en formato de lista plana en lugar de árbol"},
    {"command": f"{GREEN}lsblk{RESET} -m", "description": "Incluye la información de permisos de cada dispositivo"},
    {"command": f"{GREEN}lsblk{RESET} -n", "description": "Suprime la fila de encabezado de la salida"},
    {"command": f"{GREEN}lsblk{RESET} -o <columns>", "description": "Especifica columnas a mostrar, separadas por comas. Usa -o NAME,SIZE para especificar múltiples"},
    {"command": f"{GREEN}lsblk{RESET} -O", "description": "Muestra información adicional de caché y otras opciones avanzadas"},
    {"command": f"{GREEN}lsblk{RESET} -P", "description": "Formato de salida en formato parseable (clave=valor)"},
    {"command": f"{GREEN}lsblk{RESET} -r", "description": "Produce una salida que es compatible para un reordenamiento (reordenable)"},
    {"command": f"{GREEN}lsblk{RESET} -s", "description": "Ordena la salida por la jerarquía de dispositivos (discos primero, particiones después)"},
    {"command": f"{GREEN}lsblk{RESET} -t", "description": "Muestra el árbol completo de dispositivos, incluso si hay duplicados"},
    {"command": f"{GREEN}lsblk{RESET} -u <unit>", "description": "Define la unidad de tamaño (ej. k, m, g) para los valores mostrados"},
    {"command": f"{GREEN}lsblk{RESET} -x <sort>", "description": "Ordena la salida de acuerdo con el criterio especificado (ej. -x SIZE)"},
    {"command": f"{GREEN}lsblk{RESET} --help", "description": "Muestra la ayuda con todas las opciones disponibles"},
    {"command": f"{GREEN}lsblk{RESET} --json", "description": "Muestra la salida en formato JSON, alias para -J"},
    {"command": f"{GREEN}lsblk{RESET} --list", "description": "Muestra la salida en formato de lista (similar a -l)"},
    {"command": f"{GREEN}lsblk{RESET} --output-all", "description": "Muestra todas las columnas disponibles en la salida"},
    {"command": f"{GREEN}lsblk{RESET} --pairs", "description": "Muestra la salida en formato parseable (clave=valor), similar a -P"},
    {"command": f"{GREEN}lsblk{RESET} --paths", "description": "Muestra nombres completos de dispositivos en la columna NAME"},
    {"command": f"{GREEN}lsblk{RESET} --fs", "description": "Muestra la información del sistema de archivos de cada dispositivo"},
    {"command": f"{GREEN}lsblk{RESET} --noheadings", "description": "Suprime el encabezado de columna en la salida (similar a -n)"},
    {"command": f"{GREEN}lsblk{RESET} --nodeps", "description": "Muestra solo dispositivos principales (similar a -d)"},
    {"command": f"{GREEN}lsblk{RESET} --raw", "description": "Formato de salida RAW para análisis programático"},
    {"command": f"{GREEN}lsblk{RESET} --scsi", "description": "Incluye información SCSI específica del dispositivo"},
    {"command": f"{GREEN}lsblk{RESET} --sysroot <dir>", "description": "Cambia la raíz del sistema para analizar dispositivos en otro sistema"},
]

print(f"\nComandos de LSBLK con ejemplos y descripciones:\n")
print(f"{'Comando':<31} | {'Descripción'}")
print("-" * 129)
for cmd in lsblk_commands:
    command = cmd["command"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<40} | {description}")
