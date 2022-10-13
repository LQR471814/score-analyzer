
from dataclasses import dataclass
from enum import Enum
from typing import Any, Generic, Iterator
from typing_extensions import TypeVarTuple, Unpack


def condition(name: str) -> Enum:
    return Enum(name, "TRUE FALSE")


K = TypeVarTuple("K")

# def nested_dict():

#     for var in K:


# # * a invertible, multidimensional, state machine
# class StateMachine(Generic[Unpack[K]]):
#     _tree

#     pass

@dataclass
class DecisionTree(Generic[I, O]):
    _tree: dict[I, Any]
    _inverse: dict[O, Any]

    inputs: set[I]
    outputs: set[O]

    def __init__(self, tree: dict[I, O]) -> None:
        self._tree = tree
        self._inverse = {}
        self.inputs = set()
        self.outputs = set()

        for k in tree:
            self.inputs.add(k)

        def traverse_bottom(
            node: dict[Any, Any], path: list[Any]
        ) -> Iterator[tuple[O, list[Any]]]:
            for k in node:
                if not isinstance(node[k], dict):
                    yield (node[k], path)
                    continue
                traverse_bottom(node[k], [*path, k])

        for o, path in traverse_bottom(tree, []):
            if o not in self._inverse:
                self._inverse[o] = {}

            current = self._inverse[o]
            for k in reversed(path):
                current[k] =

            self.outputs.add(o)


