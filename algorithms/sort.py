from typing import List

def bubble_sort(array: List[float]):
    """ A sorting algorithm that iterates through an array
    and swaps two items if the first is smaller than the next.
    Time complexity: O(N^2)
    """
    unsorted_until_index = len(array) - 1
    array_sorted = False

    while not array_sorted:
        array_sorted = True
        for i in range(unsorted_until_index):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                array_sorted = False

        unsorted_until_index -= 1

    return array


def selection_sort(array: List[float]):
    """
    Iterate through an array and search for the index of the number
    with the lowest value. At the end of the iteration swap the first number
    of the iteration with the lower number. We then iterate again through the rest of the array.
    This algorithm is 2x faster than bubble sort even though Big O doesn't reflect it.
    Time complexity: O(N^2)
    """
    for i in range(len(array)):
        lowest_value_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[lowest_value_index]:
                lowest_value_index = j

        if lowest_value_index != i:
            array[i], array[lowest_value_index] = array[lowest_value_index], array[i]

    return array


def insertion_sort(array: List[float]):
    """
    Iterate through each number of the array starting from index 1
    and check if it's bigger than the previous ones. If a bigger one is found,
    shift the number to the left.
    This algorithm runs faster than selection sort in best case scenarios
    compared to selection sort but slower in worst case scenarios.
    It's most effective with mostly sorted arrays.
    Time complexity: O(N^2)
    """

    for i in range(1, len(array)):
        position_index = i - 1
        temp_value = array[i]

        while position_index >= 0:
            if temp_value < array[position_index]:
                array[position_index + 1] = array[position_index]
                position_index -= 1
            else:
                break

            array[position_index + 1] = temp_value

    return array
