"""
Test cases for Sum of Two Integers problem.
"""
import unittest
from src.leetcode.bit_manipulation.sum_of_two_integers import get_sum

class TestSumOfTwoIntegers(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(get_sum(1, 2), 3)

    def test_case_2(self):
        self.assertEqual(get_sum(-2, 3), 1)

    def test_case_3(self):
        self.assertEqual(get_sum(-1, -1), -2)

    def test_case_4(self):
        self.assertEqual(get_sum(0, 0), 0)

if __name__ == "__main__":
    unittest.main()