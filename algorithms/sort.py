def bubble_sort(array: list):
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


def selection_sort(array: list):
    """
    Iterate through an array and search for the index of the number
    with the lowest value. At the end of the iteration swap the first number
    of the iteration with the lower number. This algorithm is 2x faster than
    bubble sort even though Big O doesn't reflect it.
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
