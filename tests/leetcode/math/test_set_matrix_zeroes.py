"""
Test cases for Set Matrix Zeroes problem.
"""
import unittest
from src.leetcode.math.set_matrix_zeroes import set_zeroes

class TestSetMatrixZeroes(unittest.TestCase):
    def test_case_1(self):
        matrix = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
        set_zeroes(matrix)
        self.assertEqual(matrix, [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]
        ])

    def test_case_2(self):
        matrix = [
            [0, 1, 2, 0],
            [3, 4, 5, 2],
            [1, 3, 1, 5]
        ]
        set_zeroes(matrix)
        self.assertEqual(matrix, [
            [0, 0, 0, 0],
            [0, 4, 5, 0],
            [0, 3, 1, 0]
        ])

    def test_case_3(self):
        matrix = [[1]]
        set_zeroes(matrix)
        self.assertEqual(matrix, [[1]])

    def test_case_4(self):
        matrix = [[0]]
        set_zeroes(matrix)
        self.assertEqual(matrix, [[0]])

if __name__ == "__main__":
    unittest.main()