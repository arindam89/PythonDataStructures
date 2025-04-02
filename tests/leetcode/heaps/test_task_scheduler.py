"""
Test cases for the LeetCode problem: Task Scheduler
Link: https://leetcode.com/problems/task-scheduler/

The test cases validate the following scenarios:
1. Tasks with no cooldown period.
2. Tasks with a cooldown period that requires idle time.
3. All tasks are the same.
4. Tasks with a cooldown period but no idle time required.
"""

import unittest
from src.leetcode.heaps.task_scheduler import least_interval

class TestTaskScheduler(unittest.TestCase):
    def test_case_1(self):
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 2
        self.assertEqual(least_interval(tasks, n), 8)  # Example from problem statement

    def test_case_2(self):
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 0
        self.assertEqual(least_interval(tasks, n), 6)  # No cooldown period

    def test_case_3(self):
        tasks = ["A", "A", "A", "A"]
        n = 3
        self.assertEqual(least_interval(tasks, n), 10)  # All tasks are the same

    def test_case_4(self):
        tasks = ["A", "B", "C", "D"]
        n = 2
        self.assertEqual(least_interval(tasks, n), 4)  # No idle time required

if __name__ == "__main__":
    unittest.main()