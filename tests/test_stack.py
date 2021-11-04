from datastructures.stack import Stack
import unittest


class TestStack(unittest.TestCase):
    def test_is_empty_on_stack_with_items(self):
        stack = Stack()

        stack.push(2)
        self.assertFalse(stack.is_empty)

    def test_is_empty_on_empty_stack(self):
        stack = Stack()
        self.assertTrue(stack.is_empty)

        stack.push(2)
        stack.pop()
        self.assertTrue(stack.is_empty)

    def test_stack_size(self):
        stack = Stack()
        stack.push(1)
        stack.push(5)
        stack.push(9)

        self.assertEqual(3, stack.size)

    def test_read_on_stack_with_items(self):
        stack = Stack()
        stack.push('a')
        stack.push('c')

        self.assertEqual('c', stack.read())

    def test_read_on_empty_stack(self):
        stack = Stack()

        with self.assertRaises(IndexError) as c:
            stack.read()
        self.assertIn('Stack Empty', str(c.exception))

    def test_pop_on_empty_stack(self):
        stack = Stack()
        with self.assertRaises(IndexError) as c:
            stack.pop()
        self.assertIn('Stack Empty', str(c.exception))

    def test_pop_on_stack_with_few_items(self):
        stack = Stack()
        stack.push('a')
        stack.push('b')
        stack.push('c')

        popped_item = stack.pop()
        self.assertEqual('c', popped_item)

    def test_push_for_one_item(self):
        stack = Stack()
        stack.push(10)
        self.assertEqual(1, stack.size)
        self.assertEqual(10, stack.read())

    def test_stack_is_sequential(self):
        stack = Stack()
        stack.push('a')
        stack.push('b')
        stack.push('c')

        sequence = [stack.pop(), stack.pop(), stack.pop()]

        self.assertListEqual(['c', 'b', 'a'], sequence)


if __name__ == '__main__':
    unittest.main()