from typing import Optional


class TreeNode:
    def __init__(self, value: float) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    A tree data structure that organizes values that are smaller than the root on the left
    side and values that are bigger on the right. It allows for very efficient insert, search
    and delete operations.
    Operation   Average     Worst
    Search		O(log n)	O(n)
    Insert		O(log n)	O(n)
    Delete		O(log n)	O(n)
    """
    def __init__(self) -> None:
        self.root = None
        
    def search(self, value: float) -> bool:
        return self.search_recursive(value, self.root)

    def search_recursive(self, value: float, node: TreeNode) -> bool:
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self.search_recursive(value, node.left)
        else:
            return self.search_recursive(value, node.right)            

    def insert(self, value: float) -> bool:
        if self.root:
            return self.insert_recursive(value, self.root)
        else:
            self.root = TreeNode(value)
            return True

    def insert_recursive(self, value: float, node: TreeNode) -> bool:
        if value == node.value:
            # The data is already there
            return False
        elif value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
                return True
            else:
                return self.insert_recursive(value, node.left)
        else:
            if node.right is None:
                node.right = TreeNode(value)
                return True
            else:
                return self.insert_recursive(value, node.right)

    def delete(self, value):
        self.delete_recursive(value, self.root)

    def delete_recursive(self, value: float, node: TreeNode) -> Optional[TreeNode]:
        if node is None:
            return None
        elif value < node.value:
            node.left = self.delete_recursive(value, node.left)
            return node
        elif value > node.value:
            node.right = self.delete_recursive(value, node.right)
            return node
        elif value == node.value:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.right = self.lift(node.right, node)

    def lift(self, node: TreeNode, node_to_delete: TreeNode) -> TreeNode:
        if node.left:
            node.left = self.lift(node.left, node_to_delete)
            return node

    def traverse_and_print_in_order(self, node: TreeNode) -> None:
        if node is None:
            return

        self.traverse_and_print_in_order(node.left)
        print(node.value)
        self.traverse_and_print_in_order(node.right)

    def max(self) -> float:
        return self.max_recursive(self.root)

    def max_recursive(self, node: TreeNode) -> float:
        if node.right:
            return self.max_recursive(node.right)
        else:
            return node.value

    def min(self) -> float:
        return self.min_recursive(self.root)

    def min_recursive(self, node: TreeNode) -> float:
        if node.left:
            return self.min_recursive(node.left)
        else:
            return node.value
