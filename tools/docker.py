
# Configuración de colores
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

docker_commands = [
    {"command": f"{GREEN}docker{RESET} ps", "description": "Lista los contenedores en ejecución"},
    {"command": f"{GREEN}docker{RESET} ps -a", "description": "Lista todos los contenedores (en ejecución y detenidos)"},
    {"command": f"{GREEN}docker{RESET} images", "description": "Lista todas las imágenes disponibles"},
    {"command": f"{GREEN}docker{RESET} run image_name", "description": "Inicia un nuevo contenedor a partir de la imagen especificada"},
    {"command": f"{GREEN}docker{RESET} run -d image_name", "description": "Inicia un contenedor en modo desprendido (background)"},
    {"command": f"{GREEN}docker{RESET} start container_id", "description": "Inicia un contenedor detenido"},
    {"command": f"{GREEN}docker{RESET} stop container_id", "description": "Detiene un contenedor en ejecución"},
    {"command": f"{GREEN}docker{RESET} restart container_id", "description": "Reinicia un contenedor en ejecución"},
    {"command": f"{GREEN}docker{RESET} rm container_id", "description": "Elimina un contenedor detenido"},
    {"command": f"{GREEN}docker{RESET} rmi image_id", "description": "Elimina una imagen"},
    {"command": f"{GREEN}docker{RESET} pull image_name", "description": "Descarga una imagen desde Docker Hub"},
    {"command": f"{GREEN}docker{RESET} build -t new_image_name .", "description": "Construye una imagen desde un Dockerfile en el directorio actual"},
    {"command": f"{GREEN}docker{RESET} exec -it container_id bash", "description": "Ejecuta un shell interactivo dentro de un contenedor"},
    {"command": f"{GREEN}docker{RESET} logs container_id", "description": "Muestra los registros (logs) de un contenedor"},
    {"command": f"{GREEN}docker{RESET} inspect container_id", "description": "Muestra información detallada de un contenedor"},
    {"command": f"{GREEN}docker{RESET} network ls", "description": "Lista las redes de Docker"},
    {"command": f"{GREEN}docker{RESET} volume ls", "description": "Lista los volúmenes de Docker"},
    {"command": f"{GREEN}docker{RESET} system prune", "description": "Limpia contenedores, imágenes, volúmenes y redes no utilizados"},
]

print(f"\nOpciones de DOCKER con ejemplos y descripciones:\n")
print(f"{'Comando':<41} | {'Descripción'}")
print("-" * 108)
for cmd in docker_commands:
    command = cmd["command"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<50} | {description}")

