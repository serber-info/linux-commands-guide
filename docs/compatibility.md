# Compatibility and safety

- Python 3.9+; Linux is the target platform. Python 3.9 remains tested for existing users even though
  it is end-of-life; prefer a supported Python version for new installations.
- `shellcolorize>=1.1.1` from PyPI. No sibling checkout required. Its implementation remains in its
  own project; lh does not mutate global `Color` attributes.
- GNU tools are the reference baseline. Not every utility is installed by default.
- `cd`, `jobs`, `fg`, `bg`, `export`, `type` and `umask` are shell concepts/builtins. `help` is Bash;
  zsh uses `man zshbuiltins`. Learning a builtin does not require an executable on PATH.
- Regex depends on its engine. `grep` uses BRE, `grep -E` ERE and `grep -P` PCRE when supported.
  `\d` and lookaround are not portable ERE. Shell filename patterns are a different language.
- `nc` varies across OpenBSD netcat, traditional netcat and ncat. Check `nc -h` locally.
- `systemctl` and `journalctl` require systemd. Log paths depend on installed services/configuration.
- `apt`, `dnf` and `pacman` are alternatives for different distribution families, not commands to run
  interchangeably. DNF4/DNF5 can differ; Arch does not support partial upgrades.
- Optional tools (`bat`, `rg`, `fd`, `fzf`, `ncdu`, etc.) may need installation. `batcat`/`fdfind` are
  lookup aliases in lh, not a claim that those executables are installed.
- Classic LXC `lxc-*` is distinct from LXD/Incus's `lxc` client.
- `--quick` does not hide effect warnings. `--explain` covers curated examples; use the source manual
  for exhaustive option details.
- `FORCE_COLOR` can intentionally add ANSI to redirected output. `NO_COLOR` takes precedence.
- CLI usage errors exit 2; an unknown tool/topic exits 1; successful queries (including no search
  matches) exit 0. A closed downstream pipe exits 141 without a traceback.
- Tests validate every fiche's structure, but execute only selected safe examples. No claim is made
  that every example was tested on every distribution/version.

Official references: [Bash](https://www.gnu.org/software/bash/manual/bash.html),
[GNU Grep](https://www.gnu.org/software/grep/manual/grep.html),
[Findutils](https://www.gnu.org/software/findutils/manual/html_node/find_html/Safe-File-Name-Handling.html),
[Coreutils](https://www.gnu.org/software/coreutils/manual/coreutils.html).
