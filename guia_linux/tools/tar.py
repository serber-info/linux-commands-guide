from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de TAR"
TITLE_EN = "TAR Options"
BRIEF = "Empaquetado y compresión de archivos"
BRIEF_EN = "File archiving and compression"

COMMANDS = [
    {"command": f"{Color.GREEN}tar{Color.RESET} -czf archive.tar.gz dir/", "description": "Crea un archivo .tar.gz comprimido con gzip", "description_en": "Create a gzip-compressed .tar.gz archive"},
    {"command": f"{Color.GREEN}tar{Color.RESET} -cjf archive.tar.bz2 dir/", "description": "Crea un archivo .tar.bz2 comprimido con bzip2", "description_en": "Create a bzip2-compressed .tar.bz2 archive"},
    {"command": f"{Color.GREEN}tar{Color.RESET} -cJf archive.tar.xz dir/", "description": "Crea un archivo .tar.xz comprimido con xz", "description_en": "Create an xz-compressed .tar.xz archive"},
    {"command": f"{Color.GREEN}tar{Color.RESET} -cf archive.tar dir/", "description": "Crea un archivo tar sin compresión", "description_en": "Create a tar archive without compression"},
    {"command": f"{Color.GREEN}tar{Color.RESET} -xzf archive.tar.gz", "description": "Extrae un archivo .tar.gz", "description_en": "Extract a .tar.gz archive"},
    {"command": f"{Color.GREEN}tar{Color.RESET} -xjf archive.tar.bz2", "description": "Extrae un archivo .tar.bz2", "description_en": "Extract a .tar.bz2 archive"},
    {"command": f"{Color.GREEN}tar{Color.RESET} -xJf archive.tar.xz", "description": "Extrae un archivo .tar.xz", "description_en": "Extract a .tar.xz archive"},
    {"command": f"{Color.GREEN}tar{Color.RESET} -xzf archive.tar.gz -C /dest/", "description": "Extrae en el directorio especificado", "description_en": "Extract to the specified directory"},
    {"command": f"{Color.GREEN}tar{Color.RESET} -tzf archive.tar.gz", "description": "Lista el contenido sin extraer", "description_en": "List archive contents without extracting"},
    {"command": f"{Color.GREEN}tar{Color.RESET} -czf archive.tar.gz --exclude='*.log' dir/", "description": "Crea un archivo excluyendo ciertos archivos", "description_en": "Create archive excluding certain files"},
    {"command": f"{Color.GREEN}tar{Color.RESET} -czf archive.tar.gz -C /parent/ subdir/", "description": "Crea un archivo desde un directorio padre", "description_en": "Create archive relative to a parent directory"},
    {"command": f"{Color.GREEN}tar{Color.RESET} --append -f archive.tar file.txt", "description": "Añade un archivo a un tar existente", "description_en": "Append a file to an existing tar archive"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
