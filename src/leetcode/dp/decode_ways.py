"""
LeetCode Problem: Decode Ways
Link: https://leetcode.com/problems/decode-ways/

A message containing letters from A-Z can be encoded into numbers using the mapping 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26.
To decode an encoded message, determine the total number of ways it can be decoded.

Approach:
We use dynamic programming to solve this problem. Let dp[i] represent the number of ways to decode the substring s[:i].
1. If s[i-1] is a valid single digit (1-9), then dp[i] += dp[i-1].
2. If s[i-2:i] is a valid two-digit number (10-26), then dp[i] += dp[i-2].

Time Complexity: O(n)
Space Complexity: O(n)
"""

def num_decodings(s: str) -> int:
    if not s or s[0] == '0':
        return 0

    n = len(s)
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1

    for i in range(2, n + 1):
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]
        if 10 <= int(s[i - 2:i]) <= 26:
            dp[i] += dp[i - 2]

    return dp[n]