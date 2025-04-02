"""
LeetCode Problem: Detect Squares
Link: https://leetcode.com/problems/detect-squares/

Problem Statement:
You are given a stream of points on the X-Y plane. Design an algorithm that:
1. Adds new points from the stream.
2. Counts the number of squares that can be formed with a given point.

Approach:
1. Use a dictionary to store the frequency of each point.
2. For counting squares, iterate through points that share the same x or y coordinate with the given point.
3. Check if the other two points of the square exist and calculate the count.

Time Complexity:
- add: O(1)
- count: O(n), where n is the number of unique points.

Space Complexity: O(n), where n is the number of unique points.
"""

from collections import defaultdict

class DetectSquares:
    def __init__(self):
        self.points_count = defaultdict(int)

    def add(self, point):
        """Adds a point to the data structure."""
        self.points_count[tuple(point)] += 1

    def count(self, point):
        """Counts the number of squares that can be formed with the given point."""
        px, py = point
        count = 0

        for (x, y), freq in self.points_count.items():
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue

            count += freq * self.points_count.get((px, y), 0) * self.points_count.get((x, py), 0)

        return count