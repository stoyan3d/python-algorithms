from datastructures.queue import Queue

import unittest

class TestQueue(unittest.TestCase):
    def test_is_empty_on_queue_with_items(self):
        queue = Queue()

        queue.enqueue(2)
        self.assertFalse(queue.is_empty)

    def test_is_empty_on_empty_queue(self):
        queue = Queue()

        self.assertTrue(queue.is_empty)
        queue.enqueue(2)
        queue.dequeue()
        self.assertTrue(queue.is_empty)

    def test_queue_size(self):
        queue = Queue()

        queue.enqueue(1)
        queue.enqueue(5)
        queue.enqueue(9)

        self.assertEquals(3, queue.size)

    def test_read_on_empty_queue(self):
        queue = Queue()

        with self.assertRaises(IndexError) as c:
            queue.read()
        self.assertIn('The queue is empty', str(c.exception))

    def test_read_on_stack_with_items(self):
        queue = Queue()

        queue.enqueue(2)
        queue.enqueue(4)
        queue.enqueue(5)
        self.assertEquals(2, queue.read())
        queue.dequeue()
        self.assertEquals(4, queue.read())

    def test_enqueue(self):
        queue = Queue()

        queue.enqueue(3)
        queue.enqueue(7)
        self.assertEquals(3, queue.read())

        queue.dequeue()
        self.assertEquals(7, queue.read())

    def test_dequeue_on_empty_queue(self):
        queue = Queue()

        with self.assertRaises(IndexError) as c:
            queue.dequeue()
        self.assertIn('The queue is empty', str(c.exception))

    def test_dequeue_on_queue_with_items(self):
        queue = Queue()

        queue.enqueue('a')
        queue.enqueue('b')
        queue.enqueue('c')

        self.assertEquals('a', queue.dequeue())
        self.assertEquals('b', queue.dequeue())
        self.assertEquals('c', queue.dequeue())