"""
Test cases for the LeetCode problem: Find Median from Data Stream
Link: https://leetcode.com/problems/find-median-from-data-stream/

The test cases validate the following scenarios:
1. Adding numbers and retrieving the median after each addition.
2. Handling both even and odd numbers of elements.
3. Edge cases with a single element.
"""

import unittest
from src.leetcode.heaps.find_median_from_data_stream import MedianFinder

class TestFindMedianFromDataStream(unittest.TestCase):
    def test_case_1(self):
        median_finder = MedianFinder()
        median_finder.addNum(1)
        self.assertEqual(median_finder.findMedian(), 1.0)  # Single element
        median_finder.addNum(2)
        self.assertEqual(median_finder.findMedian(), 1.5)  # Average of 1 and 2
        median_finder.addNum(3)
        self.assertEqual(median_finder.findMedian(), 2.0)  # Median is 2

    def test_case_2(self):
        median_finder = MedianFinder()
        nums = [5, 15, 1, 3]
        medians = []
        for num in nums:
            median_finder.addNum(num)
            medians.append(median_finder.findMedian())
        self.assertEqual(medians, [5.0, 10.0, 5.0, 4.0])  # Medians after each addition

    def test_case_3(self):
        median_finder = MedianFinder()
        nums = [2, 4, 6, 8, 10, 12]
        medians = []
        for num in nums:
            median_finder.addNum(num)
            medians.append(median_finder.findMedian())
        self.assertEqual(medians, [2.0, 3.0, 4.0, 5.0, 6.0, 7.0])  # Medians after each addition

if __name__ == "__main__":
    unittest.main()