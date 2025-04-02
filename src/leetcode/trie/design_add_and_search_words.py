# Problem: Design Add and Search Words Data Structure
# Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/
#
# Approach:
# - Use a TrieNode class to represent each node in the Trie.
# - The WordDictionary class will have methods to add words and search for words.
# - The search method will support '.' as a wildcard character, which can match any letter.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        """Add a word to the data structure."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """Search for a word in the data structure. Supports '.' as a wildcard character."""
        def dfs(index, node):
            if index == len(word):
                return node.is_end_of_word

            char = word[index]
            if char == '.':
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(index + 1, node.children[char])

        return dfs(0, self.root)