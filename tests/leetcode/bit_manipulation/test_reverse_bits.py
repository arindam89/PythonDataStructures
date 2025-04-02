"""
Test cases for Reverse Bits problem.
"""
import unittest
from src.leetcode.bit_manipulation.reverse_bits import reverse_bits

class TestReverseBits(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(reverse_bits(43261596), 964176192)  # Binary: 00000010100101000001111010011100 -> 00111001011110000010100101000000

    def test_case_2(self):
        self.assertEqual(reverse_bits(4294967293), 3221225471)  # Binary: 11111111111111111111111111111101 -> 10111111111111111111111111111111

if __name__ == "__main__":
    unittest.main()