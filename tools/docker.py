from shellcolorize import Color

docker_commands = [
    {"command": f"{Color.GREEN}docker{Color.RESET} ps", "description": "Lista los contenedores en ejecución"},
    {"command": f"{Color.GREEN}docker{Color.RESET} ps -a", "description": "Lista todos los contenedores (en ejecución y detenidos)"},
    {"command": f"{Color.GREEN}docker{Color.RESET} images", "description": "Lista todas las imágenes disponibles"},
    {"command": f"{Color.GREEN}docker{Color.RESET} run image_name", "description": "Inicia un nuevo contenedor a partir de la imagen especificada"},
    {"command": f"{Color.GREEN}docker{Color.RESET} run -d image_name", "description": "Inicia un contenedor en modo desprendido (background)"},
    {"command": f"{Color.GREEN}docker{Color.RESET} start container_id", "description": "Inicia un contenedor detenido"},
    {"command": f"{Color.GREEN}docker{Color.RESET} stop container_id", "description": "Detiene un contenedor en ejecución"},
    {"command": f"{Color.GREEN}docker{Color.RESET} restart container_id", "description": "Reinicia un contenedor en ejecución"},
    {"command": f"{Color.GREEN}docker{Color.RESET} rm container_id", "description": "Elimina un contenedor detenido"},
    {"command": f"{Color.GREEN}docker{Color.RESET} rmi image_id", "description": "Elimina una imagen"},
    {"command": f"{Color.GREEN}docker{Color.RESET} pull image_name", "description": "Descarga una imagen desde Docker Hub"},
    {"command": f"{Color.GREEN}docker{Color.RESET} build -t new_image_name .", "description": "Construye una imagen desde un Dockerfile en el directorio actual"},
    {"command": f"{Color.GREEN}docker{Color.RESET} exec -it container_id bash", "description": "Ejecuta un shell interactivo dentro de un contenedor"},
    {"command": f"{Color.GREEN}docker{Color.RESET} logs container_id", "description": "Muestra los registros (logs) de un contenedor"},
    {"command": f"{Color.GREEN}docker{Color.RESET} inspect container_id", "description": "Muestra información detallada de un contenedor"},
    {"command": f"{Color.GREEN}docker{Color.RESET} network ls", "description": "Lista las redes de Docker"},
    {"command": f"{Color.GREEN}docker{Color.RESET} volume ls", "description": "Lista los volúmenes de Docker"},
    {"command": f"{Color.GREEN}docker{Color.RESET} system prune", "description": "Limpia contenedores, imágenes, volúmenes y redes no utilizados"},
]

print(f"\nOpciones de DOCKER con ejemplos y descripciones:\n")
print(f"{'Comando':<41} | {'Descripción'}")
print("-" * 108)
for cmd in docker_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<50} | {description}")

