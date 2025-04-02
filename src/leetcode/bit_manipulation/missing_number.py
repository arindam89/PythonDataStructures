"""
LeetCode Problem: Missing Number
Link: https://leetcode.com/problems/missing-number/

Problem Statement:
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Approach:
1. Use XOR to find the missing number.
2. XOR all numbers from 0 to n and XOR all elements in the array.
3. The result will be the missing number since all other numbers cancel out.

Time Complexity: O(n), where n is the length of nums.
Space Complexity: O(1).
"""

def missing_number(nums):
    """Finds the missing number in the array."""
    n = len(nums)
    result = n
    for i in range(n):
        result ^= i ^ nums[i]
    return result