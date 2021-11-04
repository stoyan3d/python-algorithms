import unittest
from datastructures.graph import Vertex


class TestVertex(unittest.TestCase):
    def setUp(self):
        self.root = Vertex("Mohammad")
        felicia = Vertex("Felicia")
        zei = Vertex("Zei")

        self.root.add_adjacent(felicia)
        self.root.add_adjacent(zei)
        felicia.add_adjacent(zei)

    def test_dfs(self):
        self.assertEqual("Zei", self.root.depth_first_search(self.root, "Zei").value)
        self.assertEqual("Felicia", self.root.depth_first_search(self.root, "Felicia").value)
        self.assertIsNone(self.root.depth_first_search(self.root, "Tom"))

    def test_bfs(self):
        self.assertEqual("Zei", self.root.breadth_first_search(self.root, "Zei").value)
        self.assertEqual("Felicia", self.root.breadth_first_search(self.root, "Felicia").value)
        self.assertIsNone(self.root.breadth_first_search(self.root, "Tom"))
