
# Configuración de colores
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

git_commands = [
    {"section": "Repository Management"},
    {"command": f"{GREEN}git{RESET} init", "description": "Crea un nuevo repositorio Git en el directorio actual"},
    {"command": f"{GREEN}git{RESET} clone URL", "description": "Clona un repositorio desde la URL especificada"},
    {"command": f"{GREEN}git{RESET} remote add origin URL", "description": "Asocia el repositorio remoto llamado 'origin' a la URL dada"},
    {"command": f"{GREEN}git{RESET} remote -v", "description": "Muestra los repositorios remotos asociados"},

    {"section": "Staging and Committing"},
    {"command": f"{GREEN}git{RESET} add filename", "description": "Agrega un archivo al área de preparación (staging)"},
    {"command": f"{GREEN}git{RESET} add .", "description": "Agrega todos los cambios en el directorio actual al área de preparación"},
    {"command": f"{GREEN}git{RESET} commit -m {YELLOW}'message'{RESET}                       ", "description": "Realiza un commit con el mensaje especificado"},
    {"command": f"{GREEN}git{RESET} commit -am {YELLOW}'message'{RESET}                      ", "description": "Agrega y realiza commit de todos los cambios rastreados en un solo paso"},
    {"command": f"{GREEN}git{RESET} commit --amend", "description": "Modifica el último commit, manteniendo el mensaje previo o cambiándolo"},

    {"section": "Branching"},
    {"command": f"{GREEN}git{RESET} branch branch_name", "description": "Crea una nueva rama llamada 'branch_name'"},
    {"command": f"{GREEN}git{RESET} branch -d branch_name", "description": "Elimina la rama 'branch_name'"},
    {"command": f"{GREEN}git{RESET} branch -D branch_name", "description": "Fuerza la eliminación de la rama 'branch_name'"},
    {"command": f"{GREEN}git{RESET} branch -m old_name new_name", "description": "Renombra una rama existente"},
    {"command": f"{GREEN}git{RESET} branch -a", "description": "Muestra todas las ramas locales y remotas"},
    {"command": f"{GREEN}git{RESET} checkout branch_name", "description": "Cambia a la rama especificada"},
    {"command": f"{GREEN}git{RESET} checkout -b new_branch", "description": "Crea y cambia a una nueva rama"},

    {"section": "Merging and Rebasing"},
    {"command": f"{GREEN}git{RESET} merge branch_name", "description": "Fusiona la rama especificada en la rama actual"},
    {"command": f"{GREEN}git{RESET} rebase branch_name", "description": "Reaplica los commits de la rama actual en la rama especificada"},
    {"command": f"{GREEN}git{RESET} rebase --continue", "description": "Continúa un rebase después de resolver conflictos"},
    {"command": f"{GREEN}git{RESET} rebase --abort", "description": "Cancela un rebase en curso"},

    {"section": "Working with Remotes"},
    {"command": f"{GREEN}git{RESET} push origin branch_name", "description": "Envía los commits locales de 'branch_name' a 'origin'"},
    {"command": f"{GREEN}git{RESET} push origin --delete branch_name", "description": "Elimina una rama remota"},
    {"command": f"{GREEN}git{RESET} pull origin branch_name", "description": "Actualiza la rama actual desde 'origin'"},
    {"command": f"{GREEN}git{RESET} fetch origin", "description": "Descarga actualizaciones de 'origin' sin fusionarlas"},
    {"command": f"{GREEN}git{RESET} fetch --all", "description": "Descarga actualizaciones de todos los repositorios remotos"},
    {"command": f"{GREEN}git{RESET} pull --rebase origin branch_name", "description": "Actualiza la rama actual con rebase desde 'origin'"},

    {"section": "Stashing"},
    {"command": f"{GREEN}git{RESET} stash", "description": "Guarda los cambios actuales sin realizar commit"},
    {"command": f"{GREEN}git{RESET} stash apply", "description": "Aplica el último stash sin eliminarlo"},
    {"command": f"{GREEN}git{RESET} stash pop", "description": "Aplica y elimina el último stash"},
    {"command": f"{GREEN}git{RESET} stash list", "description": "Muestra una lista de todos los stashes guardados"},
    {"command": f"{GREEN}git{RESET} stash drop stash@{{0}}", "description": "Elimina un stash específico"},

    {"section": "Viewing and Logging"},
    {"command": f"{GREEN}git{RESET} status", "description": "Muestra el estado actual del repositorio"},
    {"command": f"{GREEN}git{RESET} log", "description": "Muestra el historial de commits"},
    {"command": f"{GREEN}git{RESET} log --oneline", "description": "Muestra el historial de commits en una sola línea"},
    {"command": f"{GREEN}git{RESET} log -p", "description": "Muestra el historial de commits con diferencias"},
    {"command": f"{GREEN}git{RESET} diff", "description": "Muestra los cambios sin realizar commit"},
    {"command": f"{GREEN}git{RESET} diff HEAD", "description": "Muestra los cambios entre el directorio de trabajo y el último commit"},
    {"command": f"{GREEN}git{RESET} show commit_id", "description": "Muestra los detalles de un commit específico"},

    {"section": "Undoing Changes"},
    {"command": f"{GREEN}git{RESET} reset HEAD filename", "description": "Quita un archivo del área de preparación"},
    {"command": f"{GREEN}git{RESET} reset --soft HEAD~1", "description": "Deshace el último commit pero mantiene los cambios en staging"},
    {"command": f"{GREEN}git{RESET} reset --hard HEAD~1", "description": "Deshace el último commit y elimina los cambios"},

    {"section": "Configuration"},
    {"command": f"{GREEN}git{RESET} config --global user.name {YELLOW}'name'{RESET}          ", "description": "Establece el nombre del usuario a nivel global"},
    {"command": f"{GREEN}git{RESET} config --global user.email {YELLOW}'email'{RESET}        ", "description": "Establece el email del usuario a nivel global"},
    {"command": f"{GREEN}git{RESET} config --list", "description": "Muestra toda la configuración actual de Git"},
    {"command": f"{GREEN}git{RESET} config --global alias.co {YELLOW}'checkout'{RESET}       ", "description": "Crea un alias 'co' para el comando 'checkout'"},

    {"section": "Tagging"},
    {"command": f"{GREEN}git{RESET} tag tag_name", "description": "Crea una etiqueta (tag) en el último commit"},
    {"command": f"{GREEN}git{RESET} tag -a tag_name -m {YELLOW}'message'{RESET}              ", "description": "Crea una etiqueta anotada con un mensaje"},
    {"command": f"{GREEN}git{RESET} tag -d tag_name", "description": "Elimina una etiqueta local"},
    {"command": f"{GREEN}git{RESET} push origin tag_name", "description": "Envía una etiqueta al repositorio remoto"},
    {"command": f"{GREEN}git{RESET} push origin --tags", "description": "Envía todas las etiquetas locales al repositorio remoto"},
    {"command": f"{GREEN}git{RESET} push origin :refs/tags/tag_name", "description": "Elimina una etiqueta del repositorio remoto"},
]

print(f"\nComandos de GIT con ejemplos y descripciones:\n")
print(f"{'Comando':<46} | {'Descripción'}")
print("-" * 120)
for cmd in git_commands:
    if "section" in cmd:
        print(f"\n{RED}{cmd['section']}{RESET}\n" + "-" * 120)
    else:
        command = cmd["command"]
        description = f"{RED}{cmd['description']}{RESET}"
        print(f"{command:<55} | {description}")

