import unittest
from datastructures.graph import GraphVertex, WeightedGraphVertex
from algorithms.graph_search import depth_first_search, breadth_first_search, dijkstra_shortest_path


class TestGraphVertex(unittest.TestCase):
    def setUp(self):
        self.root = GraphVertex("Mohammad")
        felicia = GraphVertex("Felicia")
        zei = GraphVertex("Zei")

        self.root.add_adjacent(felicia)
        self.root.add_adjacent(zei)
        felicia.add_adjacent(zei)

    def test_dfs(self):
        self.assertEqual("Zei", depth_first_search(self.root, "Zei").value)
        self.assertEqual("Felicia", depth_first_search(self.root, "Felicia").value)
        self.assertIsNone(depth_first_search(self.root, "Tom"))

    def test_bfs(self):
        self.assertEqual("Zei", breadth_first_search(self.root, "Zei").value)
        self.assertEqual("Felicia", breadth_first_search(self.root, "Felicia").value)
        self.assertIsNone(breadth_first_search(self.root, "Tom"))


class TestWeightedGraphVertex(unittest.TestCase):
    def test_dijkstra_shortest_path(self):
        atlanta = WeightedGraphVertex("Atlanta")
        boston = WeightedGraphVertex("Boston")
        chicago = WeightedGraphVertex("Chicago")
        denver = WeightedGraphVertex("Denver")
        el_paso = WeightedGraphVertex("El Paso")

        atlanta.add_adjacent(boston, 100)
        atlanta.add_adjacent(denver, 160)
        boston.add_adjacent(chicago, 120)
        boston.add_adjacent(denver, 180)
        chicago.add_adjacent(el_paso, 80)
        denver.add_adjacent(chicago, 40)
        denver.add_adjacent(el_paso, 140)

        self.assertListEqual(["Atlanta", "Denver", "Chicago", "El Paso"], dijkstra_shortest_path(atlanta, el_paso))
