
def linear_search(array: list, query: int):
    """Linear search works on any array.
    It returns the index of the given number in the array if it finds it.
    Returns -1 if it doesn't.
    It looks for the index by going over each array element and comparing it to the query.
    Time complexity: O(N)"""

    for i in range(len(array)):
        if array[i] == query:
            return i

    return -1


def binary_search(ordered_array: list, query: int):
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