# linux-commands-guide — `lh`

[![CI](https://github.com/serber-info/linux-commands-guide/actions/workflows/ci.yml/badge.svg)](https://github.com/serber-info/linux-commands-guide/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/linux-commands-guide.svg)](https://badge.fury.io/py/linux-commands-guide)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/serber-info/linux-commands-guide?style=social)](https://github.com/serber-info/linux-commands-guide/stargazers)

**Bilingual ES/EN Linux command reference for the terminal.** 51 tools covered, keyword search across all of
them, one short command: `lh`. Like a cheat sheet that is always one keystroke away — and works over SSH.

*Guía de comandos Linux bilingüe (español / inglés) para la terminal.*

<p align="center">
  <img src="https://raw.githubusercontent.com/serber-info/linux-commands-guide/main/docs/demo.gif" alt="lh demo: ssh reference, keyword search and Spanish output" width="820">
</p>

---

## ✨ Features

- 🌐 **Bilingual** — Spanish or English, picked from your locale (`--lang es|en` to force it)
- 🔍 **Cross-tool search** — `lh -s port` finds every command mentioning "port", in both languages
- 📦 **51 tools** — awk, grep, find, git, docker, ssh, tmux, jq, ss, rsync, tar, systemctl, iptables and more
- ✅ **Checked content** — every entry is tested for both translations; examples are real, working commands
- 🔇 **Pipe-friendly** — plain text when piped (`lh tar | less`), honours `NO_COLOR`

---

## 📥 Installation

```bash
pip install linux-commands-guide
```

Or from source:

```bash
git clone https://github.com/serber-info/linux-commands-guide.git
cd linux-commands-guide
pip install -e .
```

---

## 🛠 Usage

```bash
lh <tool>                  # Show commands for a tool
lh -s <keyword>            # Search across all tools
lh --lang en <tool>        # Force English (or --lang es for Spanish)
lh --help                  # Help and the full tool list
lh --version
```

### Examples

```bash
lh ssh
```

```
  ╔══════════════════════════════════════════════╗
  ║  SSH Options                                 ║
  ╚══════════════════════════════════════════════╝

  Command                                             Description
  ──────────────────────────────────────────────────────────────────────────────────────────────
  ssh user@host                                       Connect to host as the given user
  ssh -p <port> user@host                             Connect using the specified port
  ssh -i key.pem user@host                            Use a private key for authentication
  ssh -L 8080:localhost:80 user@host                  Local tunnel: forward local port 8080 to host port 80
  ssh -R 9090:localhost:8080 user@host                Remote tunnel: forward host port 9090 to local port 8080
  …
```

```bash
lh -s port
```

```
  ╔══════════════════════════════════════════════════╗
  ║  Search: port                                    ║
  ╚══════════════════════════════════════════════════╝

  34 results

  ▶  docker
    docker run -p 8080:80 image_name
    Map host port to container port
  ▶  firewall-cmd
    firewall-cmd --zone=zone --add-port=80/tcp --permanent
    Permanently open TCP port 80
    firewall-cmd --zone=zone --remove-port=80/tcp --permanent
  …
```

---

## 🔧 Available Tools

| Tool | Description |
|------|-------------|
| `awk` | Column-based text processing |
| `cat` | Display and concatenate file contents |
| `chmod` | Change file permissions |
| `chown` | Change file owner and group |
| `crontab` | Periodic task scheduling |
| `curl` | Transfer data with URLs |
| `cut` | Extract sections from each line |
| `df` | Display disk space usage |
| `docker` | Docker container management |
| `du` | Display directory space usage |
| `descriptors` | File descriptors and redirections |
| `find` | Search for files and directories |
| `firewall-cmd` | Manage the firewalld firewall |
| `free` | Display system memory usage |
| `git` | Version control with Git |
| `grep` | Search for patterns in files |
| `head` | Display the beginning of a file |
| `htop` | Interactive process monitor |
| `ifconfig` | Network interface configuration (legacy) |
| `ip` | Modern network interface and routing management |
| `iptables` | Kernel firewall rule management |
| `jq` | Command-line JSON processor |
| `logs` | Important log file paths in Linux |
| `lsblk` | List block devices |
| `lsof` | List open files by processes |
| `lxc` | LXC container management |
| `nc` | TCP/IP Swiss army knife |
| `netstat` | Network connection statistics |
| `nmap` | Network and port scanner |
| `ps` | Information about running processes |
| `regex` | Regular expression patterns |
| `rsync` | Efficient file synchronization |
| `scp` | Secure file copy over SSH |
| `sed` | Stream text editor |
| `shortcuts` | Terminal keyboard shortcuts |
| `sort` | Sort lines of text |
| `ss` | Socket statistics (replaces netstat) |
| `ssh` | Secure Shell client |
| `system` | Basic system commands |
| `systemctl` | Manage services with systemd |
| `tail` | Display the end of a file |
| `tar` | File archiving and compression |
| `tee` | Read stdin and write to stdout and files |
| `tmux` | Terminal multiplexer |
| `top` | Real-time process monitor |
| `tr` | Translate or delete characters |
| `uname` | System and kernel information |
| `uniq` | Filter adjacent duplicate lines |
| `vim` | Modal terminal text editor |
| `watch` | Execute a command periodically |
| `xargs` | Build and execute commands from stdin |

---

## 🧪 Development

```bash
pip install -e ".[dev]"
ruff check .
pytest
```

Each tool is a small module in `guia_linux/tools/` with a `COMMANDS` list. To add one, copy an existing
module, register it in `guia_linux/tools/__init__.py`, add it to the table above, and run `pytest` —
the test suite checks that every entry has both translations and that the README lists every tool.

See [CHANGELOG.md](CHANGELOG.md) for release notes.

---

## 📝 License

MIT — see [LICENSE](LICENSE).

---

## 💬 Feedback

Open an issue or reach out via GitHub.

## 🌐 Connect

[![GitHub](https://img.shields.io/badge/GitHub-@serber--info-181717?style=flat-square&logo=github)](https://github.com/serber-info)
