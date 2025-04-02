import unittest
from src.leetcode.intervals.non_overlapping_intervals import erase_overlap_intervals

class TestNonOverlappingIntervals(unittest.TestCase):
    def test_erase_overlap_intervals(self):
        self.assertEqual(erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]), 1)
        self.assertEqual(erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]), 2)
        self.assertEqual(erase_overlap_intervals([[1, 2], [2, 3]]), 0)
        self.assertEqual(erase_overlap_intervals([]), 0)
        self.assertEqual(erase_overlap_intervals([[1, 10], [2, 3], [4, 5], [6, 7]]), 0)

if __name__ == "__main__":
    unittest.main()