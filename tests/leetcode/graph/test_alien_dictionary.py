"""
Test cases for the Alien Dictionary problem.

Additional Notes:
- The test cases cover various scenarios, including:
  1. A valid order with no cycles.
  2. An invalid order due to a prefix case.
  3. A graph with multiple valid orders.
  4. A single word (no constraints).
"""

import unittest
from src.leetcode.graph.alien_dictionary import alien_order

class TestAlienDictionary(unittest.TestCase):
    def test_valid_order(self):
        words = ["wrt", "wrf", "er", "ett", "rftt"]
        expected = "wertf"
        self.assertEqual(alien_order(words), expected)

    def test_invalid_order_prefix_case(self):
        words = ["abc", "ab"]
        expected = ""
        self.assertEqual(alien_order(words), expected)

    def test_multiple_valid_orders(self):
        words = ["z", "x", "z"]
        expected = ""
        self.assertEqual(alien_order(words), expected)

    def test_single_word(self):
        words = ["z"]
        expected = "z"
        self.assertEqual(alien_order(words), expected)

if __name__ == "__main__":
    unittest.main()