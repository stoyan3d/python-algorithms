import unittest
from datastructures.trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self) -> None:
        self.trie = Trie()

        self.trie.insert("get")
        self.trie.insert("go")
        self.trie.insert("got")
        self.trie.insert("gotten")
        self.trie.insert("hall")
        self.trie.insert("ham")
        self.trie.insert("hammer")
        self.trie.insert("hill")
        self.trie.insert("zebra")

    def test_search(self):
        self.assertIsNotNone(self.trie.search("gotten"))
        self.assertIsNotNone(self.trie.search("hall"))
        self.assertIsNone(self.trie.search("mango"))
        self.assertIsNone(self.trie.search("gottenberg"))

    def test_autocomplete(self):
        self.assertListEqual(["got", "gotten"], self.trie.auto_complete("got"))
        self.assertListEqual(["hall", "ham", "hammer"], self.trie.auto_complete("ha"))

    def test_autocorrect(self):
        self.assertEqual("hammer", self.trie.auto_correct("hammed"))
        self.assertEqual("hall", self.trie.auto_correct("hatl"))
        self.assertEqual("gotten", self.trie.auto_correct("gottvn"))
        self.assertEqual("get", self.trie.auto_correct("ga"))

        self.assertIsNone(self.trie.auto_correct("billow"))
