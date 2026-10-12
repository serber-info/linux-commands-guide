"""Small immutable content model; commands are reference text, never executable input."""
from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass(frozen=True)
class Text:
    es: str
    en: str

    def in_lang(self, lang: str) -> str:
        return self.en if lang == "en" else self.es


@dataclass(frozen=True)
class Example:
    id: str
    text: str
    description: Text
    kind: str = "command"
    quick: bool = False
    effect: str = "reference"
    explanation: Optional[Text] = None
    output: str = ""


@dataclass(frozen=True)
class Tool:
    name: str
    title: Text
    brief: Text
    category: str
    level: str
    examples: Tuple[Example, ...]
    notes: Text
    sources: Tuple[str, ...]
    related: Tuple[str, ...] = ()
    aliases: Tuple[str, ...] = ()
    keywords: Tuple[str, ...] = ()
