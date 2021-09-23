class Stack():
    @property
    def size(self) -> int:
        return len(self.data)

    @property
    def is_empty(self) -> bool:
        return self.size == 0

    def __init__(self) -> None:
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.is_empty:
            raise IndexError('Stack Empty')
        else:
            return self.data.pop()

    def read(self):
        if self.is_empty:
            raise IndexError('Stack Empty')
        else:
            return self.data[-1]

