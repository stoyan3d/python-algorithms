from __future__ import annotations
from typing import List


class Vertex:
    def __init__(self, value) -> None:
        self.value = value
        self.adjacent: List[Vertex] = []

    def add_adjacent(self, vertex: Vertex) -> None:
        if vertex not in self.adjacent:
            self.adjacent.append(vertex)
            self.add_adjacent(self)
