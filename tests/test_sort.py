from typing import List
from algorithms.sort import bubble_sort, selection_sort, insertion_sort, quick_sort, partition

import unittest


def is_sorted(array: List[float]):
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

    def test_insertion_sort(self):
        array_1 = [1, 4, 15, 6, 6, 18, 12, 10]
        self.assertTrue(is_sorted(insertion_sort(array_1)))

        array_2 = [4, 2, 7, 1, 3]
        self.assertTrue(is_sorted(insertion_sort(array_2)))

        array_3 = [18, 5, 15, 6, 6, 16, 12, 10, 2, 7]
        self.assertTrue(is_sorted(insertion_sort(array_3)))

    def test_quick_sort(self):
        array_1 = [1, 4, 15, 6, 6, 18, 12, 10]
        self.assertTrue(is_sorted(quick_sort(array_1)))

        array_2 = [4, 2, 7, 1, 3]
        self.assertTrue(is_sorted(quick_sort(array_2)))

        array_3 = [18, 5, 15, 6, 6, 16, 12, 10, 2, 7]
        self.assertTrue(is_sorted(quick_sort(array_3)))


class TestSortHelpers(unittest.TestCase):
    def test_partition(self):
        array_1 = [0, 5, 2, 1, 6, 3]
        array_1_partitioned = [0, 1, 2, 3, 6, 5]

        pivot_index = partition(array_1, 0, len(array_1) - 1)
        self.assertEqual(3, pivot_index)
        self.assertListEqual(array_1_partitioned, array_1)