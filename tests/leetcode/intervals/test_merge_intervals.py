import unittest
from src.leetcode.intervals.merge_intervals import merge

class TestMergeIntervals(unittest.TestCase):
    def test_merge(self):
        self.assertEqual(merge([[1, 3], [2, 6], [8, 10], [15, 18]]), [[1, 6], [8, 10], [15, 18]])
        self.assertEqual(merge([[1, 4], [4, 5]]), [[1, 5]])
        self.assertEqual(merge([[1, 4], [2, 3]]), [[1, 4]])
        self.assertEqual(merge([[1, 4], [0, 0]]), [[0, 0], [1, 4]])
        self.assertEqual(merge([]), [])

if __name__ == "__main__":
    unittest.main()