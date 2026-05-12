from shellcolorize import Color
from guia_linux.utils import print_table

TITLE = "Opciones de GIT"
TITLE_EN = "GIT Options"
BRIEF = "Control de versiones con Git"
BRIEF_EN = "Version control with Git"

COMMANDS = [
    {"section": "Gestión del repositorio", "section_en": "Repository Management"},
    {"command": f"{Color.GREEN}git{Color.RESET} init", "description": "Crea un nuevo repositorio Git", "description_en": "Create a new Git repository"},
    {"command": f"{Color.GREEN}git{Color.RESET} clone URL", "description": "Clona un repositorio desde la URL", "description_en": "Clone a repository from URL"},
    {"command": f"{Color.GREEN}git{Color.RESET} remote add origin URL", "description": "Asocia el remoto 'origin' a la URL", "description_en": "Associate remote 'origin' with URL"},
    {"command": f"{Color.GREEN}git{Color.RESET} remote -v", "description": "Muestra los remotos asociados", "description_en": "Show associated remotes"},

    {"section": "Staging y commits", "section_en": "Staging and Commits"},
    {"command": f"{Color.GREEN}git{Color.RESET} add filename", "description": "Añade un archivo al área de staging", "description_en": "Add a file to the staging area"},
    {"command": f"{Color.GREEN}git{Color.RESET} add .", "description": "Añade todos los cambios al staging", "description_en": "Stage all current changes"},
    {"command": f"{Color.GREEN}git{Color.RESET} commit -m 'message'", "description": "Realiza un commit con el mensaje dado", "description_en": "Commit with the given message"},
    {"command": f"{Color.GREEN}git{Color.RESET} commit -am 'message'", "description": "Añade y hace commit en un solo paso", "description_en": "Stage tracked changes and commit in one step"},
    {"command": f"{Color.GREEN}git{Color.RESET} commit --amend", "description": "Modifica el último commit", "description_en": "Amend the last commit"},

    {"section": "Ramas", "section_en": "Branching"},
    {"command": f"{Color.GREEN}git{Color.RESET} branch branch_name", "description": "Crea una nueva rama", "description_en": "Create a new branch"},
    {"command": f"{Color.GREEN}git{Color.RESET} branch -d branch_name", "description": "Elimina una rama", "description_en": "Delete a branch"},
    {"command": f"{Color.GREEN}git{Color.RESET} branch -a", "description": "Lista ramas locales y remotas", "description_en": "List all local and remote branches"},
    {"command": f"{Color.GREEN}git{Color.RESET} checkout branch_name", "description": "Cambia a la rama especificada", "description_en": "Switch to the specified branch"},
    {"command": f"{Color.GREEN}git{Color.RESET} checkout -b new_branch", "description": "Crea y cambia a una nueva rama", "description_en": "Create and switch to a new branch"},
    {"command": f"{Color.GREEN}git{Color.RESET} switch branch_name", "description": "Cambia de rama (comando moderno)", "description_en": "Switch branches (modern command)"},

    {"section": "Merge y Rebase", "section_en": "Merge and Rebase"},
    {"command": f"{Color.GREEN}git{Color.RESET} merge branch_name", "description": "Fusiona la rama en la rama actual", "description_en": "Merge branch into current branch"},
    {"command": f"{Color.GREEN}git{Color.RESET} rebase branch_name", "description": "Reaplica commits sobre la rama base", "description_en": "Reapply commits onto base branch"},
    {"command": f"{Color.GREEN}git{Color.RESET} rebase --continue", "description": "Continúa un rebase tras resolver conflictos", "description_en": "Continue rebase after resolving conflicts"},
    {"command": f"{Color.GREEN}git{Color.RESET} rebase --abort", "description": "Cancela un rebase en curso", "description_en": "Abort an in-progress rebase"},

    {"section": "Remotos", "section_en": "Working with Remotes"},
    {"command": f"{Color.GREEN}git{Color.RESET} push origin branch_name", "description": "Envía commits al remoto", "description_en": "Push commits to remote"},
    {"command": f"{Color.GREEN}git{Color.RESET} pull origin branch_name", "description": "Actualiza la rama desde el remoto", "description_en": "Pull and merge from remote"},
    {"command": f"{Color.GREEN}git{Color.RESET} fetch origin", "description": "Descarga cambios del remoto sin fusionarlos", "description_en": "Fetch remote changes without merging"},

    {"section": "Stash", "section_en": "Stashing"},
    {"command": f"{Color.GREEN}git{Color.RESET} stash", "description": "Guarda los cambios actuales sin commit", "description_en": "Save current changes without committing"},
    {"command": f"{Color.GREEN}git{Color.RESET} stash pop", "description": "Aplica y elimina el último stash", "description_en": "Apply and remove the last stash"},
    {"command": f"{Color.GREEN}git{Color.RESET} stash list", "description": "Lista todos los stashes guardados", "description_en": "List all saved stashes"},

    {"section": "Historial y estado", "section_en": "Log and Status"},
    {"command": f"{Color.GREEN}git{Color.RESET} status", "description": "Muestra el estado del repositorio", "description_en": "Show repository status"},
    {"command": f"{Color.GREEN}git{Color.RESET} log --oneline", "description": "Muestra el historial en una línea por commit", "description_en": "Show one-line commit history"},
    {"command": f"{Color.GREEN}git{Color.RESET} diff", "description": "Muestra cambios sin commit", "description_en": "Show uncommitted changes"},
    {"command": f"{Color.GREEN}git{Color.RESET} show commit_id", "description": "Muestra detalles de un commit específico", "description_en": "Show details of a specific commit"},

    {"section": "Deshacer cambios", "section_en": "Undoing Changes"},
    {"command": f"{Color.GREEN}git{Color.RESET} reset --soft HEAD~1", "description": "Deshace el último commit manteniendo los cambios en staging", "description_en": "Undo last commit, keep changes staged"},
    {"command": f"{Color.GREEN}git{Color.RESET} reset --hard HEAD~1", "description": "Deshace el último commit y elimina los cambios", "description_en": "Undo last commit and discard changes"},
    {"command": f"{Color.GREEN}git{Color.RESET} restore filename", "description": "Descarta cambios en el archivo de trabajo", "description_en": "Discard working-tree changes in file"},
]


def show(lang: str = "es") -> None:
    title = TITLE_EN if lang == "en" else TITLE
    print_table(title, COMMANDS, lang)
