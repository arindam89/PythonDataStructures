"""
LeetCode 689: Maximum Sum of Three Non-Overlapping Subarrays
https://leetcode.com/problems/maximum-sum-of-three-non-overlapping-subarrays/

Given an integer array nums and an integer k, find three non-overlapping subarrays
of length k with maximum sum and return them.

Return the result as a list of indices representing the starting position of each interval
(0-indexed). If there are multiple answers, return the lexicographically smallest one.

Example:
Input: nums = [1,2,1,2,6,7,5,1], k = 2
Output: [0,3,5]
Explanation: Subarrays [1,2], [2,6], [7,5] correspond to starting indices [0,3,5].
We could have also taken [2,1], but that would be lexicographically larger.

Time Complexity: O(n) where n is length of nums
Space Complexity: O(n)
"""

from typing import List

def max_sum_of_three_subarrays(nums: List[int], k: int) -> List[int]:
    """
    Find three non-overlapping subarrays with maximum sum.
    Uses dynamic programming with forward and backward scanning.
    
    Args:
        nums: Array of integers
        k: Length of each subarray
        
    Returns:
        List of starting indices for the three subarrays
    """
    # Handle edge case
    if not nums or len(nums) < 3 * k:
        return []
        
    n = len(nums)
    
    # Calculate k-sized window sums
    window_sums = []
    curr_sum = sum(nums[:k])
    window_sums.append(curr_sum)
    
    for i in range(k, n):
        curr_sum = curr_sum + nums[i] - nums[i - k]
        window_sums.append(curr_sum)
        
    # Find best single window from left to right
    left = [0] * len(window_sums)  # left[i] is best index for window ending at i
    best_sum = window_sums[0]
    best_index = 0
    
    for i in range(1, len(window_sums) - 2 * k):
        if window_sums[i] > best_sum:
            best_sum = window_sums[i]
            best_index = i
        left[i] = best_index
        
    # Find best single window from right to left
    right = [0] * len(window_sums)  # right[i] is best index for window starting at i
    best_sum = window_sums[-1]
    best_index = len(window_sums) - 1
    
    for i in range(len(window_sums) - 2, k - 1, -1):
        if window_sums[i] >= best_sum:  # >= for lexicographically smallest
            best_sum = window_sums[i]
            best_index = i
        right[i] = best_index
        
    # Find best three windows
    max_total = 0
    result = [0, 0, 0]
    
    # Try each middle window position
    for i in range(k, n - 2 * k):
        left_index = left[i - k]
        right_index = right[i + k]
        total = window_sums[left_index] + window_sums[i] + window_sums[right_index]
        
        if total > max_total:
            max_total = total
            result = [left_index, i, right_index]
            
    return result