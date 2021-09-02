from algorithms.sort import bubble_sort

import unittest


def is_sorted(array: list):
    """A helper function to determine if an array is sorted"""
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False

    return True


class TestSort(unittest.TestCase):
    def test_bubble_sort(self):
        array = [1, 4, 15, 6, 6, 18, 12, 10]
        sorted_array = [1, 4, 6, 6, 10, 12, 15, 18]
        self.assertListEqual(sorted_array, bubble_sort(array))

