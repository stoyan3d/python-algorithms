from typing import List


def print_every_other_number(low: int, high: int):
    if low > high:
        return
    
    print(low)
    print_every_other_number(low+2, high)

# print_every_other_number(0, 10)

def count_characters_in_array_of_strings(array: List[str]) -> int:
    if len(array) == 0:
        return 0

    return len(array[0]) + count_characters_in_array_of_strings(array[1:])

array_of_strings = ['ab', 'c', 'def', 'ghij']
# print(count_characters_in_array_of_strings(array_of_strings))

def get_even_numbers_in_array(array: List[int]):
    if len(array) == 0:
        return []

    even_numbers = get_even_numbers_in_array(array[1:])
    if array[0] % 2 == 0:
        even_numbers.append(array[0])

    return even_numbers

array_of_numbers = [2, 5, 6, 7, 8, 9, 12, 15]
# print(get_even_numbers_in_array(array_of_numbers))

def get_triangular_number(n: int) -> int:
    if n == 1:
        return 1

    return get_triangular_number(n-1) + n

# print(get_triangular_number(7))

def get_index_of_x(input: str, index: int = 0):
    if input[0] == 'x':
        return index
    else:
        return get_index_of_x(input[1:], index + 1)

# print(get_index_of_x('aaioasdxj'))

def unique_paths(rows: int, columns: int, memo={}) -> int:
    if rows == 1 or columns == 1:
        return 1
    
    if not memo.get((rows, columns)):
        memo[(rows, columns)] = unique_paths(rows-1, columns) + unique_paths(rows, columns-1) 
    return memo[(rows, columns)]

print(unique_paths(7, 3))