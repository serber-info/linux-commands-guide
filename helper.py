#!/usr/bin/env python3
# Backward-compatibility shim — use 'lh' after pip install, or run this directly.
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from guia_linux.cli import run  # noqa: E402

if __name__ == "__main__":
    run()
