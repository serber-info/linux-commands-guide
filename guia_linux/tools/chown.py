from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de CHOWN"
TITLE_EN = "CHOWN Options"
BRIEF = "Cambia propietario y grupo de archivos"
BRIEF_EN = "Change file owner and group"

COMMANDS = [
    {"command": f"{Color.GREEN}chown{Color.RESET} user filename", "description": "Cambia el propietario a 'user'", "description_en": "Change owner to 'user'"},
    {"command": f"{Color.GREEN}chown{Color.RESET} user:group filename", "description": "Cambia propietario y grupo", "description_en": "Change owner and group"},
    {"command": f"{Color.GREEN}chown{Color.RESET} :group filename", "description": "Cambia solo el grupo", "description_en": "Change group only"},
    {"command": f"{Color.GREEN}chown{Color.RESET} -R user directory", "description": "Cambia propietario recursivamente", "description_en": "Change owner recursively"},
    {"command": f"{Color.GREEN}chown{Color.RESET} -R user:group directory", "description": "Cambia propietario y grupo recursivamente", "description_en": "Change owner and group recursively"},
    {"command": f"{Color.GREEN}chown{Color.RESET} --from=old_user:new_user filename", "description": "Cambia solo si coincide con el propietario actual", "description_en": "Change only if current owner matches"},
    {"command": f"{Color.GREEN}chown{Color.RESET} --reference=ref_file filename", "description": "Copia propietario y grupo de otro archivo", "description_en": "Copy owner and group from another file"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
