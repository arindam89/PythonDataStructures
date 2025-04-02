"""
Test cases for the Walls and Gates problem.

Additional Notes:
- The test cases cover various scenarios, including:
  1. A grid with multiple gates and empty rooms.
  2. A grid with no gates.
  3. A grid with all gates.
  4. An empty grid.
"""

import unittest
from src.leetcode.graph.walls_and_gates import walls_and_gates

class TestWallsAndGates(unittest.TestCase):
    def test_multiple_gates(self):
        INF = 2**31 - 1
        rooms = [
            [INF, -1, 0, INF],
            [INF, INF, INF, -1],
            [INF, -1, INF, -1],
            [0, -1, INF, INF]
        ]
        expected = [
            [3, -1, 0, 1],
            [2, 2, 1, -1],
            [1, -1, 2, -1],
            [0, -1, 3, 4]
        ]
        walls_and_gates(rooms)
        self.assertEqual(rooms, expected)

    def test_no_gates(self):
        INF = 2**31 - 1
        rooms = [
            [INF, INF],
            [INF, INF]
        ]
        expected = [
            [INF, INF],
            [INF, INF]
        ]
        walls_and_gates(rooms)
        self.assertEqual(rooms, expected)

    def test_all_gates(self):
        rooms = [
            [0, 0],
            [0, 0]
        ]
        expected = [
            [0, 0],
            [0, 0]
        ]
        walls_and_gates(rooms)
        self.assertEqual(rooms, expected)

    def test_empty_grid(self):
        rooms = []
        expected = []
        walls_and_gates(rooms)
        self.assertEqual(rooms, expected)

if __name__ == "__main__":
    unittest.main()