# Problem: Implement Trie (Prefix Tree)
# Link: https://leetcode.com/problems/implement-trie-prefix-tree/
#
# Approach:
# - Use a TrieNode class to represent each node in the Trie.
# - The Trie class will have methods to insert words, search for words, and check for prefixes.
# - Each node will store its children in a dictionary and a boolean to mark the end of a word.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert a word into the Trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """Search for a word in the Trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """Check if there is any word in the Trie that starts with the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True