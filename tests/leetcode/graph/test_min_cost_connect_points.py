"""
Test cases for the Min Cost to Connect All Points problem.

Additional Notes:
- The test cases cover various scenarios, including:
  1. A simple case with two points.
  2. A case with multiple points forming a grid.
  3. A case with points aligned in a straight line.
  4. A single point (no cost).
"""

import unittest
from src.leetcode.graph.min_cost_connect_points import min_cost_connect_points

class TestMinCostConnectPoints(unittest.TestCase):
    def test_two_points(self):
        points = [[0, 0], [2, 2]]
        self.assertEqual(min_cost_connect_points(points), 4)

    def test_grid_points(self):
        points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
        self.assertEqual(min_cost_connect_points(points), 20)

    def test_straight_line(self):
        points = [[0, 0], [1, 0], [2, 0], [3, 0]]
        self.assertEqual(min_cost_connect_points(points), 3)

    def test_single_point(self):
        points = [[0, 0]]
        self.assertEqual(min_cost_connect_points(points), 0)

if __name__ == "__main__":
    unittest.main()