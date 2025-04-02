"""
Test cases for the LeetCode problem: Kth Largest Element in an Array
Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

The test cases validate the following scenarios:
1. A basic case with multiple elements and k smaller than the total number of elements.
2. k equals the total number of elements.
3. The array contains duplicate elements.
4. The array contains only one element.
"""

import unittest
from src.leetcode.heaps.kth_largest_element_in_array import find_kth_largest

class TestKthLargestElementInArray(unittest.TestCase):
    def test_case_1(self):
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        self.assertEqual(find_kth_largest(nums, k), 5)  # 2nd largest element is 5

    def test_case_2(self):
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        self.assertEqual(find_kth_largest(nums, k), 4)  # 4th largest element is 4

    def test_case_3(self):
        nums = [1, 1, 1, 1, 1]
        k = 1
        self.assertEqual(find_kth_largest(nums, k), 1)  # Only one unique element

    def test_case_4(self):
        nums = [10]
        k = 1
        self.assertEqual(find_kth_largest(nums, k), 10)  # Single element array

if __name__ == "__main__":
    unittest.main()