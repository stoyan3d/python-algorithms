from algorithms.search import binary_search, linear_search, quick_select

import unittest


class TestSearch(unittest.TestCase):
    def test_linear_search(self):
        array = [1, 4, 15, 6, 6, 18, 12, 10, 2, 7]

        self.assertEqual(5, linear_search(array, 18))
        self.assertEqual(-1, linear_search(array, 3))
        self.assertEqual(9, linear_search(array, 7))
        self.assertEqual(1, linear_search(array, 4))

    def test_binary_search(self):
        array = [1, 2, 3, 5, 6, 6, 9, 10, 11, 11, 15, 16, 18]
        self.assertEqual(3, binary_search(array, 5))
        self.assertEqual(7, binary_search(array, 10))
        self.assertEqual(-1, binary_search(array, 22))
        self.assertEqual(-1, binary_search(array, 4))

    def test_quick_select(self):
        array = [1, 3, 4, 7, 6, 5, 2]
        # Find the median
        self.assertEqual(4, quick_select(array, 3))
        # Find the lowest value
        self.assertEqual(1, quick_select(array, 0))
        # Find the highest value
        self.assertEqual(7, quick_select(array, len(array)-1))

