"""
LeetCode Problem: House Robber
Link: https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
All houses at this place are arranged in a straight line. You cannot rob two adjacent houses.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Approach:
This is a dynamic programming problem. For each house `i`, you can either:
1. Rob the house `i` and add its value to the maximum amount robbed from houses up to `i-2`.
2. Skip the house `i` and take the maximum amount robbed from houses up to `i-1`.
We can solve this iteratively with O(n) time complexity and O(1) space complexity.
"""

def rob(nums: list[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev, curr = 0, 0
    for num in nums:
        prev, curr = curr, max(curr, prev + num)

    return curr