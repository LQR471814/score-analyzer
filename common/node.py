from __future__ import annotations

from typing import Iterable, Type, TypeVar
from ly.music.items import Item

N = TypeVar("N", bound=Item)


def get_descendants(roots: list[Item], targets: list[Type[N]]) -> list[Item]:
    pool = roots
    for t in targets:
        current: list[Item] = []
        for element in pool:
            n: Item
            for n in element.find(t):
                current.append(n)
        pool = current
    return pool


def get_children(roots: list[Item], targets: list[Type[N]]) -> list[Item]:
    pool = roots
    for t in targets:
        current: list[Item] = []
        n: Item
        for n in pool:
            for child in n:
                if type(child) == t:
                    current.append(child)
        pool = current
    return pool


def filter_ancestors(roots: Iterable[Item], targets: list[Type[N]]) -> list[Item]:
    ok_nodes = []
    for r in roots:
        bad = False
        for n in r.ancestors():
            for t in targets:
                if type(n) == t:
                    bad = True
                    break
            if bad == False:
                break
        if not bad:
            ok_nodes.append(r)
    return ok_nodes


class BadScore(Exception):
    message: str

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__()

    def __str__(self) -> str:
        return f"bad score: {self.message}"
