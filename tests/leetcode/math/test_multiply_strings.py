"""
Test cases for Multiply Strings problem.
"""
import unittest
from src.leetcode.math.multiply_strings import multiply

class TestMultiplyStrings(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(multiply("2", "3"), "6")

    def test_case_2(self):
        self.assertEqual(multiply("123", "456"), "56088")

    def test_case_3(self):
        self.assertEqual(multiply("0", "1234"), "0")

    def test_case_4(self):
        self.assertEqual(multiply("999", "999"), "998001")

if __name__ == "__main__":
    unittest.main()