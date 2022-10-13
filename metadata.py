from dataclasses import dataclass
from typing import cast
from ly.music.items import Document, Header, Assignment, Markup, String


@dataclass
class Metadata:
    title: str
    composer: str

    @classmethod
    def from_music(cls, doc: Document) -> "Metadata":
        title = ""
        composer = ""

        header: Header = next(doc.find(Header))
        for child in header:
            if isinstance(child, Assignment):
                t = child.name()
                if t == "title":
                    title_node = cast(Markup, child.value())
                    title = title_node.plaintext()
                elif t == "composer":
                    composer_node = cast(String, child.value())
                    composer = composer_node.plaintext()

        return cls(title, composer)
