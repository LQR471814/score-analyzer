from __future__ import annotations

from typing import Type, TypeVar
from ly.node import Node

N = TypeVar("N", bound=Node)


def get_descendants(roots: list[Node], targets: list[Type[N]]) -> list[Type[N]]:
    pool = roots
    for t in targets:
        current = []
        for element in pool:
            for n in element.find(t):
                current.append(n)
        pool = current
    return pool


def get_children(roots: list[Node], targets: list[Type[N]]) -> list[Type[N]]:
    pool = roots
    for t in targets:
        current = []
        for n in pool:
            for child in n:
                if type(child) == t:
                    current.append(child)
        pool = current
    return pool


def filter_ancestors(roots: list[Node], targets: list[Type[N]]) -> list[Node]:
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


roman_numerals = ["I", "II", "III", "IV", "V", "VI", "VII"]
