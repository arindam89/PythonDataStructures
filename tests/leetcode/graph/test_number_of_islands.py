"""
Test cases for the Number of Islands problem.

Additional Notes:
- The test cases cover various scenarios, including:
  1. A grid with multiple islands.
  2. A grid with no islands.
  3. A grid with a single large island.
  4. A grid with diagonal connections (not considered as islands).
"""

import unittest
from src.leetcode.graph.number_of_islands import num_islands

class TestNumberOfIslands(unittest.TestCase):
    def test_example_case(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        self.assertEqual(num_islands(grid), 3)

    def test_no_islands(self):
        grid = [
            ["0", "0", "0"],
            ["0", "0", "0"],
            ["0", "0", "0"]
        ]
        self.assertEqual(num_islands(grid), 0)

    def test_single_large_island(self):
        grid = [
            ["1", "1", "1"],
            ["1", "1", "1"],
            ["1", "1", "1"]
        ]
        self.assertEqual(num_islands(grid), 1)

    def test_diagonal_connections(self):
        grid = [
            ["1", "0", "1"],
            ["0", "1", "0"],
            ["1", "0", "1"]
        ]
        self.assertEqual(num_islands(grid), 5)

if __name__ == "__main__":
    unittest.main()