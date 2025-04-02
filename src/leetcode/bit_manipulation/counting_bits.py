"""
LeetCode Problem: Counting Bits
Link: https://leetcode.com/problems/counting-bits/

Problem Statement:
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Approach:
1. Use dynamic programming to calculate the number of 1's.
2. The number of 1's in i is equal to the number of 1's in i // 2 (right shift by 1) plus i % 2 (last bit).

Time Complexity: O(n), where n is the input number.
Space Complexity: O(n), for the output array.
"""

def count_bits(n):
    """Returns an array where each element is the number of 1's in the binary representation of its index."""
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp