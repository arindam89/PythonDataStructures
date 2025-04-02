"""
LeetCode Problem: Single Number
Link: https://leetcode.com/problems/single-number/

Problem Statement:
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Approach:
1. Use the XOR operation to find the single number.
2. XOR of a number with itself is 0, and XOR of a number with 0 is the number itself.
3. Iterate through the array and XOR all elements. The result will be the single number.

Time Complexity: O(n), where n is the number of elements in nums.
Space Complexity: O(1).
"""

def single_number(nums):
    """Finds the single number in the array."""
    result = 0
    for num in nums:
        result ^= num
    return result