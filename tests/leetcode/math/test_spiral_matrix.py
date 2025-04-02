"""
Test cases for Spiral Matrix problem.
"""
import unittest
from src.leetcode.math.spiral_matrix import spiral_order

class TestSpiralMatrix(unittest.TestCase):
    def test_case_1(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(spiral_order(matrix), [1, 2, 3, 6, 9, 8, 7, 4, 5])

    def test_case_2(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
        self.assertEqual(spiral_order(matrix), [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])

    def test_case_3(self):
        matrix = [[1]]
        self.assertEqual(spiral_order(matrix), [1])

    def test_case_4(self):
        matrix = [
            [1, 2],
            [3, 4]
        ]
        self.assertEqual(spiral_order(matrix), [1, 2, 4, 3])

if __name__ == "__main__":
    unittest.main()