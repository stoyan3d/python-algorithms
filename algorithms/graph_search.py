from __future__ import annotations
from typing import Optional
from datastructures.graph import GraphVertex
from datastructures.queue import DoublyLinkedQueue


def depth_first_search(vertex: GraphVertex, search_value, visited_vertices=None) -> Optional[GraphVertex]:
    """This algorithm moves away from the starting vertex as quickly as possible.
    It relies on recursion."""
    if visited_vertices is None:
        visited_vertices = {}

    if vertex.value == search_value:
        return vertex

    visited_vertices[vertex.value] = True

    for adjacent in vertex.adjacent:
        if visited_vertices.get(adjacent.value):
            continue

        if adjacent.value == search_value:
            return adjacent

        searched_vertex = depth_first_search(adjacent, search_value, visited_vertices)
        if searched_vertex:
            return searched_vertex

    return None


def breadth_first_search(vertex: GraphVertex, search_value) -> Optional[GraphVertex]:
    """This algorithm starts from all adjacent vertices and gradually moves away.
    It doesn't use recursion but instead relies on the Queue data structure."""

    queue = DoublyLinkedQueue()

    visited_vertices = {vertex.value: True}
    queue.enqueue(vertex)
    while queue.read():
        current_vertex = queue.dequeue()

        if current_vertex.value == search_value:
            return current_vertex

        for adjacent in current_vertex.adjacent:
            if not visited_vertices.get(adjacent.value):
                visited_vertices[adjacent.value] = True
                queue.enqueue(adjacent)

    return None
