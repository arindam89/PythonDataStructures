import unittest
from src.leetcode.binary_search.search_2d_matrix import search_matrix

class TestSearchMatrix(unittest.TestCase):
    def test_target_found(self):
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 60]
        ]
        self.assertTrue(search_matrix(matrix, 3))

    def test_target_not_found(self):
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 60]
        ]
        self.assertFalse(search_matrix(matrix, 13))

    def test_empty_matrix(self):
        self.assertFalse(search_matrix([], 1))

    def test_single_element_found(self):
        self.assertTrue(search_matrix([[1]], 1))

    def test_single_element_not_found(self):
        self.assertFalse(search_matrix([[1]], 2))

if __name__ == "__main__":
    unittest.main()