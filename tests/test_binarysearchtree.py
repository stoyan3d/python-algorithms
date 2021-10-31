import unittest
from datastructures.binarysearchtree import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):
    def test_search(self):
        bst = BinarySearchTree()

        bst.insert(2)
        bst.insert(5)
        bst.insert(7)

        self.assertTrue(bst.search(5))
        self.assertTrue(bst.search(2))
        self.assertTrue(bst.search(7))
        self.assertFalse(bst.search(3))

    def test_insert_existing_data(self):
        bst = BinarySearchTree()
        bst.insert(2)
        bst.insert(5)
        bst.insert(7)

        self.assertFalse(bst.insert(5))
        self.assertTrue(bst.insert(6))

    def test_delete(self):
        bst = BinarySearchTree()

        bst.insert(1)
        bst.insert(5)
        bst.insert(9)
        bst.insert(2)
        bst.insert(4)
        bst.insert(10)

        bst.delete(9)
        self.assertFalse(bst.search(9))
        self.assertTrue(bst.search(2))