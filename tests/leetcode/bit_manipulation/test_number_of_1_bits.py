"""
Test cases for Number of 1 Bits problem.
"""
import unittest
from src.leetcode.bit_manipulation.number_of_1_bits import hamming_weight

class TestNumberOf1Bits(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(hamming_weight(11), 3)  # Binary: 1011

    def test_case_2(self):
        self.assertEqual(hamming_weight(128), 1)  # Binary: 10000000

    def test_case_3(self):
        self.assertEqual(hamming_weight(4294967293), 31)  # Binary: 11111111111111111111111111111101

if __name__ == "__main__":
    unittest.main()