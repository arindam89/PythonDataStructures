"""
Test cases for Plus One problem.
"""
import unittest
from src.leetcode.math.plus_one import plus_one

class TestPlusOne(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(plus_one([1, 2, 3]), [1, 2, 4])

    def test_case_2(self):
        self.assertEqual(plus_one([4, 3, 2, 1]), [4, 3, 2, 2])

    def test_case_3(self):
        self.assertEqual(plus_one([9, 9, 9]), [1, 0, 0, 0])

    def test_case_4(self):
        self.assertEqual(plus_one([0]), [1])

if __name__ == "__main__":
    unittest.main()