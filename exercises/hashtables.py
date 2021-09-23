from typing import List


def get_intersection(array_1: list, array_2: list):
    array_hash = {}
    for item in array_1:
        array_hash[item] = True

    intersection = []
    for item in array_2:
        if array_hash.get(item):
            intersection.append(item)

    return intersection

array_1 = [1, 2, 3, 4, 5]
array_2 = [0, 2, 4, 6, 8]
print(get_intersection(array_1, array_2))


def find_duplicate(array: List[str]):
    array_hash = {}
    for item in array:
        if array_hash.get(item):
            return item
        else:
            array_hash[item] = True

array = ["a", "b", "c", "d", "c", "e", "f"]
print(find_duplicate(array))


def find_missing_letter(input: str):
    input_hash = {}
    for letter in input:
        input_hash[letter] = True

    alphabet = "abcdefghijklmnopqrstuvwxyz "
    for letter in alphabet:
        if not input_hash.get(letter):
            return letter

print(find_missing_letter("the quick brown box jumps over a lazy dog"))


def find_non_duplicate(input: str):
    input_hash = {}
    for letter in input:
        if letter in input_hash:
            input_hash[letter] += 1
        else:
            input_hash[letter] = 1
        
    for letter in input:
        if input_hash[letter] == 1:
            return letter

print(find_non_duplicate("minimum"))
