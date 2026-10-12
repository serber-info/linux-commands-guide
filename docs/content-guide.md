# Content authoring / Guía de contenido

A tool is a UTF-8 JSON file in `guia_linux/content/tools/`. No ANSI codes or executable Python.
`catalog.py` validates it before exposing any content. JSON is packaged as a wheel resource
([setuptools data-files documentation](https://setuptools.pypa.io/en/latest/userguide/datafiles.html)).

## Minimal example

```json
{
  "name": "example",
  "title": {"es": "Ejemplo", "en": "Example"},
  "brief": {"es": "Qué tarea resuelve", "en": "What task it solves"},
  "category": "text",
  "level": "beginner",
  "notes": {"es": "Requisitos y errores comunes", "en": "Requirements and common mistakes"},
  "sources": ["https://www.gnu.org/software/coreutils/manual/coreutils.html"],
  "examples": [
    {
      "id": "example.01",
      "text": "printf '%s\\n' hola",
      "description": {"es": "Imprime una línea", "en": "Print one line"},
      "quick": true,
      "effect": "reference",
      "explanation": {"es": "%s inserta texto; \\n termina la línea.", "en": "%s inserts text; \\n ends the line."},
      "output": "hola"
    }
  ]
}
```

Use stable IDs: moving a file or editing wording must not rename its existing example IDs.
`{"ref": "system.46"}` references a definition elsewhere. The ID must actually exist; inspect the
JSON rather than guessing it. References share the same immutable model object. Only one definition
of each ID is allowed. Global search deduplicates references by ID.

## Fields

- Required tool fields: `name`, bilingual `title`/`brief`/`notes`, `category`, `level`, `sources`, `examples`.
- Optional: `related` (existing tool names), `aliases` (unique, non-reserved names), `keywords` (curated task phrases in either language).
- Categories: `basics`, `files`, `text`, `shell`, `processes`, `system`, `network`, `development`, `advanced`.
- Levels: `beginner`, `intermediate`, `advanced`.
- Example kinds: `command` (default), `pattern`, `path`, `shortcut`, `section`.
- Effects: `reference` (not a promise of safety), `write`, `delete`, `network`, `admin`, `sensitive`.
- `quick`: explicit boolean. Select useful examples; the CLI caps the quick/explained view at eight.
- `explanation`: optional bilingual text. Explain arguments/options, not just the description again.
- `output`: optional illustrative output. Label environment-dependent results; do not invent evidence.
- `section`: description carries the bilingual heading; not searchable as a command.

Unknown fields, invalid enums, duplicate definitions, missing translations, control codes and unknown
references are rejected. Source links are documentation, never fetched by the runtime.

## Editorial rules

Use real small tasks and replaceable values. Explain `<placeholder>` syntax; prefer harmless example
files. Quote paths, avoid relying on word splitting, label GNU/Bash/zsh/PCRE-specific behavior.
Start with inspection before mutation. A delete has no guaranteed undo; a network command requires
authorized targets. Sources must support the command, not merely be a project's homepage when a
specific manual is available.

Add a behavioral test at the CLI or catalogue seam when feasible. Tests must not send real device
commands, change live services, install system packages or scan remote systems.

Lessons are JSON in `content/topics/`. Exercises are JSON in `content/exercises/`: fixed plain-file
fixtures, a challenge, hint, expected result and a reviewed solution. The application displays them
only; selected test cases execute solutions with a timeout inside temporary directories.
