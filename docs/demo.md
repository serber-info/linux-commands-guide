# Reproduce the terminal demo

`demo.gif` is rendered from the actual PTY output in `demo.cast`, not generated text or a desktop
recording. It shows quick lookup, task-based search, an explanation preview, pipes, available practice exercises,
and output alternating between English and Spanish using explicit `--lang en` / `--lang es` options.
The README remains English-only. Commands are scripted; typing and reading pauses use a virtual clock. Outputs
are captured from the current source checkout without alteration.

## Development tools only

- Linux with `bubblewrap` (`bwrap`) and permission to create its namespaces.
- A Python venv containing the project's `shellcolorize` dependency.
- [agg](https://docs.asciinema.org/manual/agg/usage/); the checked recording uses v1.9.0.
- DejaVu Sans Mono font (or change the explicit font in the script).

These are **not runtime dependencies**. agg may be provided as a temporary binary; no global install
is required. Download only from its official releases and verify the release checksum.

From the checkout, with your development venv activated:

```bash
python -m scripts.record_demo --tools "$VIRTUAL_ENV" --agg /path/to/agg
```

The script replaces `docs/demo.cast` and `docs/demo.gif`. Inspect the GIF before committing.
It uses a neutral `demo:~$` prompt, synthetic home, clean environment, read-only source and tools,
hidden real `/home` and `/run/user`, and a disabled network namespace. It never records the desktop,
uses real credentials, touches the clipboard or executes the printed practice preparation.

If bubblewrap fails, stop and inspect the error. There is deliberately no less-isolated fallback.

## Recording format and rendering

The reusable PTY recorder comes from the earlier project demo tooling. Its output follows
[asciicast v2](https://docs.asciinema.org/manual/asciicast/v2/). The renderer uses Monokai, a readable
18px font, a 96×36 terminal, a 12 FPS cap and deliberate pauses. The animation loops.

To change only visual rendering, without executing the commands again:

```bash
agg --theme monokai --text-font-family 'DejaVu Sans Mono' \
  --font-size 18 --line-height 1.15 --fps-cap 12 \
  --idle-time-limit 10 --last-frame-duration 3 docs/demo.cast docs/demo.gif
```
