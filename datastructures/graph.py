from __future__ import annotations
from typing import List


class GraphVertex:
    def __init__(self, value) -> None:
        self.value = value
        self.adjacent: List[GraphVertex] = []

    def add_adjacent(self, vertex: GraphVertex) -> None:
        if vertex not in self.adjacent:
            self.adjacent.append(vertex)
            self.add_adjacent(self)
