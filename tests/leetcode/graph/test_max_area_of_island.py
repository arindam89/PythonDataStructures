"""
Test cases for the Max Area of Island problem.

Additional Notes:
- The test cases cover various scenarios, including:
  1. A grid with multiple islands of different sizes.
  2. A grid with no islands.
  3. A grid with a single large island.
  4. A grid with islands of size 1.
"""

import unittest
from src.leetcode.graph.max_area_of_island import max_area_of_island

class TestMaxAreaOfIsland(unittest.TestCase):
    def test_example_case(self):
        grid = [
            [0, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]
        ]
        self.assertEqual(max_area_of_island(grid), 4)

    def test_no_islands(self):
        grid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(max_area_of_island(grid), 0)

    def test_single_large_island(self):
        grid = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        self.assertEqual(max_area_of_island(grid), 9)

    def test_islands_of_size_one(self):
        grid = [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]
        ]
        self.assertEqual(max_area_of_island(grid), 1)

if __name__ == "__main__":
    unittest.main()