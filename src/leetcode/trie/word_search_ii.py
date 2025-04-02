# Problem: Word Search II
# Link: https://leetcode.com/problems/word-search-ii/
#
# Approach:
# - Use a Trie to store all the words from the input list for efficient prefix matching.
# - Perform a DFS on the board to find all words that exist in the Trie.
# - Use a set to avoid duplicate words in the result.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

class Solution:
    def find_words(self, board: list[list[str]], words: list[str]) -> list[str]:
        """Find all words from the list that can be formed on the board."""
        def dfs(x, y, node, path):
            if node.is_end_of_word:
                result.add(path)

            if not (0 <= x < len(board) and 0 <= y < len(board[0])) or board[x][y] == "#":
                return

            char = board[x][y]
            if char not in node.children:
                return

            board[x][y] = "#"  # Mark as visited
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(x + dx, y + dy, node.children[char], path + char)
            board[x][y] = char  # Restore the cell

        # Build the Trie
        trie = Trie()
        for word in words:
            trie.insert(word)

        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, trie.root, "")

        return list(result)