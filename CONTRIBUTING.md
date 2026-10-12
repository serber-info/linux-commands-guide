# Contributing / Contribuir

Help beginners understand a task, not just memorize an option. Small contributions are welcome:
translations, corrected examples, clearer warnings and new beginner references.

## Before changing content

1. Check whether the command already exists inside a grouped reference (`system`, `cat`, `ssh`).
2. Read the [content guide](docs/content-guide.md) and the installed tool's manual.
3. Keep Spanish and English equally useful, and cite primary documentation.
4. Describe effects and prerequisites. Never recommend bypassing permissions, TLS or host-key
   checks as a routine fix. Do not suggest `chmod 777` as a troubleshooting shortcut.
5. Test only safe examples with temporary fixtures. Never run the whole catalogue.

## Local checks

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e '.[dev]'
python -m scripts.update_catalog_docs
ruff check .
pytest -q
```

Adding `guia_linux/content/tools/<name>.json` automatically registers it. No handwritten Python
wrapper or registry is needed. The README table is generated; CI checks it is up to date.

A PR should state the learner's task, official source, compatibility, effects and verification.
Do not include real credentials, customer data, private infrastructure or personal paths.

## Useful issue labels

Suggested labels for maintainers: `content`, `beginner`, `translation`, `bug`, `good first issue`.
They are suggestions, not automatically created GitHub labels.

## Scope

Keep runtime offline and small. New services, telemetry, automatic command execution and access to
personal files are not part of this project. A fixture exercise is not a general shell runner.
Internal Python catalogue modules changed in this refactor; the supported public surface is `lh`,
`python -m guia_linux`, `helper.py`, and the lazy `guia_linux.main()` entry.
