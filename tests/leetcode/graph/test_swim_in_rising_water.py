"""
Test cases for the Swim in Rising Water problem.

Additional Notes:
- The test cases cover various scenarios, including:
  1. A simple 2x2 grid.
  2. A grid with increasing elevations.
  3. A grid with decreasing elevations.
  4. A grid with equal elevations.
"""

import unittest
from src.leetcode.graph.swim_in_rising_water import swim_in_water

class TestSwimInRisingWater(unittest.TestCase):
    def test_simple_grid(self):
        grid = [
            [0, 2],
            [1, 3]
        ]
        self.assertEqual(swim_in_water(grid), 3)

    def test_increasing_elevations(self):
        grid = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]
        ]
        self.assertEqual(swim_in_water(grid), 8)

    def test_decreasing_elevations(self):
        grid = [
            [8, 7, 6],
            [5, 4, 3],
            [2, 1, 0]
        ]
        self.assertEqual(swim_in_water(grid), 8)

    def test_equal_elevations(self):
        grid = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        self.assertEqual(swim_in_water(grid), 1)

if __name__ == "__main__":
    unittest.main()