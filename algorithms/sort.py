def bubble_sort(array: list):
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
