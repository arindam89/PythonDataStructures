import unittest
from src.leetcode.intervals.minimum_interval_to_include_each_query import min_interval

class TestMinimumIntervalToIncludeEachQuery(unittest.TestCase):
    def test_min_interval(self):
        self.assertEqual(min_interval([[1, 4], [2, 4], [3, 6]], [2, 3, 4]), [3, 3, 3])
        self.assertEqual(min_interval([[1, 4], [2, 4], [3, 6]], [1, 5]), [4, -1])
        self.assertEqual(min_interval([[1, 2], [2, 3], [3, 4]], [2, 3]), [2, 2])
        self.assertEqual(min_interval([], [1, 2, 3]), [-1, -1, -1])
        self.assertEqual(min_interval([[1, 10], [2, 9], [3, 8]], [5, 6, 7]), [8, 8, 8])

if __name__ == "__main__":
    unittest.main()