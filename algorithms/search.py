from typing import List
from .sort import partition


def linear_search(array: List[int], query: int) -> int:
    """Linear search works on any array.
    It returns the index of the given number in the array if it finds it.
    Returns -1 if it doesn't.
    It looks for the index by going over each array element and comparing it to the query.
    Time complexity: O(N)"""

    for i in range(len(array)):
        if array[i] == query:
            return i

    return -1


def binary_search(ordered_array: List[int], query: int) -> int:
    """Binary search works on ordered arrays.
    It returns the index of the given number in the array if it finds it.
    Returns -1 if it doesn't.
    We find the value in the middle of the array and we compare it to the query. If the query is
    smaller than the found value we find the mid point of the lower half and repeat the process.
    Time complexity: O(log(N))"""
    lower_bound = 0
    upper_bound = len(ordered_array) - 1

    while lower_bound <= upper_bound:
        mid_point_index = (lower_bound + upper_bound) // 2
        mid_point_value = ordered_array[mid_point_index]

        if mid_point_value == query:
            return mid_point_index
        elif mid_point_value < query:
            lower_bound = mid_point_index + 1
        elif mid_point_value > query:
            upper_bound = mid_point_index - 1

    return -1


def quick_select(array: List[float], nth_element: int) -> float:
    return quick_select_recursive(array, nth_element, 0, len(array) - 1)


def quick_select_recursive(array: List[float], nth_element: int, left_index: int, right_index: int) -> float:
    """
    Used for finding the nth element in an array. It uses a combination
    of partition and binary search.
    Time complexity: O(N)
    """
    if right_index - left_index <= 0:
        return array[left_index]

    pivot_index = partition(array, left_index, right_index)

    if nth_element < pivot_index:
        return quick_select_recursive(array, nth_element, left_index, pivot_index - 1)
    elif nth_element > pivot_index:
        return quick_select_recursive(array, nth_element, pivot_index + 1, right_index)
    else:
        return array[pivot_index]
