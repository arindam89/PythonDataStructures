"""
Test cases for Pow(x, n) problem.
"""
import unittest
from src.leetcode.math.pow_x_n import my_pow

class TestPowXN(unittest.TestCase):
    def test_case_1(self):
        self.assertAlmostEqual(my_pow(2.0, 10), 1024.0)

    def test_case_2(self):
        self.assertAlmostEqual(my_pow(2.1, 3), 9.261, places=3)

    def test_case_3(self):
        self.assertAlmostEqual(my_pow(2.0, -2), 0.25)

    def test_case_4(self):
        self.assertAlmostEqual(my_pow(1.0, 1000), 1.0)

if __name__ == "__main__":
    unittest.main()