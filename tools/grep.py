from shellcolorize import Color

grep_commands = [
    {"command": f"{Color.GREEN}grep {Color.RESET}{Color.YELLOW}'palabra' {Color.RESET}filename", "description": "Busca líneas que contengan 'palabra' en el archivo 'filename'"},
    {"command": f"{Color.GREEN}grep {Color.RESET}-i {Color.YELLOW}'palabra' {Color.RESET}filename", "description": "Busca líneas que contengan 'palabra', ignorando mayúsculas/minúsculas"},
    {"command": f"{Color.GREEN}grep {Color.RESET}-v {Color.YELLOW}'palabra' {Color.RESET}filename", "description": "Muestra todas las líneas que NO contienen 'palabra'"},
    {"command": f"{Color.GREEN}grep {Color.RESET}-w {Color.YELLOW}'palabra' {Color.RESET}filename", "description": "Busca coincidencias exactas de 'palabra' como palabra completa"},
    {"command": f"{Color.GREEN}grep {Color.RESET}-x {Color.YELLOW}'palabra' {Color.RESET}filename", "description": "Muestra líneas que coinciden exactamente con 'palabra'"},
    {"command": f"{Color.GREEN}grep {Color.RESET}-c {Color.YELLOW}'palabra' {Color.RESET}filename", "description": "Cuenta las líneas que contienen 'palabra'"},
    {"command": f"{Color.GREEN}grep {Color.RESET}-l {Color.YELLOW}'palabra' {Color.RESET}*", "description": "Lista archivos que contienen 'palabra'"},
    {"command": f"{Color.GREEN}grep {Color.RESET}-L {Color.YELLOW}'palabra' {Color.RESET}*", "description": "Lista archivos que NO contienen 'palabra'"},
    {"command": f"{Color.GREEN}grep {Color.RESET}-n {Color.YELLOW}'palabra' {Color.RESET}filename", "description": "Muestra líneas con 'palabra' junto con su número de línea"},
    {"command": f"{Color.GREEN}grep {Color.RESET}-A NUM {Color.YELLOW}'palabra' {Color.RESET}filename", "description": "Muestra 'NUM' líneas después de la línea coincidente"},
    {"command": f"{Color.GREEN}grep {Color.RESET}-B NUM {Color.YELLOW}'palabra' {Color.RESET}filename", "description": "Muestra 'NUM' líneas antes de la línea coincidente"},
    {"command": f"{Color.GREEN}grep {Color.RESET}-C NUM {Color.YELLOW}'palabra' {Color.RESET}filename", "description": "Muestra 'NUM' líneas alrededor de la línea coincidente"},
    {"command": f"{Color.GREEN}grep {Color.RESET}--color {Color.YELLOW}'palabra' {Color.RESET}filename", "description": "Resalta 'palabra' en el resultado con color"},
    {"command": f"{Color.GREEN}grep {Color.RESET}-E {Color.YELLOW}'palabra1|palabra2' {Color.RESET}filename", "description": "Usa expresiones regulares extendidas para buscar 'palabra1' o 'palabra2'"},
    {"command": f"{Color.GREEN}grep {Color.RESET}-f {Color.YELLOW}palabras.txt {Color.RESET}filename", "description": "Usa patrones de búsqueda desde un archivo"},
    {"command": f"{Color.GREEN}grep {Color.RESET}-o {Color.YELLOW}'palabra' {Color.RESET}filename", "description": "Muestra solo la coincidencia exacta de 'palabra'"},
    {"command": f"{Color.GREEN}grep {Color.RESET}-q {Color.YELLOW}'palabra' {Color.RESET}filename", "description": "Silenciosamente, devuelve éxito o falla si encuentra 'palabra'"},
    {"command": f"{Color.GREEN}grep {Color.RESET}-s {Color.YELLOW}'palabra' {Color.RESET}filename", "description": "No muestra mensajes de error en archivos inexistentes o inaccesibles"},
    {"command": f"{Color.GREEN}grep {Color.RESET}-R {Color.YELLOW}'palabra' {Color.RESET}directory", "description": "Busca recursivamente en todos los archivos dentro del directorio"},
    {"command": f"{Color.GREEN}grep {Color.RESET}-m NUM {Color.YELLOW}'palabra' {Color.RESET}filename", "description": "Muestra solo las primeras 'NUM' coincidencias"},
    {"command": f"{Color.GREEN}grep {Color.RESET}--exclude={Color.YELLOW}'*.log' 'palabra' {Color.RESET}directory", "description": "Excluye archivos que coincidan con el patrón especificado"},
    {"command": f"{Color.GREEN}grep {Color.RESET}--include={Color.YELLOW}'*.txt' 'palabra' {Color.RESET}directory", "description": "Incluye solo archivos que coincidan con el patrón especificado"},
    {"command": f"{Color.GREEN}grep {Color.RESET}-Z {Color.YELLOW}'palabra' {Color.RESET}filename", "description": "Imprime un carácter NULL después del nombre del archivo (para uso con xargs)"},
    {"command": f"{Color.GREEN}grep {Color.RESET}--line-buffered {Color.YELLOW}'palabra' {Color.RESET}filename", "description": "Procesa línea por línea en lugar de en bloques, útil en tiempo real"},
    {"command": f"{Color.GREEN}grep {Color.RESET}--binary-files=text {Color.YELLOW}'palabra' {Color.RESET}filename", "description": "Considera archivos binarios como texto (evita omisión de archivos binarios)"},
    {"command": f"{Color.GREEN}grep {Color.RESET}-P {Color.YELLOW}'palabra' {Color.RESET}filename", "description": "Usa expresiones regulares Perl (PCRE) en 'palabra'"},
    {"command": f"{Color.GREEN}grep {Color.RESET}{Color.YELLOW}'\\bpalabra\\b' {Color.RESET}filename", "description": "Busca 'palabra' como una palabra completa usando límites de palabra"},
    {"command": f"{Color.GREEN}grep {Color.RESET}{Color.YELLOW}'palabra$' {Color.RESET}filename", "description": "Busca líneas que terminen con 'palabra'"},
    {"command": f"{Color.GREEN}grep {Color.RESET}{Color.YELLOW}'^palabra' {Color.RESET}filename", "description": "Busca líneas que comiencen con 'palabra'"},
]

print(f"\nOpciones de GREP con ejemplos y descripciones:\n")
print(f"{'Comando':<47} | {'Descripción'}")
print("-" * 125)
for cmd in grep_commands:
    command = cmd["command"]
    description = f"{Color.RED}{cmd['description']}{Color.RESET}"
    print(f"{command:<65} | {description}")

