"""
Test cases for Reverse Integer problem.
"""
import unittest
from src.leetcode.bit_manipulation.reverse_integer import reverse

class TestReverseInteger(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(reverse(123), 321)

    def test_case_2(self):
        self.assertEqual(reverse(-123), -321)

    def test_case_3(self):
        self.assertEqual(reverse(120), 21)

    def test_case_4(self):
        self.assertEqual(reverse(0), 0)

    def test_case_5(self):
        self.assertEqual(reverse(1534236469), 0)  # Overflow case

if __name__ == "__main__":
    unittest.main()