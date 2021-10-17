class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class DoublyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.previous_node = None
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.first_node = None

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
        new_node = LinkedListNode(value)

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
                new_node.previous_node = current_node
                current_node.next_node = new_node
                return

        new_node.previous_node = current_node
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

    def append(self, value):
        current_node = self.first_node
        new_node = LinkedListNode(value)

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


class DoublyLinkedList:
    @property
    def size(self) -> int:
        current_node = self.first_node
        current_index = 0
        while current_node:
            current_node = current_node.next_node
            current_index += 1

        return current_index

    def __init__(self):
        self.first_node = None
        self.last_node = None

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
        new_node = DoublyLinkedListNode(value)

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
        new_node = DoublyLinkedListNode(value)

        if not self.first_node:
            self.first_node, self.last_node = new_node, new_node
        else:
            new_node.previous_node = self.last_node
            self.last_node.next_node = new_node
            self.last_node = new_node

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
            removed_node = self.first_node
            self.first_node = self.first_node.next_node
            return removed_node.data

        current_node = self.first_node
        for i in range(index - 1):
            if current_node:
                current_node = current_node.next_node
            else:
                raise IndexError('Linked List index out of range')

        if current_node.next_node:
            current_node.next_node.next_node.previous_node = current_node
            current_node.next_node = current_node.next_node.next_node
        else:
            raise IndexError('Linked List index out of range')

