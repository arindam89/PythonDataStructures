"""
LeetCode Problem: Partition Equal Subset Sum
Link: https://leetcode.com/problems/partition-equal-subset-sum/

Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal.

Approach:
This is a dynamic programming problem. We use a 1D DP array where dp[j] represents whether a subset with sum j can be formed using the elements of the array.
1. Calculate the total sum of the array. If it is odd, return False (cannot partition into two equal subsets).
2. Target sum for each subset is total_sum // 2.
3. Iterate through the array and update the DP array from back to front to avoid overwriting.

Time Complexity: O(n * target)
Space Complexity: O(target)
"""

def can_partition(nums: list[int]) -> bool:
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    return dp[target]