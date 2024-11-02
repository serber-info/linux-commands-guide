from shellcolorize import Color

git_commands = [
    {"section": "Repository Management"},
    {"command": f"{Color.GREEN}git{Color.RESET} init", "description": "Crea un nuevo repositorio Git en el directorio actual"},
    {"command": f"{Color.GREEN}git{Color.RESET} clone URL", "description": "Clona un repositorio desde la URL especificada"},
    {"command": f"{Color.GREEN}git{Color.RESET} remote add origin URL", "description": "Asocia el repositorio remoto llamado 'origin' a la URL dada"},
    {"command": f"{Color.GREEN}git{Color.RESET} remote -v", "description": "Muestra los repositorios remotos asociados"},

    {"section": "Staging and Committing"},
    {"command": f"{Color.GREEN}git{Color.RESET} add filename", "description": "Agrega un archivo al área de preparación (staging)"},
    {"command": f"{Color.GREEN}git{Color.RESET} add .", "description": "Agrega todos los cambios en el directorio actual al área de preparación"},
    {"command": f"{Color.GREEN}git{Color.RESET} commit -m {Color.YELLOW}'message'{Color.RESET}                       ", "description": "Realiza un commit con el mensaje especificado"},
    {"command": f"{Color.GREEN}git{Color.RESET} commit -am {Color.YELLOW}'message'{Color.RESET}                      ", "description": "Agrega y realiza commit de todos los cambios rastreados en un solo paso"},
    {"command": f"{Color.GREEN}git{Color.RESET} commit --amend", "description": "Modifica el último commit, manteniendo el mensaje previo o cambiándolo"},

    {"section": "Branching"},
    {"command": f"{Color.GREEN}git{Color.RESET} branch branch_name", "description": "Crea una nueva rama llamada 'branch_name'"},
    {"command": f"{Color.GREEN}git{Color.RESET} branch -d branch_name", "description": "Elimina la rama 'branch_name'"},
    {"command": f"{Color.GREEN}git{Color.RESET} branch -D branch_name", "description": "Fuerza la eliminación de la rama 'branch_name'"},
    {"command": f"{Color.GREEN}git{Color.RESET} branch -m old_name new_name", "description": "Renombra una rama existente"},
    {"command": f"{Color.GREEN}git{Color.RESET} branch -a", "description": "Muestra todas las ramas locales y remotas"},
    {"command": f"{Color.GREEN}git{Color.RESET} checkout branch_name", "description": "Cambia a la rama especificada"},
    {"command": f"{Color.GREEN}git{Color.RESET} checkout -b new_branch", "description": "Crea y cambia a una nueva rama"},

    {"section": "Merging and Rebasing"},
    {"command": f"{Color.GREEN}git{Color.RESET} merge branch_name", "description": "Fusiona la rama especificada en la rama actual"},
    {"command": f"{Color.GREEN}git{Color.RESET} rebase branch_name", "description": "Reaplica los commits de la rama actual en la rama especificada"},
    {"command": f"{Color.GREEN}git{Color.RESET} rebase --continue", "description": "Continúa un rebase después de resolver conflictos"},
    {"command": f"{Color.GREEN}git{Color.RESET} rebase --abort", "description": "Cancela un rebase en curso"},

    {"section": "Working with Remotes"},
    {"command": f"{Color.GREEN}git{Color.RESET} push origin branch_name", "description": "Envía los commits locales de 'branch_name' a 'origin'"},
    {"command": f"{Color.GREEN}git{Color.RESET} push origin --delete branch_name", "description": "Elimina una rama remota"},
    {"command": f"{Color.GREEN}git{Color.RESET} pull origin branch_name", "description": "Actualiza la rama actual desde 'origin'"},
    {"command": f"{Color.GREEN}git{Color.RESET} fetch origin", "description": "Descarga actualizaciones de 'origin' sin fusionarlas"},
    {"command": f"{Color.GREEN}git{Color.RESET} fetch --all", "description": "Descarga actualizaciones de todos los repositorios remotos"},
    {"command": f"{Color.GREEN}git{Color.RESET} pull --rebase origin branch_name", "description": "Actualiza la rama actual con rebase desde 'origin'"},

    {"section": "Stashing"},
    {"command": f"{Color.GREEN}git{Color.RESET} stash", "description": "Guarda los cambios actuales sin realizar commit"},
    {"command": f"{Color.GREEN}git{Color.RESET} stash apply", "description": "Aplica el último stash sin eliminarlo"},
    {"command": f"{Color.GREEN}git{Color.RESET} stash pop", "description": "Aplica y elimina el último stash"},
    {"command": f"{Color.GREEN}git{Color.RESET} stash list", "description": "Muestra una lista de todos los stashes guardados"},
    {"command": f"{Color.GREEN}git{Color.RESET} stash drop stash@{{0}}", "description": "Elimina un stash específico"},

    {"section": "Viewing and Logging"},
    {"command": f"{Color.GREEN}git{Color.RESET} status", "description": "Muestra el estado actual del repositorio"},
    {"command": f"{Color.GREEN}git{Color.RESET} log", "description": "Muestra el historial de commits"},
    {"command": f"{Color.GREEN}git{Color.RESET} log --oneline", "description": "Muestra el historial de commits en una sola línea"},
    {"command": f"{Color.GREEN}git{Color.RESET} log -p", "description": "Muestra el historial de commits con diferencias"},
    {"command": f"{Color.GREEN}git{Color.RESET} diff", "description": "Muestra los cambios sin realizar commit"},
    {"command": f"{Color.GREEN}git{Color.RESET} diff HEAD", "description": "Muestra los cambios entre el directorio de trabajo y el último commit"},
    {"command": f"{Color.GREEN}git{Color.RESET} show commit_id", "description": "Muestra los detalles de un commit específico"},

    {"section": "Undoing Changes"},
    {"command": f"{Color.GREEN}git{Color.RESET} reset HEAD filename", "description": "Quita un archivo del área de preparación"},
    {"command": f"{Color.GREEN}git{Color.RESET} reset --soft HEAD~1", "description": "Deshace el último commit pero mantiene los cambios en staging"},
    {"command": f"{Color.GREEN}git{Color.RESET} reset --hard HEAD~1", "description": "Deshace el último commit y elimina los cambios"},

    {"section": "Configuration"},
    {"command": f"{Color.GREEN}git{Color.RESET} config --global user.name {Color.YELLOW}'name'{Color.RESET}          ", "description": "Establece el nombre del usuario a nivel global"},
    {"command": f"{Color.GREEN}git{Color.RESET} config --global user.email {Color.YELLOW}'email'{Color.RESET}        ", "description": "Establece el email del usuario a nivel global"},
    {"command": f"{Color.GREEN}git{Color.RESET} config --list", "description": "Muestra toda la configuración actual de Git"},
    {"command": f"{Color.GREEN}git{Color.RESET} config --global alias.co {Color.YELLOW}'checkout'{Color.RESET}       ", "description": "Crea un alias 'co' para el comando 'checkout'"},

    {"section": "Tagging"},
    {"command": f"{Color.GREEN}git{Color.RESET} tag tag_name", "description": "Crea una etiqueta (tag) en el último commit"},
    {"command": f"{Color.GREEN}git{Color.RESET} tag -a tag_name -m {Color.YELLOW}'message'{Color.RESET}              ", "description": "Crea una etiqueta anotada con un mensaje"},
    {"command": f"{Color.GREEN}git{Color.RESET} tag -d tag_name", "description": "Elimina una etiqueta local"},
    {"command": f"{Color.GREEN}git{Color.RESET} push origin tag_name", "description": "Envía una etiqueta al repositorio remoto"},
    {"command": f"{Color.GREEN}git{Color.RESET} push origin --tags", "description": "Envía todas las etiquetas locales al repositorio remoto"},
    {"command": f"{Color.GREEN}git{Color.RESET} push origin :refs/tags/tag_name", "description": "Elimina una etiqueta del repositorio remoto"},
]

print(f"\nComandos de GIT con ejemplos y descripciones:\n")
print(f"{'Comando':<46} | {'Descripción'}")
print("-" * 120)
for cmd in git_commands:
    if "section" in cmd:
        print(f"\n{Color.RED}{cmd['section']}{Color.RESET}\n" + "-" * 120)
    else:
        command = cmd["command"]
        description = f"{Color.RED}{cmd['description']}{Color.RESET}"
        print(f"{command:<55} | {description}")

