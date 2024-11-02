# Configuración de colores
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"


# Define system logs
system_logs = [
    {"category": f"{RED}Logs de Sistema{RESET}", "logfile": "", "description": ""},
    {"logfile": f"{GREEN}/var/log/syslog{RESET}", "description": f"{RED}Log principal de mensajes del sistema en distribuciones como Ubuntu y Debian; contiene información general del sistema{RESET}"},
    {"logfile": f"{GREEN}/var/log/messages{RESET}", "description": f"{RED}Log principal de mensajes en sistemas CentOS/RHEL, similar a syslog en Debian/Ubuntu{RESET}"},
    {"logfile": f"{GREEN}/var/log/kern.log{RESET}", "description": f"{RED}Contiene mensajes específicos del kernel, incluyendo errores y advertencias{RESET}"},
    {"logfile": f"{GREEN}/var/log/auth.log{RESET}", "description": f"{RED}Log de autenticaciones y autorizaciones, registra accesos exitosos y fallidos{RESET}"},
    {"logfile": f"{GREEN}/var/log/secure{RESET}", "description": f"{RED}Equivalente a auth.log en sistemas RHEL/CentOS, registra intentos de autenticación{RESET}"},
    {"logfile": f"{GREEN}/var/log/cron.log{RESET}", "description": f"{RED}Log de todas las tareas de cron que se ejecutan en el sistema{RESET}"},
    {"logfile": f"{GREEN}/var/log/audit/audit.log{RESET}", "description": f"{RED}Contiene información detallada de eventos auditados, especialmente para configuraciones de seguridad{RESET}"},
    {"logfile": f"{GREEN}/var/log/boot.log{RESET}", "description": f"{RED}Log de todos los mensajes de arranque generados durante la secuencia de inicio del sistema{RESET}"},
    {"logfile": f"{GREEN}/var/log/dmesg{RESET}", "description": f"{RED}Log de mensajes de diagnóstico del kernel, contiene información de hardware y errores de inicialización{RESET}"},
    {"logfile": f"{GREEN}/var/log/faillog{RESET}", "description": f"{RED}Registra los intentos de inicio de sesión fallidos y bloqueos de cuentas{RESET}"},
    {"logfile": f"{GREEN}/var/log/lastlog{RESET}", "description": f"{RED}Muestra la última vez que cada usuario inició sesión exitosamente en el sistema{RESET}"},
    {"logfile": f"{GREEN}/var/log/wtmp{RESET}", "description": f"{RED}Log binario de todos los inicios y cierres de sesión{RESET}"},
    {"logfile": f"{GREEN}/var/log/btmp{RESET}", "description": f"{RED}Log binario de intentos de inicio de sesión fallidos{RESET}"},
]

# Define service logs with additional services
service_logs = [
    {"category": f"{RED}Logs de Servidores Web{RESET}", "logfile": "", "description": ""},
    {"logfile": f"{GREEN}Apache: {RESET}/var/log/apache2/access.log{RESET}", "description": f"{RED}Log de accesos para Apache HTTP Server en sistemas basados en Debian{RESET}"},
    {"logfile": f"{GREEN}Apache: {RESET}/var/log/apache2/error.log{RESET}", "description": f"{RED}Log de errores de Apache, incluyendo fallos en la carga de archivos y errores de configuración{RESET}"},
    {"logfile": f"{GREEN}Nginx: {RESET}/var/log/nginx/access.log{RESET}", "description": f"{RED}Log de accesos para el servidor Nginx{RESET}"},
    {"logfile": f"{GREEN}Nginx: {RESET}/var/log/nginx/error.log{RESET}", "description": f"{RED}Log de errores de Nginx{RESET}"},

    {"category": f"{RED}Logs de Servidores de Base de Datos{RESET}", "logfile": "", "description": ""},
    {"logfile": f"{GREEN}MySQL: {RESET}/var/log/mysql/mysql.log{RESET}", "description": f"{RED}Log principal de MySQL que contiene eventos generales y errores de la base de datos{RESET}"},
    {"logfile": f"{GREEN}MySQL: {RESET}/var/log/mysql/error.log{RESET}", "description": f"{RED}Log de errores específicos de MySQL{RESET}"},
    {"logfile": f"{GREEN}Postgre: {RESET}/var/log/postgresql/xxx-main.log{RESET}", "description": f"{RED}Log de accesos y errores de PostgreSQL, donde <version> es la versión instalada{RESET}"},

    {"category": f"{RED}Logs de Autenticación y Seguridad{RESET}", "logfile": "", "description": ""},
    {"logfile": f"{GREEN}Auth: {RESET}/var/log/auth.log{RESET}", "description": f"{RED}Log de autenticaciones en Debian/Ubuntu, registra accesos de OpenSSH y otros servicios{RESET}"},
    {"logfile": f"{GREEN}Secure: {RESET}/var/log/secure{RESET}", "description": f"{RED}Log de autenticaciones, utilizado por servicios como OpenSSH para registrar accesos en CentOS/RHEL{RESET}"},

    {"category": f"{RED}Logs de Administración del Sistema{RESET}", "logfile": "", "description": ""},
    {"logfile": f"{GREEN}Systemd: {RESET}/var/log/journal/{RESET}", "description": f"{RED}Directorio que contiene registros binarios de systemd, accesible con el comando 'journalctl'{RESET}"},
    {"logfile": f"{GREEN}Syssat: {RESET}/var/log/sysstat/sa{RESET}", "description": f"{RED}Logs de sysstat para estadísticas de rendimiento y uso del sistema{RESET}"},

    {"category": f"{RED}Logs de PHP y PHP-FPM{RESET}", "logfile": "", "description": ""},
    {"logfile": f"{GREEN}Php-Fpm: {RESET}/var/log/php7.4-fpm.log{RESET}", "description": f"{RED}Log de errores y advertencias de PHP-FPM (FastCGI Process Manager){RESET}"},
    {"logfile": f"{GREEN}Php: {RESET}/var/log/php_errors.log{RESET}", "description": f"{RED}Log general de errores de PHP{RESET}"},

    {"category": f"{RED}Logs de Servicios de Correo{RESET}", "logfile": "", "description": ""},
    {"logfile": f"{GREEN}Postfix: {RESET}/var/log/mail.log{RESET}", "description": f"{RED}Log principal para eventos de correo electrónico, incluyendo Postfix y otros servicios de correo{RESET}"},
    {"logfile": f"{GREEN}Postfix: {RESET}/var/log/mail.err{RESET}", "description": f"{RED}Log de errores específicos para servicios de correo{RESET}"},

    {"category": f"{RED}Logs de Docker{RESET}", "logfile": "", "description": ""},
    {"logfile": f"{GREEN}Docker: {RESET}/var/log/docker.log{RESET}", "description": f"{RED}Log de eventos y errores de Docker{RESET}"},

    {"category": f"{RED}Logs de Firewalls{RESET}", "logfile": "", "description": ""},
    {"logfile": f"{GREEN}Firewalld: {RESET}/var/log/firewalld{RESET}", "description": f"{RED}Logs del firewall firewalld en sistemas compatibles{RESET}"},
    {"logfile": f"{GREEN}UFW: {RESET}/var/log/ufw.log{RESET}", "description": f"{RED}Log de eventos del firewall UFW (Uncomplicated Firewall){RESET}"},

    {"category": f"{RED}Logs de Samba (Compartición de Archivos){RESET}", "logfile": "", "description": ""},
    {"logfile": f"{GREEN}Samba: {RESET}/var/log/samba/log.smbd{RESET}", "description": f"{RED}Log de eventos y errores del servicio de compartición de archivos Samba{RESET}"},
    {"logfile": f"{GREEN}Samba: {RESET}/var/log/samba/log.nmbd{RESET}", "description": f"{RED}Log de eventos de NMB (NetBIOS Name Service) de Samba{RESET}"},

    {"category": f"{RED}Logs de Servicios FTP (vsftpd){RESET}", "logfile": "", "description": ""},
    {"logfile": f"{GREEN}FTP: {RESET}/var/log/vsftpd.log{RESET}", "description": f"{RED}Log de accesos y eventos del servicio FTP vsftpd{RESET}"},
]

# Print system logs
print(f"\nLogs de Sistema con Descripciones:\n")
print(f"{'Archivo de Log':<47} | {'Descripción'}")
print("-" * 168)
for log in system_logs:
    if "category" in log:
        print(f"\n{log['category']}\n" + "-" * 168)
    else:
        print(f"{log['logfile']:<56} | {log['description']}")

# Print service logs
print(f"\nLogs de Servicios Importantes:\n")
print(f"{'Archivo de Log':<47} | {'Descripción'}")
print("-" * 168)
for log in service_logs:
    if "category" in log:
        print(f"\n{log['category']}\n" + "-" * 168)
    else:
        print(f"{log['logfile']:<60} | {log['description']}")
