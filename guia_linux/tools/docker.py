from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de DOCKER"
TITLE_EN = "DOCKER Options"
BRIEF = "Gestión de contenedores Docker"
BRIEF_EN = "Docker container management"

COMMANDS = [
    {"command": f"{Color.GREEN}docker{Color.RESET} ps", "description": "Lista los contenedores en ejecución", "description_en": "List running containers"},
    {"command": f"{Color.GREEN}docker{Color.RESET} ps -a", "description": "Lista todos los contenedores (incluidos detenidos)", "description_en": "List all containers (including stopped)"},
    {"command": f"{Color.GREEN}docker{Color.RESET} images", "description": "Lista todas las imágenes disponibles", "description_en": "List all available images"},
    {"command": f"{Color.GREEN}docker{Color.RESET} run image_name", "description": "Inicia un contenedor desde la imagen", "description_en": "Start a container from an image"},
    {"command": f"{Color.GREEN}docker{Color.RESET} run -d image_name", "description": "Inicia un contenedor en segundo plano", "description_en": "Start a container in background (detached)"},
    {"command": f"{Color.GREEN}docker{Color.RESET} run -it image_name bash", "description": "Inicia un contenedor interactivo con shell", "description_en": "Start an interactive container with shell"},
    {"command": f"{Color.GREEN}docker{Color.RESET} run -p 8080:80 image_name", "description": "Mapea puerto del host al contenedor", "description_en": "Map host port to container port"},
    {"command": f"{Color.GREEN}docker{Color.RESET} start container_id", "description": "Inicia un contenedor detenido", "description_en": "Start a stopped container"},
    {"command": f"{Color.GREEN}docker{Color.RESET} stop container_id", "description": "Detiene un contenedor en ejecución", "description_en": "Stop a running container"},
    {"command": f"{Color.GREEN}docker{Color.RESET} restart container_id", "description": "Reinicia un contenedor", "description_en": "Restart a container"},
    {"command": f"{Color.GREEN}docker{Color.RESET} rm container_id", "description": "Elimina un contenedor detenido", "description_en": "Remove a stopped container"},
    {"command": f"{Color.GREEN}docker{Color.RESET} rmi image_id", "description": "Elimina una imagen", "description_en": "Remove an image"},
    {"command": f"{Color.GREEN}docker{Color.RESET} pull image_name", "description": "Descarga una imagen desde Docker Hub", "description_en": "Pull an image from Docker Hub"},
    {"command": f"{Color.GREEN}docker{Color.RESET} build -t name .", "description": "Construye una imagen desde un Dockerfile", "description_en": "Build an image from a Dockerfile"},
    {"command": f"{Color.GREEN}docker{Color.RESET} exec -it container_id bash", "description": "Ejecuta un shell interactivo en el contenedor", "description_en": "Run an interactive shell inside a container"},
    {"command": f"{Color.GREEN}docker{Color.RESET} logs container_id", "description": "Muestra los logs de un contenedor", "description_en": "Show container logs"},
    {"command": f"{Color.GREEN}docker{Color.RESET} logs -f container_id", "description": "Sigue los logs en tiempo real", "description_en": "Follow container logs in real time"},
    {"command": f"{Color.GREEN}docker{Color.RESET} inspect container_id", "description": "Muestra información detallada del contenedor", "description_en": "Show detailed container information"},
    {"command": f"{Color.GREEN}docker{Color.RESET} network ls", "description": "Lista las redes de Docker", "description_en": "List Docker networks"},
    {"command": f"{Color.GREEN}docker{Color.RESET} volume ls", "description": "Lista los volúmenes de Docker", "description_en": "List Docker volumes"},
    {"command": f"{Color.GREEN}docker{Color.RESET} system prune", "description": "Limpia recursos no utilizados", "description_en": "Remove unused containers, images, and networks"},
    {"command": f"{Color.GREEN}docker{Color.RESET} stats", "description": "Muestra el uso de recursos en tiempo real", "description_en": "Show live resource usage stats"},
    {"command": f"{Color.GREEN}docker{Color.RESET} compose up -d", "description": "Lanza servicios definidos en docker-compose.yml", "description_en": "Start services defined in docker-compose.yml"},
    {"command": f"{Color.GREEN}docker{Color.RESET} compose down", "description": "Detiene y elimina los servicios de compose", "description_en": "Stop and remove compose services"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
