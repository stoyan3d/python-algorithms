from datastructures.queue import Queue, DoublyLinkedQueue

import unittest


class TestQueue(unittest.TestCase):
    def setUp(self) -> None:
        self.queue = Queue()

    def test_is_empty_on_queue_with_items(self):
        self.queue.enqueue(2)
        self.assertFalse(self.queue.is_empty)

    def test_is_empty_on_empty_queue(self):
        self.assertTrue(self.queue.is_empty)
        self.queue.enqueue(2)
        self.queue.dequeue()
        self.assertTrue(self.queue.is_empty)

    def test_queue_size(self):
        self.queue.enqueue(1)
        self.queue.enqueue(5)
        self.queue.enqueue(9)

        self.assertEqual(3, self.queue.size)

    def test_read_on_empty_queue(self):
        with self.assertRaises(IndexError) as c:
            self.queue.read()
        self.assertIn('The queue is empty', str(c.exception))

    def test_read_on_stack_with_items(self):
        self.queue.enqueue(2)
        self.queue.enqueue(4)
        self.queue.enqueue(5)
        self.assertEqual(2, self.queue.read())
        self.queue.dequeue()
        self.assertEqual(4, self.queue.read())

    def test_enqueue(self):
        self.queue.enqueue(3)
        self.queue.enqueue(7)
        self.assertEqual(3, self.queue.read())

        self.queue.dequeue()
        self.assertEqual(7, self.queue.read())

    def test_dequeue_on_empty_queue(self):
        with self.assertRaises(IndexError) as c:
            self.queue.dequeue()
        self.assertIn('The queue is empty', str(c.exception))

    def test_dequeue_on_queue_with_items(self):
        self.queue.enqueue('a')
        self.queue.enqueue('b')
        self.queue.enqueue('c')

        self.assertEqual('a', self.queue.dequeue())
        self.assertEqual('b', self.queue.dequeue())
        self.assertEqual('c', self.queue.dequeue())


class TestDoublyLinkedQueue(TestQueue):
    def setUp(self) -> None:
        self.queue = DoublyLinkedQueue()
