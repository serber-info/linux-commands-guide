# Changelog

## 2.1.0

### Fixed (content)
- `regex`: `word{3}`, `word*`, `word+` and `word?` were described as repeating the whole word; a quantifier only
  applies to the previous item. Now `(word){3}`, `(word){2,5}`, `a*`, `a+` and `colou?r`.
- `lxc`: `lxc-config -n … -s storage|network|security`, `lxc-attach -f /path` and `lxc-restart` do not exist or
  do something else. The tool now covers create, start/stop/reboot, attach, console, info, freeze, copy,
  snapshot, destroy and checkconfig.
- `chown --from` had the wrong syntax (`--from=old_user new_user file`).
- `cat` listed `bat` options (`-r`, `--theme`, `--paging`, `-L`) as if they were `cat` options.
- `rsync` examples without `-a` did not recurse (`--delete`, `--exclude`, `--dry-run`…).
- `xargs -P 4 python3` passed many files to one process; now `-n 1 -P 4`.
- `iptables` uses `-m conntrack --ctstate` instead of the deprecated `-m state`.
- Clarified `ifconfig add` (IPv6), tmux split directions and netcat variants (`-p`, `-e`).

### Fixed
- README install command (`pip install linux-commands-guide`), badges and clone folder.
- Missing LICENSE file (MIT, as declared).
- Colors were written into pipes and files; output is plain when piped or when `NO_COLOR` is set.
- Header boxes were two characters too wide.
- `lh tool | head` printed a BrokenPipeError traceback.

### Added
- Language is picked from the locale (`es_*` → Spanish, anything else → English); `--lang` still forces it.
- Search matches both the Spanish and the English descriptions.
- `lh --version` and `python -m guia_linux`.
- Test suite (content checks for all 51 tools) and GitHub Actions CI.

### Removed
- The legacy top-level `tools/` directory (v1 code, no longer used).

## 2.0.1

- Visual redesign: clean box headers, ANSI-aware alignment.

## 2.0.0

- Bilingual, search, 51 tools, pip-installable.
