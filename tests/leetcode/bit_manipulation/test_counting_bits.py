"""
Test cases for Counting Bits problem.
"""
import unittest
from src.leetcode.bit_manipulation.counting_bits import count_bits

class TestCountingBits(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(count_bits(2), [0, 1, 1])

    def test_case_2(self):
        self.assertEqual(count_bits(5), [0, 1, 1, 2, 1, 2])

    def test_case_3(self):
        self.assertEqual(count_bits(0), [0])

if __name__ == "__main__":
    unittest.main()