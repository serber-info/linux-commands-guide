#!/usr/bin/env python3
# Backward-compatibility shim — use 'lh' after pip install, or run this directly.
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from guia_linux.cli import main

if __name__ == "__main__":
    main()
