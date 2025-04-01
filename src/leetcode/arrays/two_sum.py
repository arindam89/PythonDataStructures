"""
LeetCode 1: Two Sum
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the
two numbers in nums such that they add up to target. You may assume that each
input would have exactly one solution, and you may not use the same element twice.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Find two numbers in the array that sum to target.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List containing indices of the two numbers
    """
    seen = {}  # val -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
        
    return []  # No solution found