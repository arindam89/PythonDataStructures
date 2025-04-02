"""
Test cases for the Rotting Oranges problem.

Additional Notes:
- The test cases cover various scenarios, including:
  1. A grid where all oranges rot.
  2. A grid where not all oranges can rot.
  3. A grid with no fresh oranges.
  4. An empty grid.
"""

import unittest
from src.leetcode.graph.rotting_oranges import oranges_rotting

class TestOrangesRotting(unittest.TestCase):
    def test_all_oranges_rot(self):
        grid = [
            [2, 1, 1],
            [1, 1, 0],
            [0, 1, 1]
        ]
        self.assertEqual(oranges_rotting(grid), 4)

    def test_not_all_oranges_rot(self):
        grid = [
            [2, 1, 1],
            [0, 0, 1],
            [1, 0, 1]
        ]
        self.assertEqual(oranges_rotting(grid), -1)

    def test_no_fresh_oranges(self):
        grid = [
            [2, 2, 0],
            [2, 2, 0],
            [0, 0, 0]
        ]
        self.assertEqual(oranges_rotting(grid), 0)

    def test_empty_grid(self):
        grid = []
        self.assertEqual(oranges_rotting(grid), -1)

if __name__ == "__main__":
    unittest.main()