"""
Test cases for the LeetCode problem: Last Stone Weight
Link: https://leetcode.com/problems/last-stone-weight/

The test cases validate the following scenarios:
1. A single stone remains after all collisions.
2. All stones are destroyed.
3. No stones are provided initially.
4. Only one stone is provided initially.
"""

import unittest
from src.leetcode.heaps.last_stone_weight import last_stone_weight

class TestLastStoneWeight(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(last_stone_weight([2, 7, 4, 1, 8, 1]), 1)  # Example from problem statement

    def test_case_2(self):
        self.assertEqual(last_stone_weight([1, 1]), 0)  # All stones are destroyed

    def test_case_3(self):
        self.assertEqual(last_stone_weight([]), 0)  # No stones provided

    def test_case_4(self):
        self.assertEqual(last_stone_weight([10]), 10)  # Only one stone provided

if __name__ == "__main__":
    unittest.main()