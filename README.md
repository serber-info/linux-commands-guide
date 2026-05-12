# Guia-Comandos-Linux

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/serber-info/Guia-Comandos-Linux?style=social)](https://github.com/serber-info/Guia-Comandos-Linux/stargazers)

**Bilingual ES/EN interactive Linux command reference for the terminal.** 50+ tools covered, keyword search across all of them, pip-installable with a single `lh` command.

---

## ✨ Features

- 🌐 **Bilingual** — full Spanish and English descriptions via `--lang en` / `--lang es`
- 🔍 **Cross-tool search** — `lh -s recursive` finds every command mentioning "recursive" across all tools
- 📦 **50+ tools** — awk, grep, find, git, docker, ssh, tmux, jq, ss, rsync, tar, crontab and many more
- 🚀 **pip-installable** — one command, available anywhere in your shell as `lh`

---

## 📥 Installation

```bash
pip install guia-linux
```

Or clone and install in development mode:

```bash
git clone https://github.com/serber-info/Guia-Comandos-Linux.git
cd Guia-Comandos-Linux
pip install -e .
```

---

## 🛠 Usage

```bash
lh <tool>                  # Show commands for a tool (Spanish by default)
lh --lang en <tool>        # Force English output
lh -s <keyword>            # Search across all tools
lh -s <keyword> --lang en  # Search in English
lh --help                  # Show help and full tool list
```

### Examples

```bash
lh grep                    # All grep options in Spanish
lh --lang en grep          # All grep options in English
lh -s recursive            # Find every command mentioning "recursive"
lh -s port --lang en       # Find port-related commands (English descriptions)
lh ssh
lh docker
lh tmux
lh jq
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

## 📝 License

MIT — see [LICENSE](LICENSE).

---

## 💬 Feedback

Open an issue or reach out via GitHub.

## 🌐 Connect

[![GitHub](https://img.shields.io/badge/GitHub-@serber--info-181717?style=flat-square&logo=github)](https://github.com/serber-info)
