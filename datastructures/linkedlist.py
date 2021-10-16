class Node:
    next_node = None
    data = None

    def __init__(self, data):
        self.data = data


class LinkedList:
    first_node = None

    def read(self, index: int):
        if not self.first_node:
            raise IndexError('Linked List index out of range')

        current_node = self.first_node
        for i in range(index):
            if current_node and current_node.next_node:
                current_node = current_node.next_node
            else:
                raise IndexError('Linked List index out of range')

        return current_node.data

    def insert(self, index: int, value):
        new_node = Node(value)

        if index == 0:
            new_node.next_node = self.first_node
            self.first_node = new_node
            return

        current_node = self.first_node
        for i in range(index-1):
            if current_node.next_node:
                current_node = current_node.next_node
            else:
                # We have reached the end of the linked list
                current_node.next_node = new_node
                return

        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

    def append(self, value):
        current_node = self.first_node
        new_node = Node(value)

        if not current_node:
            self.first_node = new_node
        else:
            while current_node.next_node:
                current_node = current_node.next_node

            current_node.next_node = new_node

    def index_of(self, value):
        index = 0
        current_node = self.first_node
        while current_node:
            if current_node.data == value:
                return index

            current_node = current_node.next_node
            index += 1

        return None

    def delete(self, index: int):
        if not self.first_node:
            raise IndexError('Linked List index out of range')

        if index == 0:
            self.first_node = self.first_node.next_node
            return

        current_node = self.first_node
        for i in range(index - 1):
            if current_node:
                current_node = current_node.next_node
            else:
                raise IndexError('Linked List index out of range')

        if current_node.next_node:
            current_node.next_node = current_node.next_node.next_node
        else:
            raise IndexError('Linked List index out of range')
