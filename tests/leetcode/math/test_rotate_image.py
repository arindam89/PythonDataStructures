"""
Test cases for Rotate Image problem.
"""
import unittest
from src.leetcode.math.rotate_image import rotate

class TestRotateImage(unittest.TestCase):
    def test_case_1(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        rotate(matrix)
        self.assertEqual(matrix, [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ])

    def test_case_2(self):
        matrix = [
            [5, 1, 9, 11],
            [2, 4, 8, 10],
            [13, 3, 6, 7],
            [15, 14, 12, 16]
        ]
        rotate(matrix)
        self.assertEqual(matrix, [
            [15, 13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7, 10, 11]
        ])

    def test_case_3(self):
        matrix = [[1]]
        rotate(matrix)
        self.assertEqual(matrix, [[1]])

    def test_case_4(self):
        matrix = [
            [1, 2],
            [3, 4]
        ]
        rotate(matrix)
        self.assertEqual(matrix, [
            [3, 1],
            [4, 2]
        ])

if __name__ == "__main__":
    unittest.main()