"""
Test cases for Missing Number problem.
"""
import unittest
from src.leetcode.bit_manipulation.missing_number import missing_number

class TestMissingNumber(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(missing_number([3, 0, 1]), 2)

    def test_case_2(self):
        self.assertEqual(missing_number([0, 1]), 2)

    def test_case_3(self):
        self.assertEqual(missing_number([9,6,4,2,3,5,7,0,1]), 8)

    def test_case_4(self):
        self.assertEqual(missing_number([0]), 1)

if __name__ == "__main__":
    unittest.main()