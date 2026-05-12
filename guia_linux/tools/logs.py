from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Ubicaciones de Logs del Sistema"
TITLE_EN = "System Log Locations"
BRIEF = "Rutas de logs importantes en Linux"
BRIEF_EN = "Important log file paths in Linux"

COMMANDS = [
    {"category": "Logs de Sistema", "category_en": "System Logs"},
    {"logfile": f"{Color.GREEN}/var/log/syslog{Color.RESET}", "description": "Log principal del sistema (Debian/Ubuntu)", "description_en": "Main system log (Debian/Ubuntu)"},
    {"logfile": f"{Color.GREEN}/var/log/messages{Color.RESET}", "description": "Log principal del sistema (RHEL/CentOS)", "description_en": "Main system log (RHEL/CentOS)"},
    {"logfile": f"{Color.GREEN}/var/log/kern.log{Color.RESET}", "description": "Mensajes del kernel", "description_en": "Kernel messages"},
    {"logfile": f"{Color.GREEN}/var/log/auth.log{Color.RESET}", "description": "Autenticaciones y accesos (Debian/Ubuntu)", "description_en": "Authentication and access log (Debian/Ubuntu)"},
    {"logfile": f"{Color.GREEN}/var/log/secure{Color.RESET}", "description": "Autenticaciones y accesos (RHEL/CentOS)", "description_en": "Authentication and access log (RHEL/CentOS)"},
    {"logfile": f"{Color.GREEN}/var/log/cron.log{Color.RESET}", "description": "Log de tareas cron", "description_en": "Cron job log"},
    {"logfile": f"{Color.GREEN}/var/log/audit/audit.log{Color.RESET}", "description": "Eventos auditados del sistema", "description_en": "Audited system events"},
    {"logfile": f"{Color.GREEN}/var/log/boot.log{Color.RESET}", "description": "Mensajes de arranque del sistema", "description_en": "System boot messages"},
    {"logfile": f"{Color.GREEN}/var/log/dmesg{Color.RESET}", "description": "Mensajes de diagnóstico del kernel", "description_en": "Kernel diagnostic messages"},
    {"logfile": f"{Color.GREEN}/var/log/faillog{Color.RESET}", "description": "Intentos de inicio de sesión fallidos", "description_en": "Failed login attempts"},
    {"logfile": f"{Color.GREEN}/var/log/lastlog{Color.RESET}", "description": "Último inicio de sesión de cada usuario", "description_en": "Last login for each user"},

    {"category": "Logs de Servidores Web", "category_en": "Web Server Logs"},
    {"logfile": f"{Color.GREEN}Apache: /var/log/apache2/access.log{Color.RESET}", "description": "Log de accesos de Apache (Debian)", "description_en": "Apache access log (Debian)"},
    {"logfile": f"{Color.GREEN}Apache: /var/log/apache2/error.log{Color.RESET}", "description": "Log de errores de Apache", "description_en": "Apache error log"},
    {"logfile": f"{Color.GREEN}Nginx: /var/log/nginx/access.log{Color.RESET}", "description": "Log de accesos de Nginx", "description_en": "Nginx access log"},
    {"logfile": f"{Color.GREEN}Nginx: /var/log/nginx/error.log{Color.RESET}", "description": "Log de errores de Nginx", "description_en": "Nginx error log"},

    {"category": "Logs de Bases de Datos", "category_en": "Database Logs"},
    {"logfile": f"{Color.GREEN}MySQL: /var/log/mysql/mysql.log{Color.RESET}", "description": "Log general de MySQL", "description_en": "MySQL general log"},
    {"logfile": f"{Color.GREEN}MySQL: /var/log/mysql/error.log{Color.RESET}", "description": "Log de errores de MySQL", "description_en": "MySQL error log"},
    {"logfile": f"{Color.GREEN}PostgreSQL: /var/log/postgresql/*.log{Color.RESET}", "description": "Logs de PostgreSQL", "description_en": "PostgreSQL logs"},

    {"category": "Logs de Servicios", "category_en": "Service Logs"},
    {"logfile": f"{Color.GREEN}Systemd: /var/log/journal/{Color.RESET}", "description": "Logs binarios de systemd (usar journalctl)", "description_en": "systemd binary logs (use journalctl)"},
    {"logfile": f"{Color.GREEN}Docker: /var/log/docker.log{Color.RESET}", "description": "Log de eventos de Docker", "description_en": "Docker event log"},
    {"logfile": f"{Color.GREEN}Postfix: /var/log/mail.log{Color.RESET}", "description": "Log de correo electrónico", "description_en": "Mail server log"},
    {"logfile": f"{Color.GREEN}FTP: /var/log/vsftpd.log{Color.RESET}", "description": "Log del servicio vsftpd", "description_en": "vsftpd FTP service log"},

    {"category": "Logs de Firewall", "category_en": "Firewall Logs"},
    {"logfile": f"{Color.GREEN}Firewalld: /var/log/firewalld{Color.RESET}", "description": "Log de firewalld", "description_en": "firewalld log"},
    {"logfile": f"{Color.GREEN}UFW: /var/log/ufw.log{Color.RESET}", "description": "Log de UFW (Uncomplicated Firewall)", "description_en": "UFW (Uncomplicated Firewall) log"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
