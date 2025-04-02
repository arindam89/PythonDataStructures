"""
Test cases for Single Number problem.
"""
import unittest
from src.leetcode.bit_manipulation.single_number import single_number

class TestSingleNumber(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(single_number([2, 2, 1]), 1)

    def test_case_2(self):
        self.assertEqual(single_number([4, 1, 2, 1, 2]), 4)

    def test_case_3(self):
        self.assertEqual(single_number([1]), 1)

if __name__ == "__main__":
    unittest.main()