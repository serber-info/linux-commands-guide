"""Validated package data behind one query interface. No filesystem or shell queries.

Package resources work in an installed wheel as well as a source checkout:
https://docs.python.org/3.9/library/importlib.html#module-importlib.resources
"""
import json
import re
import unicodedata
from functools import lru_cache
from importlib.resources import files
from types import MappingProxyType
from typing import Mapping, Optional

from guia_linux.models import Example, Text, Tool

CATEGORIES = ("basics", "files", "text", "shell", "processes", "system", "network", "development", "advanced")
LEVELS = ("beginner", "intermediate", "advanced")
EFFECTS = ("reference", "write", "delete", "network", "admin", "sensitive")
KINDS = ("command", "pattern", "path", "shortcut", "section")
RESERVED_NAMES = {"list", "learn", "practice"}
_NAME = re.compile(r"[a-z0-9][a-z0-9-]*\Z")
_ID = re.compile(r"[a-z0-9][a-z0-9.-]*\Z")


def _clean(value, label, allow_empty=False):
    if not isinstance(value, str) or (not allow_empty and not value.strip()):
        raise ValueError(f"{label}: expected non-empty text")
    if any(not c.isprintable() and c not in "\n\t" for c in value):
        raise ValueError(f"{label}: control characters are not allowed")
    return value


def _text(value, label, allow_empty=False):
    if not isinstance(value, dict) or set(value) != {"es", "en"}:
        raise ValueError(f"{label}: both es and en are required")
    return Text(*(_clean(value[lang], f"{label}.{lang}", allow_empty) for lang in ("es", "en")))


def _fields(data, required, optional, label):
    if not isinstance(data, dict) or not required <= data.keys() or data.keys() - required - optional:
        raise ValueError(f"{label}: missing or unknown fields")


def _strings(value, label):
    if not isinstance(value, list):
        raise ValueError(f"{label}: expected a list")
    return tuple(_clean(v, label) for v in value)


def _example(data):
    _fields(data, {"id", "text", "description"}, {"kind", "quick", "effect", "explanation", "output"}, "example")
    if not isinstance(data["id"], str) or not _ID.fullmatch(data["id"]):
        raise ValueError("example: invalid id")
    kind, effect = data.get("kind", "command"), data.get("effect", "reference")
    if kind not in KINDS or effect not in EFFECTS or type(data.get("quick", False)) is not bool:
        raise ValueError("example: invalid kind, effect or quick flag")
    explanation = _text(data["explanation"], "explanation") if "explanation" in data else None
    return Example(data["id"], _clean(data["text"], "text"), _text(data["description"], "description"),
                   kind, data.get("quick", False), effect, explanation, _clean(data.get("output", ""), "output", True))


def normalize(text):
    return "".join(c for c in unicodedata.normalize("NFKD", text.casefold()) if not unicodedata.combining(c))


class Catalog:
    def __init__(self, tools: Mapping[str, Tool]):
        self.tools = MappingProxyType(dict(tools))
        aliases = {}
        for tool in tools.values():
            for alias in tool.aliases:
                if alias in tools or alias in aliases:
                    raise ValueError(f"Duplicate alias: {alias}")
                aliases[alias] = tool.name
            if any(name not in tools for name in tool.related):
                raise ValueError(f"Unknown related tool: {tool.name}")
        self.aliases = MappingProxyType(aliases)

    def get(self, name: str) -> Tool:
        name = name.lower()
        return self.tools[self.aliases.get(name, name)]

    def list(self, category: Optional[str] = None):
        return tuple(t for t in sorted(self.tools.values(), key=lambda t: t.name) if category is None or t.category == category)

    def search(self, query: str, tool: Optional[str] = None):
        """Accent-insensitive AND search, grouped by tool; no network or fuzzy guesses."""
        tokens = normalize(query).split()
        if not tokens:
            return ()
        tools = (self.get(tool),) if tool else self.list()
        results = []
        seen = set()
        for item in tools:
            for entry in item.examples:
                if entry.kind == "section" or entry.id in seen:
                    continue
                haystack = normalize(" ".join((item.name, item.brief.es, item.brief.en, *item.keywords, entry.text,
                                               entry.description.es, entry.description.en)))
                if all(token in haystack for token in tokens):
                    results.append((item, entry))
                    seen.add(entry.id)
        return tuple(results)


def catalog_from_data(documents):
    """Validate all definitions and references before exposing any content."""
    documents = tuple(documents)
    definitions = {}
    names = set()
    required = {"name", "title", "brief", "category", "level", "examples", "notes", "sources"}
    for doc in documents:
        _fields(doc, required, {"related", "aliases", "keywords"}, "tool")
        name = doc["name"]
        if not isinstance(name, str) or not _NAME.fullmatch(name) or name in names or name in RESERVED_NAMES:
            raise ValueError("tool: invalid or duplicate name")
        names.add(name)
        if doc["category"] not in CATEGORIES or doc["level"] not in LEVELS:
            raise ValueError(f"{name}: invalid category or level")
        if not isinstance(doc["examples"], list) or not doc["examples"]:
            raise ValueError(f"{name}: examples must not be empty")
        for row in doc["examples"]:
            if isinstance(row, dict) and set(row) == {"ref"}:
                continue
            entry = _example(row)
            if entry.id in definitions:
                raise ValueError(f"Duplicate example id: {entry.id}")
            definitions[entry.id] = entry
    tools = {}
    for doc in documents:
        entries = []
        for row in doc["examples"]:
            key = row.get("ref", row.get("id"))
            if not isinstance(key, str) or key not in definitions:
                raise ValueError(f"Unknown example reference: {key}")
            entries.append(definitions[key])
        if len({e.id for e in entries}) != len(entries):
            raise ValueError(f"{doc['name']}: repeated example")
        if not any(e.quick and e.kind != "section" for e in entries):
            raise ValueError(f"{doc['name']}: select at least one quick example")
        sources = _strings(doc["sources"], "sources")
        if not sources or any(not s.startswith("https://") or " " in s for s in sources):
            raise ValueError("sources: HTTPS documentation links required")
        aliases = _strings(doc.get("aliases", []), "aliases")
        if any(not _NAME.fullmatch(a) or a in RESERVED_NAMES for a in aliases):
            raise ValueError("invalid alias")
        tool = Tool(doc["name"], _text(doc["title"], "title"), _text(doc["brief"], "brief"),
                    doc["category"], doc["level"], tuple(entries), _text(doc["notes"], "notes", True),
                    sources, _strings(doc.get("related", []), "related"), aliases,
                    _strings(doc.get("keywords", []), "keywords"))
        tools[tool.name] = tool
    return Catalog(tools)


@lru_cache(maxsize=1)
def load_catalog():
    root = files("guia_linux").joinpath("content").joinpath("tools")
    docs = [json.loads(p.read_text(encoding="utf-8")) for p in sorted(root.iterdir(), key=lambda p: p.name) if p.name.endswith(".json")]
    return catalog_from_data(docs)
