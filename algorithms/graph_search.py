from __future__ import annotations
from typing import Optional, List
from datastructures.graph import GraphVertex, WeightedGraphVertex
from datastructures.queue import DoublyLinkedQueue


def depth_first_search(vertex: GraphVertex, search_value, visited_vertices=None) -> Optional[GraphVertex]:
    """This algorithm moves away from the starting vertex as quickly as possible.
    It relies on recursion.
    The time complexity is O(V + E) where V is the number of vertices and E is the number of edges."""

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
    It doesn't use recursion but instead relies on the Queue data structure.
    The time complexity is O(V + E) where V is the number of vertices and E is the number of edges."""

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


def dijkstra_shortest_path(starting: WeightedGraphVertex, destination: WeightedGraphVertex) -> List[str]:
    smallest_weight_table = {}
    smallest_weight_previous_vertex_table = {}
    unvisited_vertices: List[WeightedGraphVertex] = []
    visited_vertices: dict[WeightedGraphVertex, bool] = {}

    smallest_weight_table[starting.value] = 0
    current_vertex = starting

    while current_vertex:
        visited_vertices[current_vertex.value] = True
        if current_vertex in unvisited_vertices:
            unvisited_vertices.remove(current_vertex)

        for adjacent, weight in current_vertex.adjacent.items():
            if not visited_vertices.get(adjacent.value):
                unvisited_vertices.append(adjacent)

            weight_to_current_vertex = smallest_weight_table[current_vertex.value] + weight

            if not smallest_weight_table.get(adjacent.value) or \
                    weight_to_current_vertex < smallest_weight_table[adjacent.value]:
                smallest_weight_table[adjacent.value] = weight_to_current_vertex
                smallest_weight_previous_vertex_table[adjacent.value] = current_vertex.value

        # Pick the next vertex to visit based on the smallest weight
        if len(unvisited_vertices) > 0:
            current_vertex = unvisited_vertices[0]
            smallest_weight = smallest_weight_table[current_vertex.value]
            for vertex in unvisited_vertices:
                if smallest_weight_table[vertex.value] < smallest_weight:
                    smallest_weight = smallest_weight_table[vertex.value]
                    current_vertex = vertex
        else:
            current_vertex = None

    shortest_path = []
    current_vertex_value = destination.value
    while current_vertex_value != starting.value:
        shortest_path.append(current_vertex_value)
        current_vertex_value = smallest_weight_previous_vertex_table[current_vertex_value]

    shortest_path.append(current_vertex_value)

    return shortest_path[::-1]
