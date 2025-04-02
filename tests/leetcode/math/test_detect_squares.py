"""
Test cases for Detect Squares problem.
"""
import unittest
from src.leetcode.math.detect_squares import DetectSquares

class TestDetectSquares(unittest.TestCase):
    def test_case_1(self):
        ds = DetectSquares()
        ds.add([3, 10])
        ds.add([11, 2])
        ds.add([3, 2])
        self.assertEqual(ds.count([11, 10]), 1)

    def test_case_2(self):
        ds = DetectSquares()
        ds.add([1, 1])
        ds.add([2, 2])
        ds.add([2, 0])
        ds.add([0, 2])
        self.assertEqual(ds.count([0, 0]), 1)

    def test_case_3(self):
        ds = DetectSquares()
        ds.add([0, 0])
        ds.add([1, 1])
        ds.add([0, 1])
        ds.add([1, 0])
        self.assertEqual(ds.count([0, 0]), 1)

if __name__ == "__main__":
    unittest.main()