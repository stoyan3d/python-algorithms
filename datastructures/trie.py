from typing import List, Optional


class TrieNode:
    def __init__(self) -> None:
        self.children = {}


class Trie:
    """A trie is an efficient tree data structure for doing autocomplete and autocorrect.
    Both operations are done with time complexity O(K) where K is the length of the
    word we pass to the algorithm."""

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current_node = self.root
        for char in word:
            if current_node.children.get(char):
                current_node = current_node.children[char]
            else:
                new_node = TrieNode()
                current_node.children[char] = new_node
                current_node = new_node

        current_node.children["*"] = None

    def auto_complete(self, prefix: str) -> List[str]:
        current_node = self.search(prefix)
        if not current_node:
            return []
        return self.collect_all_words_recursive(current_node, word=prefix)

    def search(self, word: str) -> Optional[TrieNode]:
        current_node = self.root

        for char in word:
            if current_node.children.get(char):
                current_node = current_node.children[char]
            else:
                return None

        return current_node

    def collect_all_words_recursive(self, node: TrieNode = None, word="", words: List[str] = None) -> List[str]:
        if words is None:
            words = []

        current_node = node or self.root

        for key, child_node in current_node.children.items():
            if key == "*":
                words.append(word)
            else:
                self.collect_all_words_recursive(child_node, word + key, words)

        return words

    def auto_correct(self, word: str) -> Optional[str]:
        for i in range(len(word) - 1, 0, -1):
            suggestions = self.auto_complete(word[:i])
            if suggestions:
                return suggestions[0]

        return None
