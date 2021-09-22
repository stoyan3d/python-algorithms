from algorithms.sort import bubble_sort, selection_sort

import unittest


def is_sorted(array: list):
    """A helper function to determine if an array is sorted"""
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False

    return True


class TestSort(unittest.TestCase):
    def test_bubble_sort(self):
        array_1 = [1, 4, 15, 6, 6, 18, 12, 10]
        self.assertTrue(is_sorted(bubble_sort(array_1)))

        array_2 = [4, 2, 7, 1, 3]
        self.assertTrue(is_sorted(bubble_sort(array_2)))

        array_3 = [18, 5, 15, 6, 6, 16, 12, 10, 2, 7]
        self.assertTrue(is_sorted(bubble_sort(array_3)))

    def test_selection_sort(self):
        array_1 = [1, 4, 15, 6, 6, 18, 12, 10]
        self.assertTrue(is_sorted(selection_sort(array_1)))

        array_2 = [4, 2, 7, 1, 3]
        self.assertTrue(is_sorted(selection_sort(array_2)))

        array_3 = [18, 5, 15, 6, 6, 16, 12, 10, 2, 7]
        self.assertTrue(is_sorted(selection_sort(array_3)))