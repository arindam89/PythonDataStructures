import unittest
from src.leetcode.intervals.insert_interval import insert

class TestInsertInterval(unittest.TestCase):
    def test_insert(self):
        self.assertEqual(insert([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]])
        self.assertEqual(insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]), [[1, 2], [3, 10], [12, 16]])
        self.assertEqual(insert([], [5, 7]), [[5, 7]])
        self.assertEqual(insert([[1, 5]], [2, 3]), [[1, 5]])
        self.assertEqual(insert([[1, 5]], [2, 7]), [[1, 7]])

if __name__ == "__main__":
    unittest.main()