# linux-commands-guide — `lh`

[![CI](https://github.com/serber-info/linux-commands-guide/actions/workflows/ci.yml/badge.svg)](https://github.com/serber-info/linux-commands-guide/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/linux-commands-guide.svg)](https://badge.fury.io/py/linux-commands-guide)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Learn Linux from your terminal. Find a command, understand it, then practice.**

**Aprende Linux desde tu terminal. Encuentra un comando, entiéndelo y practica.**

`lh` is an offline Spanish/English quick reference for beginners, with advanced entries when you
need them. It displays examples; **it never executes them**. No account, telemetry or network
connection is needed after installation. It also works over SSH.

<p align="center">
  <img src="docs/demo.gif" alt="Real terminal demo: quick reference, task search, explanations, lessons, practice hints and English output" width="1000">
</p>

*Real CLI output / Salida real de la CLI. [Reproduce this recording / Reproducir la grabación](docs/demo.md).*

## Start here / Empieza aquí

```bash
lh ls --quick                 # A short reference / Referencia corta
lh grep --explain             # Explanation and sources / Explicación y fuentes
lh learn pipes                # Understand pipelines / Entiende las tuberías
lh practice grep              # A challenge with sample data / Reto con datos de ejemplo
lh practice grep --hint       # Hint / Pista
lh practice grep --solution   # Solution / Solución
```

Language follows your locale. Use `--lang es` or `--lang en` to choose explicitly.
El idioma se elige por tu locale. Puedes forzarlo con `--lang es` o `--lang en`.

## Install / Instalar

### From a checkout: one command / Desde el repo: un comando

Requires Linux, Python 3.9+ with `venv`/pip, and Internet access during installation.
Requiere Linux, Python 3.9+ con `venv`/pip y conexión durante la instalación.

```bash
git clone https://github.com/serber-info/linux-commands-guide.git
cd linux-commands-guide
./install.sh
```

The installer creates an isolated environment in `~/.local/share/linux-commands-guide/venv`
and a launcher in `~/.local/bin/lh`. **Do not use sudo.** It does not change system Python or shell
configuration, and refuses to overwrite an unrelated `lh` or reuse an unknown installation directory.
If `~/.local/bin` is not on PATH, it prints the command to enable it for your current terminal.
On Debian/Ubuntu you may need the distribution's `python3-venv` package first.

El instalador no toca el Python del sistema ni tus archivos de Bash/zsh. Si falla, no borra archivos
para intentar recuperarse: informa del error y conserva el estado para inspección.

```bash
./install.sh --dry-run         # Inspect paths without writes / Ver rutas sin cambios
./install.sh --upgrade         # Update a managed install / Actualizar una instalación propia
./install.sh --help            # Custom paths and offline wheelhouse / Rutas y modo offline
```

### Published version / Versión publicada

If you already use [pipx](https://pipx.pypa.io/stable/), the published release can be installed with:
Si ya usas pipx, instala la versión publicada con:

```bash
pipx install linux-commands-guide
```

The published release may not yet include the changes in this checkout.
La versión publicada puede no incluir todavía los cambios de este checkout.

For an existing virtual environment / En un entorno virtual existente:

```bash
python -m pip install linux-commands-guide
```

`shellcolorize` is the author's separate project, published on PyPI, and remains the color dependency.
Its repository does not need to be cloned for installation.

## Reference / Referencia

```bash
lh awk                            # Full reference / Referencia completa
lh ls --quick                     # Up to 8 curated examples / Hasta 8 ejemplos elegidos
lh grep --explain                 # Curated examples, explanation, notes and sources
lh -s 'disk space'                # Search both languages / Buscar en ambos idiomas
lh grep -s recursive              # Search only grep / Buscar solo en grep
lh list                           # Browse categories / Explorar categorías
lh list --category files          # Filter a category / Filtrar una categoría
lh --lang en ssh                  # Force English / Forzar inglés
lh --help
lh --version
python -m guia_linux awk           # Same CLI / La misma interfaz
python helper.py awk              # Legacy shim remains / Compatibilidad anterior
```

Search is case/accent-insensitive and requires every query word to match an entry's text, tool
summary or curated task keywords. It is local, not AI or natural-language reasoning. Use a few specific words.
La búsqueda no interpreta preguntas: prueba términos concretos como `disco`, `directory` o `permiso`.

Long references can be piped into `less`. `NO_COLOR=1` disables color; redirected output is plain
unless you explicitly set `FORCE_COLOR`. Commands are never reflowed, so copying preserves their
syntax; descriptions stack on narrow terminals.

```bash
lh tar | less
NO_COLOR=1 lh grep
```

`--explain` focuses on selected examples, not every advanced option. The most detailed explanations
are in foundational entries; advanced entries retain notes, effect warnings and source links.
`--explain` no pretende sustituir el manual completo de cada programa.

## Learn and practice / Aprender y practicar

```bash
lh learn
lh practice
```

Suggested route / Ruta sugerida:

1. `navigation` — paths, directories / rutas y directorios
2. `quoting` — quotes and arguments / comillas y argumentos
3. `globs` — filename globs versus regex / comodines frente a regex
4. `pipes` — stdin, stdout and stderr
5. `redirections` — input/output and overwrite risk / entrada, salida y sobrescritura
6. `exit-status` — exit codes, `&&` and `||`
7. `environment`, `permissions`, `processes`, `help`

Practices currently cover `grep`, `pipes`, `navigation`, `wc` and `regex`. They print fixture setup,
a challenge and expected output; hints and solutions are opt-in. **No commands run and no files
are created by lh.** If you copy the setup, it creates a fresh temporary directory. Use only that
directory; root is not required. There is no automatic assessment or cleanup of your files.

Las prácticas son guiadas: tú ejecutas y comparas resultados. `lh` no inspecciona tus documentos,
no ejecuta tu entrada y no guarda tu progreso.

## Safety and compatibility / Seguridad y compatibilidad

- Examples may **write, delete, change system state, generate traffic or expose sensitive data**.
  Such effects are labeled. An unlabelled reference is not a guarantee of safety.
- Never copy placeholders such as `<file>` literally. Replace them, omit the angle brackets and
  quote paths with spaces. Do not copy shell prompts (`$`/`#`) as commands.
- Read notes before using `sudo`, destructive options, recursive permissions or network changes.
- Scan only systems you own or have permission to test.
- The reference primarily covers GNU/Linux. Shell builtins, regex engines, netcat variants,
  distributions and installed versions can differ. systemd entries require systemd.
- Structural tests cover all content. Behavioral tests cover **selected** safe examples and practice
  fixtures, not every command or every Linux distribution.

See [compatibility](docs/compatibility.md) and [learning path](docs/learning-path.md).

## Available references / Fichas disponibles

<!-- BEGIN GENERATED CATALOG -->

114 references / fichas. Categories and aliases are available through `lh list`.

| Tool | Description | Category |
|------|-------------|----------|
| `apropos` | Find manuals by topic | basics |
| `apt` | Packages on Debian/Ubuntu | system |
| `awk` | Column-based text processing | text |
| `bat` | Read files with syntax highlighting | files |
| `bg` | Resume jobs in the background | processes |
| `cat` | Display and concatenate file contents | files |
| `cd` | Change to the specified directory | basics |
| `chmod` | Change file and directory permissions | files |
| `chown` | Change file owner and group | files |
| `command` | Check command resolution | basics |
| `cp` | Copy a file | files |
| `crontab` | Periodic task scheduling | system |
| `curl` | Transfer data with URLs | network |
| `cut` | Extract sections from each line | text |
| `date` | Show current date and time | system |
| `descriptors` | stdin, stdout and stderr redirections | shell |
| `df` | Display disk space usage | files |
| `diff` | Compare text files | files |
| `dig` | Query DNS records | network |
| `dirs` | Show the directory stack | shell |
| `dnf` | Packages on compatible Fedora/RHEL systems | system |
| `docker` | Docker container management | advanced |
| `du` | Display directory space usage | files |
| `echo` | Display text or variables | text |
| `env` | Inspect or pass environment variables | shell |
| `export` | Pass variables to child processes | shell |
| `fd` | Find files with fd | files |
| `fg` | Bring jobs to the foreground | processes |
| `file` | Identify file types | files |
| `find` | Search for files and directories | files |
| `firewall-cmd` | Manage the firewalld firewall | advanced |
| `free` | Display system memory usage | processes |
| `fzf` | Select text interactively | shell |
| `getent` | Query system name resolution | network |
| `git` | Version control with Git | development |
| `grep` | Search for patterns in files | text |
| `gzip` | Compress individual files | files |
| `head` | Display the beginning of a file | text |
| `help` | Help for Bash builtins | basics |
| `history` | Inspect your shell history | shell |
| `hostname` | Show or set the hostname | system |
| `htop` | Interactive process monitor | processes |
| `id` | Show UID, GID and groups of current user | system |
| `ifconfig` | Network interface configuration (legacy) | network |
| `ip` | Modern network interface and routing management | network |
| `iptables` | Kernel firewall rule management | advanced |
| `jobs` | Inspect jobs in your shell | processes |
| `journalctl` | Read systemd logs | system |
| `jq` | Command-line JSON processor | text |
| `kill` | Send signals to processes | processes |
| `less` | Display file contents interactively | files |
| `ln` | Create a symbolic link | files |
| `locate` | Find files using the locate database | files |
| `logs` | Important log file paths in Linux | system |
| `ls` | List the current directory contents | basics |
| `lsblk` | List block devices | files |
| `lsof` | List open files by processes | processes |
| `lxc` | LXC container management | advanced |
| `man` | Read command manuals | basics |
| `mkdir` | Create a new directory | files |
| `more` | Display file contents page by page | files |
| `mv` | Move or rename a file or directory | files |
| `nano` | Edit files in the terminal | files |
| `nc` | TCP/IP Swiss army knife | network |
| `ncdu` | Explore disk usage interactively | files |
| `netstat` | Network connection statistics | network |
| `nl` | Display file contents with line numbers | files |
| `nmap` | Network and port scanner | advanced |
| `pacman` | Packages on Arch-based systems | system |
| `pgrep` | Find PIDs by name | processes |
| `ping` | Check ICMP responses | network |
| `popd` | Return to the previously saved directory | shell |
| `printf` | Print predictably formatted text | text |
| `ps` | Information about running processes | processes |
| `pushd` | Save current directory and switch to the given one | shell |
| `pwd` | Print the current working directory | basics |
| `readlink` | Inspect symbolic links | files |
| `realpath` | Resolve absolute paths | files |
| `regex` | Regex search patterns | text |
| `rg` | Search text with ripgrep | text |
| `rm` | Remove a file | files |
| `rsync` | Efficient file synchronization | files |
| `scp` | Secure file copy over SSH | files |
| `sed` | Stream text editor | text |
| `sha256sum` | Check integrity with SHA-256 | files |
| `shortcuts` | Bash/zsh keyboard shortcuts | basics |
| `sort` | Sort lines of text | text |
| `ss` | Socket statistics (replaces netstat) | network |
| `ssh` | Secure Shell client | network |
| `stat` | Show file details (timestamps, permissions) | files |
| `sudo` | Understand and inspect privileges | system |
| `system` | Navigation, files and system management | basics |
| `systemctl` | Manage services with systemd | system |
| `tail` | Display the end of a file | text |
| `tar` | File archiving and compression | files |
| `tee` | Read stdin and write to stdout and files | text |
| `timeout` | Limit a command’s duration | processes |
| `tmux` | Terminal multiplexer | shell |
| `top` | Real-time process monitor | processes |
| `touch` | Create an empty file or update its timestamp | files |
| `tr` | Translate or delete characters | text |
| `tree` | Display directories as a tree | files |
| `type` | Identify commands, aliases and functions | basics |
| `umask` | Understand new-file permissions | shell |
| `uname` | System and kernel information | system |
| `uniq` | Filter adjacent duplicate lines | text |
| `unzip` | Inspect and extract ZIP archives | files |
| `uptime` | Show how long the system has been running | system |
| `vim` | Modal terminal text editor | shell |
| `watch` | Execute a command periodically | processes |
| `wc` | Count lines, words and bytes | text |
| `whoami` | Show the current user | system |
| `xargs` | Build and execute commands from stdin | text |
| `zip` | Create ZIP archives | files |

<!-- END GENERATED CATALOG -->

## Development / Desarrollo

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e '.[dev]'
ruff check .
python -m scripts.update_catalog_docs --check
pytest -q
python -m build
```

Content lives in validated bilingual JSON under `guia_linux/content/`, not in executable Python or
ANSI-colored strings. References can share example IDs without duplicating definitions.

- `catalog.py` loads/validates content and handles lookup/search.
- `render.py` presents it using stream-local `shellcolorize` colors, without global color mutation.
- `learning.py` displays lessons and practice plans without executing commands.
- `cli.py` parses requests; `models.py` holds immutable reference data.

The CI tests the declared minimum and published `shellcolorize` versions, builds a wheel and
checks installation outside the checkout. There is no automatic publication.

## Contribute / Contribuir

Found an incorrect example or confusing explanation? Open an issue; please remove private paths,
credentials and personal information from output. New contributors can improve a translation,
add a tested beginner example or clarify an error message.

See [CONTRIBUTING.md](CONTRIBUTING.md) and the [content guide](docs/content-guide.md).
For releases, see the [release checklist](docs/releasing.md). The [demo](docs/demo.gif) shows the
current beginner journey with real terminal output; its [recording](docs/demo.cast) is also included.

## License

[MIT](LICENSE). [Changelog](CHANGELOG.md).
