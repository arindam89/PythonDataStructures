"""
LeetCode Problem: Word Break
Link: https://leetcode.com/problems/word-break/

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Approach:
We use dynamic programming to solve this problem. Let dp[i] represent whether the substring s[:i] can be segmented into words from the dictionary.
1. Initialize dp[0] = True (empty string can always be segmented).
2. For each index i, check all substrings s[j:i] where j < i. If dp[j] is True and s[j:i] is in wordDict, set dp[i] = True.
3. Return dp[len(s)].

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

def word_break(s: str, wordDict: list[str]) -> bool:
    word_set = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]