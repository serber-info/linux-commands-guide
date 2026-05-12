from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de CRONTAB"
TITLE_EN = "CRONTAB Options"
BRIEF = "Programación de tareas periódicas"
BRIEF_EN = "Periodic task scheduling"

COMMANDS = [
    {"section": "Gestión de crontab", "section_en": "Crontab Management"},
    {"command": f"{Color.GREEN}crontab{Color.RESET} -e", "description": "Edita el crontab del usuario actual", "description_en": "Edit the current user's crontab"},
    {"command": f"{Color.GREEN}crontab{Color.RESET} -l", "description": "Lista las tareas del crontab actual", "description_en": "List current crontab entries"},
    {"command": f"{Color.GREEN}crontab{Color.RESET} -r", "description": "Elimina el crontab del usuario actual", "description_en": "Remove the current user's crontab"},
    {"command": f"{Color.GREEN}crontab{Color.RESET} -u user -l", "description": "Lista el crontab de otro usuario (requiere root)", "description_en": "List another user's crontab (requires root)"},
    {"command": f"{Color.GREEN}crontab{Color.RESET} file.cron", "description": "Instala un crontab desde un archivo", "description_en": "Install a crontab from a file"},

    {"section": "Sintaxis de los campos  [min hora día mes día_semana]", "section_en": "Field Syntax  [min hour day month weekday]"},
    {"command": f"{Color.YELLOW}* * * * *{Color.RESET} command", "description": "Ejecuta cada minuto", "description_en": "Run every minute"},
    {"command": f"{Color.YELLOW}0 * * * *{Color.RESET} command", "description": "Ejecuta cada hora (al minuto 0)", "description_en": "Run every hour (at minute 0)"},
    {"command": f"{Color.YELLOW}0 0 * * *{Color.RESET} command", "description": "Ejecuta cada día a medianoche", "description_en": "Run every day at midnight"},
    {"command": f"{Color.YELLOW}0 9 * * 1{Color.RESET} command", "description": "Ejecuta cada lunes a las 9:00", "description_en": "Run every Monday at 9:00"},
    {"command": f"{Color.YELLOW}0 0 1 * *{Color.RESET} command", "description": "Ejecuta el primer día de cada mes", "description_en": "Run on the first day of every month"},
    {"command": f"{Color.YELLOW}*/15 * * * *{Color.RESET} command", "description": "Ejecuta cada 15 minutos", "description_en": "Run every 15 minutes"},
    {"command": f"{Color.YELLOW}0 8-18 * * 1-5{Color.RESET} command", "description": "Ejecuta cada hora de 8 a 18, de lunes a viernes", "description_en": "Run hourly from 8 to 18, Monday to Friday"},
    {"command": f"{Color.YELLOW}30 23 * * 0,6{Color.RESET} command", "description": "Ejecuta a las 23:30 los sábados y domingos", "description_en": "Run at 23:30 on Saturdays and Sundays"},

    {"section": "Variables especiales", "section_en": "Special Variables"},
    {"command": f"{Color.GREEN}MAILTO{Color.RESET}=user@example.com", "description": "Envía la salida por correo al usuario especificado", "description_en": "Send output by email to the specified user"},
    {"command": f"{Color.GREEN}PATH{Color.RESET}=/usr/local/bin:/usr/bin:/bin", "description": "Define el PATH para los comandos del crontab", "description_en": "Set PATH for crontab commands"},
    {"command": f"{Color.GREEN}@reboot{Color.RESET} command", "description": "Ejecuta el comando al arrancar el sistema", "description_en": "Run command at system boot"},
    {"command": f"{Color.GREEN}@hourly{Color.RESET} command", "description": "Alias de '0 * * * *'", "description_en": "Alias for '0 * * * *'"},
    {"command": f"{Color.GREEN}@daily{Color.RESET} command", "description": "Alias de '0 0 * * *'", "description_en": "Alias for '0 0 * * *'"},
    {"command": f"{Color.GREEN}@weekly{Color.RESET} command", "description": "Alias de '0 0 * * 0'", "description_en": "Alias for '0 0 * * 0'"},
    {"command": f"{Color.GREEN}@monthly{Color.RESET} command", "description": "Alias de '0 0 1 * *'", "description_en": "Alias for '0 0 1 * *'"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
