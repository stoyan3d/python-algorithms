from .linkedlist import DoublyLinkedList


class Queue:
    @property
    def size(self) -> int:
        return len(self.data)

    @property
    def is_empty(self) -> bool:
        return self.size == 0

    def __init__(self):
        self.data = []

    def enqueue(self, element):
        self.data.append(element)

    def dequeue(self):
        if self.is_empty:
            raise IndexError('The queue is empty')
        else:
            return self.data.pop(0)

    def read(self):
        if self.is_empty:
            return None
        else:
            return self.data[0]


class DoublyLinkedQueue:
    @property
    def size(self) -> int:
        return self.data.size

    @property
    def is_empty(self) -> bool:
        return self.data.first_node is None

    def __init__(self):
        self.data = DoublyLinkedList()

    def enqueue(self, element):
        self.data.append(element)

    def dequeue(self):
        if self.is_empty:
            raise IndexError('The queue is empty')
        else:
            return self.data.delete(0)

    def read(self):
        if self.is_empty:
            return None
        else:
            return self.data.read(0)

