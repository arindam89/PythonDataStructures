"""
Test cases for the Surrounded Regions problem.

Additional Notes:
- The test cases cover various scenarios, including:
  1. A grid with surrounded regions.
  2. A grid with no surrounded regions.
  3. A grid with all 'O's connected to the border.
  4. An empty grid.
"""

import unittest
from src.leetcode.graph.surrounded_regions import solve

class TestSurroundedRegions(unittest.TestCase):
    def test_surrounded_regions(self):
        board = [
            ['X', 'X', 'X', 'X'],
            ['X', 'O', 'O', 'X'],
            ['X', 'X', 'O', 'X'],
            ['X', 'O', 'X', 'X']
        ]
        expected = [
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X'],
            ['X', 'O', 'X', 'X']
        ]
        solve(board)
        self.assertEqual(board, expected)

    def test_no_surrounded_regions(self):
        board = [
            ['X', 'X', 'X'],
            ['X', 'O', 'X'],
            ['X', 'X', 'X']
        ]
        expected = [
            ['X', 'X', 'X'],
            ['X', 'O', 'X'],
            ['X', 'X', 'X']
        ]
        solve(board)
        self.assertEqual(board, expected)

    def test_all_connected_to_border(self):
        board = [
            ['O', 'O', 'O'],
            ['O', 'O', 'O'],
            ['O', 'O', 'O']
        ]
        expected = [
            ['O', 'O', 'O'],
            ['O', 'O', 'O'],
            ['O', 'O', 'O']
        ]
        solve(board)
        self.assertEqual(board, expected)

    def test_empty_grid(self):
        board = []
        expected = []
        solve(board)
        self.assertEqual(board, expected)

if __name__ == "__main__":
    unittest.main()