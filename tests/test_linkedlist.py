import unittest
from datastructures.linkedlist import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_append(self):
        linked_list = LinkedList()
        data = 'something'
        linked_list.append(data)
        self.assertEqual(data, linked_list.read(0))

        data = 'else'
        linked_list.append(data)
        self.assertEqual(data, linked_list.read(1))

        data = 'happened'
        linked_list.append(data)
        self.assertEqual(data, linked_list.read(2))

    def test_read(self):
        linked_list = LinkedList()
        linked_list.append(20)
        self.assertEqual(20, linked_list.read(0))
        linked_list.append(10)
        self.assertEqual(10, linked_list.read(1))

    def test_read_index_out_of_range(self):
        linked_lists = LinkedList()

        with self.assertRaises(IndexError) as c:
            linked_lists.read(0)
        self.assertIn('Linked List index out of range', str(c.exception))

        linked_lists.append('hello')

        with self.assertRaises(IndexError) as c:
            linked_lists.read(3)
        self.assertIn('Linked List index out of range', str(c.exception))

        with self.assertRaises(IndexError) as c:
            linked_lists.read(1)
        self.assertIn('Linked List index out of range', str(c.exception))

    def test_insert(self):
        linked_list = LinkedList()
        linked_list.append(3)
        linked_list.append(6)
        linked_list.append(8)
        linked_list.insert(1, 'bee')
        linked_list.insert(2, 120)

        self.assertEqual('bee', linked_list.read(1))
        self.assertEqual(120, linked_list.read(2))
        self.assertEqual(6, linked_list.read(3))

        linked_list.insert(0, 'first')
        self.assertEqual('first', linked_list.read(0))
        self.assertEqual(3, linked_list.read(1))

    def test_insert_with_bigger_index(self):
        linked_list = LinkedList()
        linked_list.append(3)
        linked_list.append(6)
        linked_list.append(8)
        linked_list.insert(6, 'test')

        self.assertEqual('test', linked_list.read(3))

    def test_index_of(self):
        linked_list = LinkedList()
        linked_list.append(3)
        linked_list.append(6)
        linked_list.append(8)

        self.assertEqual(0, linked_list.index_of(3))
        self.assertEqual(1, linked_list.index_of(6))
        self.assertEqual(2, linked_list.index_of(8))
        self.assertIsNone(linked_list.index_of(10))

    def test_delete(self):
        linked_list = LinkedList()
        linked_list.append(3)
        linked_list.append(6)
        linked_list.append(8)
        linked_list.append(10)

        linked_list.delete(0)
        self.assertEqual(6, linked_list.read(0))

        linked_list.delete(1)
        self.assertEqual(10, linked_list.read(1))

    def test_delete_out_of_range(self):
        linked_list = LinkedList()
        with self.assertRaises(IndexError) as c:
            linked_list.delete(0)
        self.assertIn('Linked List index out of range', str(c.exception))

        linked_list.append(3)
        linked_list.append(6)
        linked_list.append(8)

        with self.assertRaises(IndexError) as c:
            linked_list.delete(3)
        self.assertIn('Linked List index out of range', str(c.exception))

        with self.assertRaises(IndexError) as c:
            linked_list.delete(10)
        self.assertIn('Linked List index out of range', str(c.exception))
