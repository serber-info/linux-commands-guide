from shellcolorize import Color

# Define system logs
system_logs = [
    {"category": f"{Color.RED}Logs de Sistema{Color.RESET}", "logfile": "", "description": ""},
    {"logfile": f"{Color.GREEN}/var/log/syslog{Color.RESET}", "description": f"{Color.RED}Log principal de mensajes del sistema en distribuciones como Ubuntu y Debian; contiene información general del sistema{Color.RESET}"},
    {"logfile": f"{Color.GREEN}/var/log/messages{Color.RESET}", "description": f"{Color.RED}Log principal de mensajes en sistemas CentOS/RHEL, similar a syslog en Debian/Ubuntu{Color.RESET}"},
    {"logfile": f"{Color.GREEN}/var/log/kern.log{Color.RESET}", "description": f"{Color.RED}Contiene mensajes específicos del kernel, incluyendo errores y advertencias{Color.RESET}"},
    {"logfile": f"{Color.GREEN}/var/log/auth.log{Color.RESET}", "description": f"{Color.RED}Log de autenticaciones y autorizaciones, registra accesos exitosos y fallidos{Color.RESET}"},
    {"logfile": f"{Color.GREEN}/var/log/secure{Color.RESET}", "description": f"{Color.RED}Equivalente a auth.log en sistemas RHEL/CentOS, registra intentos de autenticación{Color.RESET}"},
    {"logfile": f"{Color.GREEN}/var/log/cron.log{Color.RESET}", "description": f"{Color.RED}Log de todas las tareas de cron que se ejecutan en el sistema{Color.RESET}"},
    {"logfile": f"{Color.GREEN}/var/log/audit/audit.log{Color.RESET}", "description": f"{Color.RED}Contiene información detallada de eventos auditados, especialmente para configuraciones de seguridad{Color.RESET}"},
    {"logfile": f"{Color.GREEN}/var/log/boot.log{Color.RESET}", "description": f"{Color.RED}Log de todos los mensajes de arranque generados durante la secuencia de inicio del sistema{Color.RESET}"},
    {"logfile": f"{Color.GREEN}/var/log/dmesg{Color.RESET}", "description": f"{Color.RED}Log de mensajes de diagnóstico del kernel, contiene información de hardware y errores de inicialización{Color.RESET}"},
    {"logfile": f"{Color.GREEN}/var/log/faillog{Color.RESET}", "description": f"{Color.RED}Registra los intentos de inicio de sesión fallidos y bloqueos de cuentas{Color.RESET}"},
    {"logfile": f"{Color.GREEN}/var/log/lastlog{Color.RESET}", "description": f"{Color.RED}Muestra la última vez que cada usuario inició sesión exitosamente en el sistema{Color.RESET}"},
    {"logfile": f"{Color.GREEN}/var/log/wtmp{Color.RESET}", "description": f"{Color.RED}Log binario de todos los inicios y cierres de sesión{Color.RESET}"},
    {"logfile": f"{Color.GREEN}/var/log/btmp{Color.RESET}", "description": f"{Color.RED}Log binario de intentos de inicio de sesión fallidos{Color.RESET}"},
]

# Define service logs with additional services
service_logs = [
    {"category": f"{Color.RED}Logs de Servidores Web{Color.RESET}", "logfile": "", "description": ""},
    {"logfile": f"{Color.GREEN}Apache: {Color.RESET}/var/log/apache2/access.log{Color.RESET}", "description": f"{Color.RED}Log de accesos para Apache HTTP Server en sistemas basados en Debian{Color.RESET}"},
    {"logfile": f"{Color.GREEN}Apache: {Color.RESET}/var/log/apache2/error.log{Color.RESET}", "description": f"{Color.RED}Log de errores de Apache, incluyendo fallos en la carga de archivos y errores de configuración{Color.RESET}"},
    {"logfile": f"{Color.GREEN}Nginx: {Color.RESET}/var/log/nginx/access.log{Color.RESET}", "description": f"{Color.RED}Log de accesos para el servidor Nginx{Color.RESET}"},
    {"logfile": f"{Color.GREEN}Nginx: {Color.RESET}/var/log/nginx/error.log{Color.RESET}", "description": f"{Color.RED}Log de errores de Nginx{Color.RESET}"},

    {"category": f"{Color.RED}Logs de Servidores de Base de Datos{Color.RESET}", "logfile": "", "description": ""},
    {"logfile": f"{Color.GREEN}MySQL: {Color.RESET}/var/log/mysql/mysql.log{Color.RESET}", "description": f"{Color.RED}Log principal de MySQL que contiene eventos generales y errores de la base de datos{Color.RESET}"},
    {"logfile": f"{Color.GREEN}MySQL: {Color.RESET}/var/log/mysql/error.log{Color.RESET}", "description": f"{Color.RED}Log de errores específicos de MySQL{Color.RESET}"},
    {"logfile": f"{Color.GREEN}Postgre: {Color.RESET}/var/log/postgresql/xxx-main.log{Color.RESET}", "description": f"{Color.RED}Log de accesos y errores de PostgreSQL, donde <version> es la versión instalada{Color.RESET}"},

    {"category": f"{Color.RED}Logs de Autenticación y Seguridad{Color.RESET}", "logfile": "", "description": ""},
    {"logfile": f"{Color.GREEN}Auth: {Color.RESET}/var/log/auth.log{Color.RESET}", "description": f"{Color.RED}Log de autenticaciones en Debian/Ubuntu, registra accesos de OpenSSH y otros servicios{Color.RESET}"},
    {"logfile": f"{Color.GREEN}Secure: {Color.RESET}/var/log/secure{Color.RESET}", "description": f"{Color.RED}Log de autenticaciones, utilizado por servicios como OpenSSH para registrar accesos en CentOS/RHEL{Color.RESET}"},

    {"category": f"{Color.RED}Logs de Administración del Sistema{Color.RESET}", "logfile": "", "description": ""},
    {"logfile": f"{Color.GREEN}Systemd: {Color.RESET}/var/log/journal/{Color.RESET}", "description": f"{Color.RED}Directorio que contiene registros binarios de systemd, accesible con el comando 'journalctl'{Color.RESET}"},
    {"logfile": f"{Color.GREEN}Syssat: {Color.RESET}/var/log/sysstat/sa{Color.RESET}", "description": f"{Color.RED}Logs de sysstat para estadísticas de rendimiento y uso del sistema{Color.RESET}"},

    {"category": f"{Color.RED}Logs de PHP y PHP-FPM{Color.RESET}", "logfile": "", "description": ""},
    {"logfile": f"{Color.GREEN}Php-Fpm: {Color.RESET}/var/log/php7.4-fpm.log{Color.RESET}", "description": f"{Color.RED}Log de errores y advertencias de PHP-FPM (FastCGI Process Manager){Color.RESET}"},
    {"logfile": f"{Color.GREEN}Php: {Color.RESET}/var/log/php_errors.log{Color.RESET}", "description": f"{Color.RED}Log general de errores de PHP{Color.RESET}"},

    {"category": f"{Color.RED}Logs de Servicios de Correo{Color.RESET}", "logfile": "", "description": ""},
    {"logfile": f"{Color.GREEN}Postfix: {Color.RESET}/var/log/mail.log{Color.RESET}", "description": f"{Color.RED}Log principal para eventos de correo electrónico, incluyendo Postfix y otros servicios de correo{Color.RESET}"},
    {"logfile": f"{Color.GREEN}Postfix: {Color.RESET}/var/log/mail.err{Color.RESET}", "description": f"{Color.RED}Log de errores específicos para servicios de correo{Color.RESET}"},

    {"category": f"{Color.RED}Logs de Docker{Color.RESET}", "logfile": "", "description": ""},
    {"logfile": f"{Color.GREEN}Docker: {Color.RESET}/var/log/docker.log{Color.RESET}", "description": f"{Color.RED}Log de eventos y errores de Docker{Color.RESET}"},

    {"category": f"{Color.RED}Logs de Firewalls{Color.RESET}", "logfile": "", "description": ""},
    {"logfile": f"{Color.GREEN}Firewalld: {Color.RESET}/var/log/firewalld{Color.RESET}", "description": f"{Color.RED}Logs del firewall firewalld en sistemas compatibles{Color.RESET}"},
    {"logfile": f"{Color.GREEN}UFW: {Color.RESET}/var/log/ufw.log{Color.RESET}", "description": f"{Color.RED}Log de eventos del firewall UFW (Uncomplicated Firewall){Color.RESET}"},

    {"category": f"{Color.RED}Logs de Samba (Compartición de Archivos){Color.RESET}", "logfile": "", "description": ""},
    {"logfile": f"{Color.GREEN}Samba: {Color.RESET}/var/log/samba/log.smbd{Color.RESET}", "description": f"{Color.RED}Log de eventos y errores del servicio de compartición de archivos Samba{Color.RESET}"},
    {"logfile": f"{Color.GREEN}Samba: {Color.RESET}/var/log/samba/log.nmbd{Color.RESET}", "description": f"{Color.RED}Log de eventos de NMB (NetBIOS Name Service) de Samba{Color.RESET}"},

    {"category": f"{Color.RED}Logs de Servicios FTP (vsftpd){Color.RESET}", "logfile": "", "description": ""},
    {"logfile": f"{Color.GREEN}FTP: {Color.RESET}/var/log/vsftpd.log{Color.RESET}", "description": f"{Color.RED}Log de accesos y eventos del servicio FTP vsftpd{Color.RESET}"},
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
