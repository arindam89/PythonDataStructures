# Test cases for Implement Trie (Prefix Tree)
import unittest
from src.leetcode.trie.implement_trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_insert_and_search(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("apple"))  # Word exists
        self.assertFalse(self.trie.search("app"))   # Prefix but not a word

    def test_starts_with(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.starts_with("app"))  # Prefix exists
        self.assertFalse(self.trie.starts_with("apl")) # Prefix does not exist

    def test_multiple_words(self):
        self.trie.insert("apple")
        self.trie.insert("app")
        self.assertTrue(self.trie.search("app"))  # Word exists
        self.assertTrue(self.trie.starts_with("app"))  # Prefix exists
        self.assertFalse(self.trie.search("appl"))  # Prefix but not a word

if __name__ == "__main__":
    unittest.main()