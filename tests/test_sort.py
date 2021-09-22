from random import randint
from algorithms.sort import bubble_sort, selection_sort, insertion_sort

import unittest


def is_sorted(array: list):
    """A helper function to determine if an array is sorted"""
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False

    return True

def get_random_array(array_length: int = 10):
    """A helper function for generating an unsorted array of random int values."""
    return [randint(0, 100) for i in range(array_length)]


class TestSort(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertTrue(is_sorted(bubble_sort(get_random_array())))
        self.assertTrue(is_sorted(bubble_sort(get_random_array())))
        self.assertTrue(is_sorted(bubble_sort(get_random_array())))

    def test_selection_sort(self):
        self.assertTrue(is_sorted(selection_sort(get_random_array())))
        self.assertTrue(is_sorted(selection_sort(get_random_array())))
        self.assertTrue(is_sorted(selection_sort(get_random_array())))

    def test_insertion_sort(self):
        self.assertTrue(is_sorted(insertion_sort(get_random_array())))
        self.assertTrue(is_sorted(insertion_sort(get_random_array())))
        self.assertTrue(is_sorted(insertion_sort(get_random_array())))