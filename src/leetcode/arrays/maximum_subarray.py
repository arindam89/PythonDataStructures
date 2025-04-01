"""
LeetCode 53: Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Implemented with both Kadane's algorithm (O(n)) and divide-and-conquer (O(n log n))
approaches for educational purposes.
"""

from typing import List, Tuple

def max_subarray_kadane(nums: List[int]) -> int:
    """
    Find maximum subarray sum using Kadane's algorithm.
    
    Args:
        nums: Array of integers
        
    Returns:
        Maximum sum of any contiguous subarray
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return 0
    
    max_sum = current_sum = nums[0]
    
    for num in nums[1:]:
        # Either extend previous subarray or start new one
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
        
    return max_sum

def max_subarray_divide_conquer(nums: List[int]) -> int:
    """
    Find maximum subarray sum using divide and conquer approach.
    
    Args:
        nums: Array of integers
        
    Returns:
        Maximum sum of any contiguous subarray
        
    Time Complexity: O(n log n)
    Space Complexity: O(log n) due to recursion stack
    """
    def find_max_crossing(nums: List[int], left: int, mid: int, right: int) -> int:
        """Find maximum sum crossing the middle element."""
        # Left half
        left_sum = float('-inf')
        curr_sum = 0
        for i in range(mid, left - 1, -1):
            curr_sum += nums[i]
            left_sum = max(left_sum, curr_sum)
            
        # Right half
        right_sum = float('-inf')
        curr_sum = 0
        for i in range(mid + 1, right + 1):
            curr_sum += nums[i]
            right_sum = max(right_sum, curr_sum)
            
        return left_sum + right_sum
    
    def max_subarray_recursive(nums: List[int], left: int, right: int) -> int:
        """Recursive helper for divide and conquer approach."""
        # Base case: single element
        if left == right:
            return nums[left]
            
        mid = (left + right) // 2
        
        # Find maximum in left and right halves
        left_max = max_subarray_recursive(nums, left, mid)
        right_max = max_subarray_recursive(nums, mid + 1, right)
        
        # Find maximum crossing the middle
        cross_max = find_max_crossing(nums, left, mid, right)
        
        # Return maximum of the three
        return max(left_max, right_max, cross_max)
    
    if not nums:
        return 0
        
    return max_subarray_recursive(nums, 0, len(nums) - 1)

def max_subarray_with_indices(nums: List[int]) -> Tuple[int, int, int]:
    """
    Find maximum subarray sum and return indices of the subarray.
    Uses Kadane's algorithm with index tracking.
    
    Args:
        nums: Array of integers
        
    Returns:
        Tuple of (maximum sum, start index, end index)
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return (0, -1, -1)
    
    max_sum = current_sum = nums[0]
    max_start = max_end = start = 0
    
    for i in range(1, len(nums)):
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            start = i
        else:
            current_sum += nums[i]
            
        if current_sum > max_sum:
            max_sum = current_sum
            max_start = start
            max_end = i
            
    return (max_sum, max_start, max_end)