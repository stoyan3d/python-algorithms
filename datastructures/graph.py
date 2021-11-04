from __future__ import annotations
from typing import List, Optional


class Vertex:
    def __init__(self, value) -> None:
        self.value = value
        self.adjacent: List[Vertex] = []

    def add_adjacent(self, vertex: Vertex) -> None:
        if vertex not in self.adjacent:
            self.adjacent.append(vertex)
            self.add_adjacent(self)

    def depth_first_search(self, vertex: Vertex, search_value, visited_vertices=None) -> Optional[Vertex]:
        if visited_vertices is None:
            visited_vertices = {}

        if vertex.value == search_value:
            return vertex
        
        visited_vertices[vertex.value] = True

        for adjacent in self.adjacent:
            if visited_vertices.get(adjacent.value):
                continue

            if adjacent.value == search_value:
                return adjacent

            searched_vertex = self.depth_first_search(adjacent, search_value, visited_vertices)
            if searched_vertex:
                return searched_vertex

        return None
