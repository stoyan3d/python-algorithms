import unittest
from datastructures.graph import Vertex
from algorithms.graph_search import depth_first_search, breadth_first_search


class TestVertex(unittest.TestCase):
    def setUp(self):
        self.root = Vertex("Mohammad")
        felicia = Vertex("Felicia")
        zei = Vertex("Zei")

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
