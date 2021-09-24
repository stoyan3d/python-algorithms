from datastructures.stack import Stack


def reverse_string(input: str) -> str:
    input_stack = Stack()
    for letter in input:
        input_stack.push(letter)

    reversed_string = ''
    while not input_stack.is_empty:
        reversed_string += input_stack.pop()

    return reversed_string


print(reverse_string('Hello'))