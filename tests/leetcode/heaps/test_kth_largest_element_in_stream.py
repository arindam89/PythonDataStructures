"""
Test cases for the LeetCode problem: Kth Largest Element in a Stream
Link: https://leetcode.com/problems/kth-largest-element-in-a-stream/

The test cases validate the following scenarios:
1. Adding elements to an initially empty stream.
2. Adding elements to a stream with pre-existing elements.
3. Ensuring the kth largest element is correctly updated after each addition.
"""

import unittest
from src.leetcode.heaps.kth_largest_element_in_stream import KthLargest

class TestKthLargestElementInStream(unittest.TestCase):
    def test_case_1(self):
        kth_largest = KthLargest(3, [4, 5, 8, 2])
        self.assertEqual(kth_largest.add(3), 4)  # After adding 3, the 3rd largest is 4
        self.assertEqual(kth_largest.add(5), 5)  # After adding 5, the 3rd largest is 5
        self.assertEqual(kth_largest.add(10), 5) # After adding 10, the 3rd largest is 5
        self.assertEqual(kth_largest.add(9), 8)  # After adding 9, the 3rd largest is 8
        self.assertEqual(kth_largest.add(4), 8)  # After adding 4, the 3rd largest is 8

    def test_case_2(self):
        kth_largest = KthLargest(1, [])
        self.assertEqual(kth_largest.add(-1), -1) # Adding to an empty stream
        self.assertEqual(kth_largest.add(1), 1)   # Adding a larger element
        self.assertEqual(kth_largest.add(-2), 1)  # Adding a smaller element
        self.assertEqual(kth_largest.add(-4), 1)  # Adding an even smaller element
        self.assertEqual(kth_largest.add(3), 3)   # Adding the largest element so far

if __name__ == "__main__":
    unittest.main()