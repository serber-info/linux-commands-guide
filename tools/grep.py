
# Configuración de colores
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

grep_commands = [
    {"command": f"{GREEN}grep {RESET}{YELLOW}'palabra' {RESET}filename", "description": "Busca líneas que contengan 'palabra' en el archivo 'filename'"},
    {"command": f"{GREEN}grep {RESET}-i {YELLOW}'palabra' {RESET}filename", "description": "Busca líneas que contengan 'palabra', ignorando mayúsculas/minúsculas"},
    {"command": f"{GREEN}grep {RESET}-v {YELLOW}'palabra' {RESET}filename", "description": "Muestra todas las líneas que NO contienen 'palabra'"},
    {"command": f"{GREEN}grep {RESET}-w {YELLOW}'palabra' {RESET}filename", "description": "Busca coincidencias exactas de 'palabra' como palabra completa"},
    {"command": f"{GREEN}grep {RESET}-x {YELLOW}'palabra' {RESET}filename", "description": "Muestra líneas que coinciden exactamente con 'palabra'"},
    {"command": f"{GREEN}grep {RESET}-c {YELLOW}'palabra' {RESET}filename", "description": "Cuenta las líneas que contienen 'palabra'"},
    {"command": f"{GREEN}grep {RESET}-l {YELLOW}'palabra' {RESET}*", "description": "Lista archivos que contienen 'palabra'"},
    {"command": f"{GREEN}grep {RESET}-L {YELLOW}'palabra' {RESET}*", "description": "Lista archivos que NO contienen 'palabra'"},
    {"command": f"{GREEN}grep {RESET}-n {YELLOW}'palabra' {RESET}filename", "description": "Muestra líneas con 'palabra' junto con su número de línea"},
    {"command": f"{GREEN}grep {RESET}-A NUM {YELLOW}'palabra' {RESET}filename", "description": "Muestra 'NUM' líneas después de la línea coincidente"},
    {"command": f"{GREEN}grep {RESET}-B NUM {YELLOW}'palabra' {RESET}filename", "description": "Muestra 'NUM' líneas antes de la línea coincidente"},
    {"command": f"{GREEN}grep {RESET}-C NUM {YELLOW}'palabra' {RESET}filename", "description": "Muestra 'NUM' líneas alrededor de la línea coincidente"},
    {"command": f"{GREEN}grep {RESET}--color {YELLOW}'palabra' {RESET}filename", "description": "Resalta 'palabra' en el resultado con color"},
    {"command": f"{GREEN}grep {RESET}-E {YELLOW}'palabra1|palabra2' {RESET}filename", "description": "Usa expresiones regulares extendidas para buscar 'palabra1' o 'palabra2'"},
    {"command": f"{GREEN}grep {RESET}-f {YELLOW}palabras.txt {RESET}filename", "description": "Usa patrones de búsqueda desde un archivo"},
    {"command": f"{GREEN}grep {RESET}-o {YELLOW}'palabra' {RESET}filename", "description": "Muestra solo la coincidencia exacta de 'palabra'"},
    {"command": f"{GREEN}grep {RESET}-q {YELLOW}'palabra' {RESET}filename", "description": "Silenciosamente, devuelve éxito o falla si encuentra 'palabra'"},
    {"command": f"{GREEN}grep {RESET}-s {YELLOW}'palabra' {RESET}filename", "description": "No muestra mensajes de error en archivos inexistentes o inaccesibles"},
    {"command": f"{GREEN}grep {RESET}-R {YELLOW}'palabra' {RESET}directory", "description": "Busca recursivamente en todos los archivos dentro del directorio"},
    {"command": f"{GREEN}grep {RESET}-m NUM {YELLOW}'palabra' {RESET}filename", "description": "Muestra solo las primeras 'NUM' coincidencias"},
    {"command": f"{GREEN}grep {RESET}--exclude={YELLOW}'*.log' 'palabra' {RESET}directory", "description": "Excluye archivos que coincidan con el patrón especificado"},
    {"command": f"{GREEN}grep {RESET}--include={YELLOW}'*.txt' 'palabra' {RESET}directory", "description": "Incluye solo archivos que coincidan con el patrón especificado"},
    {"command": f"{GREEN}grep {RESET}-Z {YELLOW}'palabra' {RESET}filename", "description": "Imprime un carácter NULL después del nombre del archivo (para uso con xargs)"},
    {"command": f"{GREEN}grep {RESET}--line-buffered {YELLOW}'palabra' {RESET}filename", "description": "Procesa línea por línea en lugar de en bloques, útil en tiempo real"},
    {"command": f"{GREEN}grep {RESET}--binary-files=text {YELLOW}'palabra' {RESET}filename", "description": "Considera archivos binarios como texto (evita omisión de archivos binarios)"},
    {"command": f"{GREEN}grep {RESET}-P {YELLOW}'palabra' {RESET}filename", "description": "Usa expresiones regulares Perl (PCRE) en 'palabra'"},
    {"command": f"{GREEN}grep {RESET}{YELLOW}'\\bpalabra\\b' {RESET}filename", "description": "Busca 'palabra' como una palabra completa usando límites de palabra"},
    {"command": f"{GREEN}grep {RESET}{YELLOW}'palabra$' {RESET}filename", "description": "Busca líneas que terminen con 'palabra'"},
    {"command": f"{GREEN}grep {RESET}{YELLOW}'^palabra' {RESET}filename", "description": "Busca líneas que comiencen con 'palabra'"},
]

print(f"\nOpciones de GREP con ejemplos y descripciones:\n")
print(f"{'Comando':<47} | {'Descripción'}")
print("-" * 125)
for cmd in grep_commands:
    command = cmd["command"]
    description = f"{RED}{cmd['description']}{RESET}"
    print(f"{command:<65} | {description}")

