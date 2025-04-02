"""
Test cases for the LeetCode problem: K Closest Points to Origin
Link: https://leetcode.com/problems/k-closest-points-to-origin/

The test cases validate the following scenarios:
1. A basic case with multiple points and k smaller than the total number of points.
2. All points are equidistant from the origin.
3. k equals the total number of points.
4. Only one point is provided.
"""

import unittest
from src.leetcode.heaps.k_closest_points_to_origin import k_closest

class TestKClosestPointsToOrigin(unittest.TestCase):
    def test_case_1(self):
        points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
        k = 2
        result = k_closest(points, k)
        self.assertCountEqual(result, [[-2, 2], [0, 1]])  # Closest points

    def test_case_2(self):
        points = [[1, 1], [-1, -1], [1, -1], [-1, 1]]
        k = 2
        result = k_closest(points, k)
        self.assertCountEqual(result, [[1, 1], [-1, -1]])  # Any two points

    def test_case_3(self):
        points = [[3, 3], [5, -1], [-2, 4]]
        k = 3
        result = k_closest(points, k)
        self.assertCountEqual(result, [[3, 3], [5, -1], [-2, 4]])  # All points

    def test_case_4(self):
        points = [[2, 2]]
        k = 1
        result = k_closest(points, k)
        self.assertEqual(result, [[2, 2]])  # Single point

if __name__ == "__main__":
    unittest.main()