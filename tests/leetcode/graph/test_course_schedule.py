"""
Test cases for the Course Schedule problem.

Additional Notes:
- The test cases cover various scenarios, including:
  1. A simple graph with no cycles.
  2. A graph with a cycle.
  3. A graph with multiple independent courses.
  4. A graph with all courses interdependent.
"""

import unittest
from src.leetcode.graph.course_schedule import can_finish

class TestCourseSchedule(unittest.TestCase):
    def test_simple_case(self):
        num_courses = 2
        prerequisites = [[1, 0]]
        self.assertTrue(can_finish(num_courses, prerequisites))

    def test_cycle_case(self):
        num_courses = 2
        prerequisites = [[1, 0], [0, 1]]
        self.assertFalse(can_finish(num_courses, prerequisites))

    def test_multiple_independent_courses(self):
        num_courses = 4
        prerequisites = [[1, 0], [2, 3]]
        self.assertTrue(can_finish(num_courses, prerequisites))

    def test_all_interdependent_courses(self):
        num_courses = 4
        prerequisites = [[1, 0], [2, 1], [3, 2], [0, 3]]
        self.assertFalse(can_finish(num_courses, prerequisites))

if __name__ == "__main__":
    unittest.main()