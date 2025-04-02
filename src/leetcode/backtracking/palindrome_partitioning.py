# LeetCode 131: Palindrome Partitioning
# https://leetcode.com/problems/palindrome-partitioning/
#
# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.
#
# Approach:
# - Use backtracking to explore all possible partitions.
# - At each step, check if the current substring is a palindrome.
# - If it is, include it in the current partition and recurse for the remaining string.
# - Backtrack by removing the last added substring.

def partition(s):
    def is_palindrome(sub):
        return sub == sub[::-1]

    def backtrack(start, path):
        if start == len(s):
            # Found a valid partition
            result.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            if is_palindrome(s[start:end]):
                # Include the palindrome substring in the partition
                path.append(s[start:end])
                # Recurse for the remaining string
                backtrack(end, path)
                # Backtrack by removing the last added substring
                path.pop()

    result = []
    backtrack(0, [])
    return result