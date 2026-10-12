#!/usr/bin/env python3
"""
castrec — record scripted terminal demos as asciicast v2 files.

A real interactive bash runs in a pseudo-terminal; commands are typed into it
character by character and the real output is captured. Timestamps use a
virtual clock so the recording pace does not depend on how fast the machine is.

Usage (from a demo script):

    from castrec import Session
    with Session("out.cast", cols=100, rows=30, env=...) as s:
        s.run("dube project --top 5")
        s.clear()
        s.run("dube project --tree")
"""
import fcntl
import json
import os
import pty
import select
import struct
import termios
import time

PROMPT_END = "\x1b[0m$ "     # the demo PS1 always ends like this


class Session:
    def __init__(self, path, cols=100, rows=30, env=None, cmd=None, title=None,
                 type_delay=0.055, prompt_pause=0.7):
        self.path, self.cols, self.rows = path, cols, rows
        self.type_delay, self.prompt_pause = type_delay, prompt_pause
        self.clock = 0.0
        self.events = []
        self.title = title
        cmd = cmd or ["bash", "--noprofile", "--norc", "-i"]
        self.pid, self.fd = pty.fork()
        if self.pid == 0:                      # child: the shell
            os.execvpe(cmd[0], cmd, env or os.environ)
        fcntl.ioctl(self.fd, termios.TIOCSWINSZ, struct.pack("HHHH", rows, cols, 0, 0))
        self.wait_prompt(timeout=15, record=False)   # skip shell start-up noise
        os.write(self.fd, b"\x0c")                   # then start from a clean screen + prompt
        self.wait_prompt()

    # ── low level ─────────────────────────────────────────────────────────────

    def _read(self, timeout):
        ready, _, _ = select.select([self.fd], [], [], timeout)
        if not ready:
            return ""
        try:
            return os.read(self.fd, 65536).decode("utf-8", "replace")
        except OSError:
            return ""

    def _emit(self, data, record=True):
        if data and record:
            self.events.append([round(self.clock, 3), "o", data])

    def wait_for(self, text, timeout=20, record=True, step=0.02):
        """Read output until `text` appears; output is spread over the virtual clock."""
        deadline = time.time() + timeout
        seen = ""
        while time.time() < deadline:
            chunk = self._read(0.05)
            if chunk:
                self._emit(chunk, record)
                self.clock += step
                seen += chunk
                if text in seen:
                    return seen
        raise TimeoutError(f"did not see {text!r}; last output: {seen[-300:]!r}")

    def wait_prompt(self, timeout=30, record=True):
        return self.wait_for(PROMPT_END, timeout, record)

    def settle(self, quiet=0.3, timeout=5):
        """Read until the terminal has been quiet for `quiet` seconds (real time)."""
        deadline = time.time() + timeout
        while time.time() < deadline:
            chunk = self._read(quiet)
            if not chunk:
                return
            self._emit(chunk)
            self.clock += 0.02

    # ── scripting helpers ─────────────────────────────────────────────────────

    def pause(self, seconds):
        self.clock += seconds

    def type(self, text):
        for ch in text:
            os.write(self.fd, ch.encode())
            self.clock += self.type_delay
            echo = self._read(0.5)
            self._emit(echo)

    def enter(self):
        os.write(self.fd, b"\r")

    def run(self, command, pause_after=2.5, timeout=60):
        """Type a command, press Enter, wait for the prompt, then linger."""
        self.pause(self.prompt_pause)
        self.type(command)
        self.pause(0.4)
        self.enter()
        self.clock += 0.1
        self.wait_prompt(timeout)
        self.pause(pause_after)

    def answer(self, question, reply, pause_before=0.6):
        """Wait for an interactive question, then type the reply and Enter."""
        self.wait_for(question)
        self.pause(pause_before)
        self.type(reply)
        self.pause(0.3)
        self.enter()
        self.clock += 0.05

    def clear(self):
        """Ctrl+L, like a person clearing the screen between commands."""
        self.pause(0.3)
        os.write(self.fd, b"\x0c")
        self.wait_prompt()

    # ── output ────────────────────────────────────────────────────────────────

    def close(self):
        try:
            os.write(self.fd, b"exit\r")
        except OSError:
            pass
        header = {"version": 2, "width": self.cols, "height": self.rows,
                  "timestamp": int(time.time()),
                  "env": {"SHELL": "/bin/bash", "TERM": "xterm-256color"}}
        if self.title:
            header["title"] = self.title
        with open(self.path, "w", encoding="utf-8") as fh:
            fh.write(json.dumps(header) + "\n")
            for event in self.events:
                fh.write(json.dumps(event, ensure_ascii=False) + "\n")
            fh.write(json.dumps([round(self.clock + 1.5, 3), "o", ""]) + "\n")  # hold last frame

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()
