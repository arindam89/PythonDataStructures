# Test cases for Word Search II
import unittest
from src.leetcode.trie.word_search_ii import Solution

class TestWordSearchII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_find_words(self):
        board = [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"]
        ]
        words = ["oath", "pea", "eat", "rain"]
        expected = ["oath", "eat"]
        result = self.solution.find_words(board, words)
        self.assertCountEqual(result, expected)  # Check if the result matches expected words

    def test_no_words_found(self):
        board = [
            ["a", "b"],
            ["c", "d"]
        ]
        words = ["efg", "hij"]
        expected = []
        result = self.solution.find_words(board, words)
        self.assertEqual(result, expected)  # No words should be found

if __name__ == "__main__":
    unittest.main()