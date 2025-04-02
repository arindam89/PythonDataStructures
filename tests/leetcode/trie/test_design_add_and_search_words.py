# Test cases for Design Add and Search Words Data Structure
import unittest
from src.leetcode.trie.design_add_and_search_words import WordDictionary

class TestWordDictionary(unittest.TestCase):
    def setUp(self):
        self.word_dict = WordDictionary()

    def test_add_and_search(self):
        self.word_dict.add_word("bad")
        self.word_dict.add_word("dad")
        self.word_dict.add_word("mad")
        self.assertTrue(self.word_dict.search("bad"))  # Exact match
        self.assertFalse(self.word_dict.search("pad")) # Word does not exist
        self.assertTrue(self.word_dict.search(".ad"))  # Wildcard match
        self.assertTrue(self.word_dict.search("b.."))  # Wildcard match

    def test_empty_search(self):
        self.assertFalse(self.word_dict.search(""))  # Empty word should return False

if __name__ == "__main__":
    unittest.main()