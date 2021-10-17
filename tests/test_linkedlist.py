import unittest
from datastructures.linkedlist import LinkedList, DoublyLinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.linked_list = LinkedList()

    def test_append(self):
        data = 'something'
        self.linked_list.append(data)
        self.assertEqual(data, self.linked_list.read(0))

        data = 'else'
        self.linked_list.append(data)
        self.assertEqual(data, self.linked_list.read(1))

        data = 'happened'
        self.linked_list.append(data)
        self.assertEqual(data, self.linked_list.read(2))

    def test_read(self):
        self.linked_list.append(20)
        self.assertEqual(20, self.linked_list.read(0))
        self.linked_list.append(10)
        self.assertEqual(10, self.linked_list.read(1))

    def test_read_index_out_of_range(self):
        with self.assertRaises(IndexError) as c:
            self.linked_list.read(0)
        self.assertIn('Linked List index out of range', str(c.exception))

        self.linked_list.append('hello')

        with self.assertRaises(IndexError) as c:
            self.linked_list.read(3)
        self.assertIn('Linked List index out of range', str(c.exception))

        with self.assertRaises(IndexError) as c:
            self.linked_list.read(1)
        self.assertIn('Linked List index out of range', str(c.exception))

    def test_insert(self):
        self.linked_list.append(3)
        self.linked_list.append(6)
        self.linked_list.append(8)
        self.linked_list.insert(1, 'bee')
        self.linked_list.insert(2, 120)

        self.assertEqual('bee', self.linked_list.read(1))
        self.assertEqual(120, self.linked_list.read(2))
        self.assertEqual(6, self.linked_list.read(3))

        self.linked_list.insert(0, 'first')
        self.assertEqual('first', self.linked_list.read(0))
        self.assertEqual(3, self.linked_list.read(1))

    def test_insert_with_bigger_index(self):
        self.linked_list.append(3)
        self.linked_list.append(6)
        self.linked_list.append(8)
        self.linked_list.insert(6, 'test')

        self.assertEqual('test', self.linked_list.read(3))

    def test_index_of(self):
        self.linked_list.append(3)
        self.linked_list.append(6)
        self.linked_list.append(8)

        self.assertEqual(0, self.linked_list.index_of(3))
        self.assertEqual(1, self.linked_list.index_of(6))
        self.assertEqual(2, self.linked_list.index_of(8))
        self.assertIsNone(self.linked_list.index_of(10))

    def test_delete(self):
        self.linked_list.append(3)
        self.linked_list.append(6)
        self.linked_list.append(8)
        self.linked_list.append(10)

        self.linked_list.delete(0)
        self.assertEqual(6, self.linked_list.read(0))

        self.linked_list.delete(1)
        self.assertEqual(10, self.linked_list.read(1))

    def test_delete_out_of_range(self):
        with self.assertRaises(IndexError) as c:
            self.linked_list.delete(0)
        self.assertIn('Linked List index out of range', str(c.exception))

        self.linked_list.append(3)
        self.linked_list.append(6)
        self.linked_list.append(8)

        with self.assertRaises(IndexError) as c:
            self.linked_list.delete(3)
        self.assertIn('Linked List index out of range', str(c.exception))

        with self.assertRaises(IndexError) as c:
            self.linked_list.delete(10)
        self.assertIn('Linked List index out of range', str(c.exception))

    def test_print(self):
        self.linked_list.append('apple')
        self.linked_list.append('orange')
        self.linked_list.append('pear')
        self.linked_list.print()

    def test_read_last(self):
        self.linked_list.append(3)
        self.linked_list.append(6)
        self.linked_list.append(8)
        self.assertEqual(8, self.linked_list.read_last())

        self.linked_list.delete(2)
        self.assertEqual(6, self.linked_list.read_last())

    def test_reverse(self):
        self.linked_list.append('a')
        self.linked_list.append('b')
        self.linked_list.append('c')
        self.linked_list.reverse()

        self.assertEqual('c', self.linked_list.read(0))
        self.assertEqual('b', self.linked_list.read(1))
        self.assertEqual('a', self.linked_list.read(2))


class TestDoublyLinkedList(TestLinkedList):
    def setUp(self) -> None:
        self.linked_list = DoublyLinkedList()

    def test_print_reversed(self):
        self.linked_list.append('apple')
        self.linked_list.append('orange')
        self.linked_list.append('pear')
        self.linked_list.print_reversed()

    def test_read_last(self):
        self.linked_list.append('a')
        self.linked_list.append('b')
        self.linked_list.append('c')

        self.assertEqual('c', self.linked_list.last_node.data)

    def test_reverse(self):
        pass
