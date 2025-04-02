"""
Test cases for Happy Number problem.
"""
import unittest
from src.leetcode.math.happy_number import is_happy

class TestHappyNumber(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(is_happy(19))

    def test_case_2(self):
        self.assertFalse(is_happy(2))

    def test_case_3(self):
        self.assertTrue(is_happy(1))

    def test_case_4(self):
        self.assertFalse(is_happy(20))

if __name__ == "__main__":
    unittest.main()