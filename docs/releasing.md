# Release checklist

Publication is a maintainer action; neither CI nor the installer publishes anything.

1. Run `ruff check .`, `pytest -q`, and `python -m scripts.update_catalog_docs --check`.
2. Review example sources, translation parity, effect labels and compatibility notes.
3. Test against minimum and latest published `shellcolorize` (PyPI, not Git HEAD).
4. Build `python -m build`; inspect wheel and sdist for JSON content, installer and source docs.
5. Install the wheel in a clean venv **outside** the checkout. Test help, `ls --quick`, explanations,
   search, lessons, practice, `NO_COLOR`, and a closed pipe. Check `pip check`.
6. Test `./install.sh --dry-run` and a real isolated install using custom `/tmp` paths. Verify refusal
   on unrelated launchers and directories. Never reinstall over an unverified path.
7. Run a current dependency advisory check (for example PyPA `pip-audit`) in the release environment;
   document any findings/deferrals. Tests are not an advisory audit or supply-chain guarantee.
8. Update `__version__` and move the Unreleased changelog into a release only when ready to publish.
9. Publish manually through the project's established trusted channel. Do not put credentials in
   source, logs, issues or this checklist.

When CLI output changes, regenerate the real [terminal demo](demo.md) and inspect representative
frames for readability and privacy. Never substitute fabricated output or record a personal desktop.
