import unittest
from src.leetcode.arrays.maximum_subarray import (
    max_subarray_kadane,
    max_subarray_divide_conquer,
    max_subarray_with_indices
)

class TestMaximumSubarray(unittest.TestCase):
    def test_kadane_algorithm(self):
        test_cases = [
            ([-2,1,-3,4,-1,2,1,-5,4], 6),
            ([1], 1),
            ([5,4,-1,7,8], 23),
            ([-1], -1),
            ([-2,-1], -1),
            ([1,-1,1], 1),
            ([], 0)
        ]
        
        for nums, expected in test_cases:
            with self.subTest(nums=nums):
                self.assertEqual(max_subarray_kadane(nums), expected)
                
    def test_divide_and_conquer(self):
        test_cases = [
            ([-2,1,-3,4,-1,2,1,-5,4], 6),
            ([1], 1),
            ([5,4,-1,7,8], 23),
            ([-1], -1),
            ([-2,-1], -1),
            ([1,-1,1], 1),
            ([], 0)
        ]
        
        for nums, expected in test_cases:
            with self.subTest(nums=nums):
                self.assertEqual(max_subarray_divide_conquer(nums), expected)
                
    def test_with_indices(self):
        test_cases = [
            ([-2,1,-3,4,-1,2,1,-5,4], (6, 3, 6)),
            ([1], (1, 0, 0)),
            ([5,4,-1,7,8], (23, 0, 4)),
            ([-1], (-1, 0, 0)),
            ([-2,-1], (-1, 1, 1)),
            ([1,-1,1], (1, 2, 2)),
            ([], (0, -1, -1))
        ]
        
        for nums, expected in test_cases:
            with self.subTest(nums=nums):
                self.assertEqual(max_subarray_with_indices(nums), expected)
                
    def test_equal_results(self):
        """Test that both implementations return the same results"""
        test_cases = [
            [-2,1,-3,4,-1,2,1,-5,4],
            [1],
            [5,4,-1,7,8],
            [-1],
            [-2,-1],
            [1,-1,1]
        ]
        
        for nums in test_cases:
            with self.subTest(nums=nums):
                kadane_result = max_subarray_kadane(nums)
                divide_conquer_result = max_subarray_divide_conquer(nums)
                with_indices_result = max_subarray_with_indices(nums)[0]
                
                self.assertEqual(kadane_result, divide_conquer_result)
                self.assertEqual(kadane_result, with_indices_result)

if __name__ == '__main__':
    unittest.main()