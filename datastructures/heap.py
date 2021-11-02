class Heap:
    """A heap is a loosly sorted tree structure that is has efficient insertion and largest
    element deletion. It is the most efficient data structure for Priority Queues.
    It has similar time efficiency as a Binary Search Tree but we always know what the largest
    element is."""
    def __init__(self) -> None:
        self.data = []

    def insert(self, value: float) -> None:
        self.data.append(value)
        self.trickle_up(len(self.data) - 1)

    def trickle_up(self, index: int) -> None:
        while self.get_parent(index):
            if self.data[index] > self.get_parent(index):
                parent_index = self.get_parent_index(index)
                self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
            index = self.get_parent_index(index)

    def get_parent(self, index: int) -> float:
        if index <= 0:
            return None

        parent_index = self.get_parent_index(index)
        return self.data[parent_index]

    def get_parent_index(self, index: int) -> int:
        return int((index - 1) / 2)

    def read(self) -> float:
        return self.data[0]

    def delete(self) -> float:
        root_node = self.data[0]
        last_node = self.data.pop()
        self.data[0] = last_node

        self.trickle_down(0)

        return root_node

    def trickle_down(self, index: int) -> None:
        while self.get_left(index):
            max_child_index = self.get_max_child_index(index)
            if self.data[index] < self.data[max_child_index]:
                self.data[index], self.data[max_child_index] = self.data[max_child_index], self.data[index]

            index = max_child_index

    def get_max_child_index(self, index: int) -> int:
        if not self.get_right(index):
            return self.get_left_index(index)
        
        if self.get_left(index) < self.get_right(index):
            return self.get_right_index(index)
        else:
            return self.get_left_index(index)

    def get_left(self, index: int) -> float:
        left_index = self.get_left_index(index)

        if len(self.data) > left_index:
            return self.data[left_index]
        else:
            return None
    
    def get_left_index(self, index: int) -> float:
        return 2 * index + 1

    def get_right(self, index: int) -> float:
        right_index = self.get_right_index(index)
        
        if len(self.data) > right_index:
            return self.data[right_index]
        else:
            return None

    def get_right_index(self, index: int) -> float:
        return 2 * index + 2