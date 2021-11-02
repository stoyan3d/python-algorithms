import unittest
from datastructures.heap import Heap


class TestHeap(unittest.TestCase):
    def test_delete(self):
        heap = Heap()

        heap.insert(3)
        heap.insert(25)
        heap.insert(1)
        heap.insert(7)
        heap.insert(2)
        heap.insert(19)
        heap.insert(36)
        heap.insert(100)
        heap.insert(17)

        self.assertEqual(100, heap.delete())
        self.assertEqual(36, heap.delete())
        self.assertEqual(25, heap.delete())

    def test_read(self):
        heap = Heap()

        heap.insert(3)
        heap.insert(25)
        heap.insert(1)
        self.assertEqual(25, heap.read())

        heap.insert(19)
        heap.insert(36)
        self.assertEqual(36, heap.read())

    def test_get_parent(self):
        heap = Heap()

        heap.insert(3)
        heap.insert(25)
        heap.insert(1)

        self.assertEqual(25, heap.get_parent(1))

    def test_get_left(self):
        heap = Heap()

        heap.insert(3)
        heap.insert(25)

        self.assertEqual(3, heap.get_left(0))

    def test_get_right(self):
        heap = Heap()

        heap.insert(3)
        heap.insert(25)
        heap.insert(1)

        self.assertEqual(1, heap.get_right(0))

    def test_get_max_child(self):
        heap = Heap()

        heap.insert(3)
        heap.insert(25)
        self.assertEqual(1, heap.get_max_child_index(0))

        heap.insert(1)
        self.assertEqual(1, heap.get_max_child_index(0))