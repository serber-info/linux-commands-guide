import sys
import subprocess
import os

# Get the directory of this script
base_dir = os.path.dirname(os.path.abspath(__file__))
tools_dir = os.path.join(base_dir, "tools")  # Path to the tools subfolder

# Dictionary mapping each tool option to its corresponding script and description
tools = {
    "awk": (os.path.join(tools_dir, "awk.py"), "Displays examples and descriptions of awk usage."),
    "cat": (os.path.join(tools_dir, "cat.py"), "Displays examples and descriptions of cat usage."),
    "chown": (os.path.join(tools_dir, "chown.py"), "Displays examples and descriptions of chown usage."),
    "chmod": (os.path.join(tools_dir, "chmod.py"), "Displays examples and descriptions of chmod usage."),
    "curl": (os.path.join(tools_dir, "curl.py"), "Displays examples and descriptions of curl usage."),
    "cut": (os.path.join(tools_dir, "cut.py"), "Displays examples and descriptions of cut usage."),
    "descriptors": (os.path.join(tools_dir, "file_descriptors.py"), "Displays examples and descriptions of file descriptors and redirections usage."),
    "df": (os.path.join(tools_dir, "df.py"), "Displays examples and descriptions of df usage."),
    "docker": (os.path.join(tools_dir, "docker.py"), "Displays examples and descriptions of docker usage."),
    "du": (os.path.join(tools_dir, "du.py"), "Displays examples and descriptions of du usage."),
    "firewall-cmd": (os.path.join(tools_dir, "firewall_cmd.py"), "Displays examples and descriptions of firewall-cmd usage."),
    "find": (os.path.join(tools_dir, "find.py"), "Displays examples and descriptions of find usage."),
    "free": (os.path.join(tools_dir, "free.py"), "Displays examples and descriptions of free usage."),
    "git": (os.path.join(tools_dir, "git.py"), "Displays examples and descriptions of git usage."),
    "grep": (os.path.join(tools_dir, "grep.py"), "Displays examples and descriptions of grep usage."),
    "head": (os.path.join(tools_dir, "head.py"), "Displays examples and descriptions of head usage."),
    "htop": (os.path.join(tools_dir, "htop.py"), "Displays examples and descriptions of htop usage."),
    "ifconfig": (os.path.join(tools_dir, "ifconfig.py"), "Displays examples and descriptions of ifconfig usage."),
    "ip": (os.path.join(tools_dir, "ip.py"), "Displays examples and descriptions of ip usage."),
    "iptables": (os.path.join(tools_dir, "iptables.py"), "Displays examples and descriptions of iptables usage."),
    "logs": (os.path.join(tools_dir, "logs.py"), "Displays examples and descriptions of logs locations."),
    "lsblk": (os.path.join(tools_dir, "lsblk.py"), "Displays examples and descriptions of lsblk usage."),
    "lxc": (os.path.join(tools_dir, "lxc.py"), "Displays examples and descriptions of lxc usage."),
    "nc": (os.path.join(tools_dir, "nc.py"), "Displays examples and descriptions of nc (netcat) usage."),
    "netstat": (os.path.join(tools_dir, "netstat.py"), "Displays examples and descriptions of netstat usage."),
    "nmap": (os.path.join(tools_dir, "nmap.py"), "Displays examples and descriptions of nmap usage."),
    "regex": (os.path.join(tools_dir, "regex.py"), "Displays examples and descriptions of regular expressions."),
    "ps": (os.path.join(tools_dir, "ps.py"), "Displays examples and descriptions of ps usage."),
    "scp": (os.path.join(tools_dir, "scp.py"), "Displays examples and descriptions of scp usage."),
    "sed": (os.path.join(tools_dir, "sed.py"), "Displays examples and descriptions of sed usage."),
    "sort": (os.path.join(tools_dir, "sort.py"), "Displays examples and descriptions of sort usage."),
    "system": (os.path.join(tools_dir, "system.py"), "Displays examples and descriptions of basic system usage."),
    "systemctl": (os.path.join(tools_dir, "systemctl.py"), "Displays examples and descriptions of systemctl usage."),
    "tail": (os.path.join(tools_dir, "tail.py"), "Displays examples and descriptions of tail usage."),
    "tee": (os.path.join(tools_dir, "tee.py"), "Displays examples and descriptions of tee usage."),
    "top": (os.path.join(tools_dir, "top.py"), "Displays examples and descriptions of top usage."),
    "tr": (os.path.join(tools_dir, "tr.py"), "Displays examples and descriptions of tr usage."),
    "uname": (os.path.join(tools_dir, "uname.py"), "Displays examples and descriptions of uname usage."),
    "uniq": (os.path.join(tools_dir, "uniq.py"), "Displays examples and descriptions of uniq usage."),
    "vim": (os.path.join(tools_dir, "vim.py"), "Displays examples and descriptions of vim usage."),
    "watch": (os.path.join(tools_dir, "watch.py"), "Displays examples and descriptions of watch usage."),
    "xargs": (os.path.join(tools_dir, "xargs.py"), "Displays examples and descriptions of xargs usage.")
}

def show_help():
    print("Usage: helper.py -o <tool> or helper.py -h\\n")
    print("Available tools:")
    for tool, (script, description) in tools.items():
        print(f"  {tool:<10} - {description}")

def main():
    # Check if no arguments are provided or -h for help is requested
    if len(sys.argv) == 1 or "-h" in sys.argv:
        show_help()
        return

    # Check for the -o option and execute the corresponding script
    if "-o" in sys.argv:
        try:
            # Get the tool specified after the -o flag
            tool = sys.argv[sys.argv.index("-o") + 1]
            if tool in tools:
                script_path = tools[tool][0]
                subprocess.run(["python3", script_path])  # Run the specified tool script
            else:
                print(f"Tool '{tool}' not found.\\n")
                show_help()
        except IndexError:
            print("Error: No tool specified after '-o'.\\n")
            show_help()
    else:
        print("Invalid option. Use -h for help.")

if __name__ == "__main__":
    main()

