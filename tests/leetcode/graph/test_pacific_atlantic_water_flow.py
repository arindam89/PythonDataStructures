"""
Test cases for the Pacific Atlantic Water Flow problem.

Additional Notes:
- The test cases cover various scenarios, including:
  1. A grid with multiple cells flowing to both oceans.
  2. A grid with no cells flowing to both oceans.
  3. A single-cell grid.
  4. A grid with all cells flowing to both oceans.
"""

import unittest
from src.leetcode.graph.pacific_atlantic_water_flow import pacific_atlantic

class TestPacificAtlantic(unittest.TestCase):
    def test_example_case(self):
        heights = [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4]
        ]
        expected = [
            (0, 4), (1, 3), (1, 4), (2, 2), (3, 0), (3, 1), (4, 0)
        ]
        result = pacific_atlantic(heights)
        self.assertCountEqual(result, expected)

    def test_no_cells_flow_to_both_oceans(self):
        heights = [
            [5, 4, 3],
            [4, 3, 2],
            [3, 2, 1]
        ]
        expected = []
        result = pacific_atlantic(heights)
        self.assertEqual(result, expected)

    def test_single_cell(self):
        heights = [[1]]
        expected = [(0, 0)]
        result = pacific_atlantic(heights)
        self.assertCountEqual(result, expected)

    def test_all_cells_flow_to_both_oceans(self):
        heights = [
            [1, 1],
            [1, 1]
        ]
        expected = [
            (0, 0), (0, 1), (1, 0), (1, 1)
        ]
        result = pacific_atlantic(heights)
        self.assertCountEqual(result, expected)

if __name__ == "__main__":
    unittest.main()