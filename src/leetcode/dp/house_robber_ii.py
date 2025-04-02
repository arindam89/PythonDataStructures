"""
LeetCode Problem: House Robber II
Link: https://leetcode.com/problems/house-robber-ii/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle. This means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Approach:
This is an extension of the House Robber problem. Since the houses are arranged in a circle, we cannot rob both the first and the last house.
We solve this by splitting the problem into two cases:
1. Rob houses from index 0 to n-2.
2. Rob houses from index 1 to n-1.
We then return the maximum of the two results.
"""

def rob(nums: list[int]) -> int:
    def rob_linear(houses: list[int]) -> int:
        prev, curr = 0, 0
        for num in houses:
            prev, curr = curr, max(curr, prev + num)
        return curr

    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))