#!/bin/sh
# Local checkout installer. Never sudo, curl|sh, or change shell configuration.
set -eu
ROOT=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
if ! command -v python3 >/dev/null 2>&1; then
    printf '%s\n' 'Python 3.9+ with venv is required / Se requiere Python 3.9+ con venv.' >&2
    exit 1
fi
exec python3 "$ROOT/scripts/install.py" "$@"
