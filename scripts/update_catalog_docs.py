"""Generate the README catalogue from its only source of truth."""
import argparse
from pathlib import Path

from guia_linux.catalog import load_catalog

START = '<!-- BEGIN GENERATED CATALOG -->'
END = '<!-- END GENERATED CATALOG -->'


def catalogue_markdown():
    tools = load_catalog().list()
    lines = [f'{len(tools)} references / fichas. Categories and aliases are available through `lh list`.', '',
             '| Tool | Description | Category |', '|------|-------------|----------|']
    for tool in tools:
        brief = tool.brief.en.replace('|', r'\|').replace('\n', ' ')
        lines.append(f'| `{tool.name}` | {brief} | {tool.category} |')
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    path = Path(__file__).resolve().parents[1] / 'README.md'
    original = path.read_text(encoding='utf-8')
    if original.count(START) != 1 or original.count(END) != 1:
        parser.error('README catalogue markers missing or repeated')
    head, tail = original.split(START, 1)
    _, end = tail.split(END, 1)
    updated = head + START + '\n\n' + catalogue_markdown() + '\n\n' + END + end
    if args.check:
        if original != updated:
            parser.exit(1, 'Catalogue is stale: run python -m scripts.update_catalog_docs\n')
    else:
        path.write_text(updated, encoding='utf-8')


if __name__ == '__main__':
    main()
