"""
LeetCode Problem: Longest Palindromic Substring
Link: https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

Approach:
We use a dynamic programming approach to solve this problem. We define a 2D DP table where dp[i][j] is True if the substring s[i:j+1] is a palindrome.
1. Base case: Single characters are palindromes.
2. Base case: Two consecutive identical characters are palindromes.
3. For substrings longer than 2, check if the first and last characters are the same and the substring between them is a palindrome.

Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""

def longest_palindrome(s: str) -> str:
    n = len(s)
    if n <= 1:
        return s

    dp = [[False] * n for _ in range(n)]
    start, max_length = 0, 1

    for i in range(n):
        dp[i][i] = True

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start, max_length = i, 2

    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start, max_length = i, length

    return s[start:start + max_length]