"""
LeetCode 5: Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.
A palindrome is a string that reads the same forward and backward.

Example:
Input: s = "babad"
Output: "bab" (Note: "aba" is also a valid answer)

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def longest_palindrome(s: str) -> str:
    """
    Find the longest palindromic substring using expand-around-center approach.
    For each position, try to expand around it treating it as center of palindrome.
    
    Args:
        s: Input string
        
    Returns:
        Longest palindromic substring
    """
    if not s:
        return ""
        
    start = 0  # Start index of longest palindrome
    max_len = 1  # Length of longest palindrome
    
    def expand_around_center(left: int, right: int) -> int:
        """
        Expand around center (left, right) and return length of palindrome.
        Works for both odd and even length palindromes.
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
        
    for i in range(len(s)):
        # Try odd length palindromes (single char center)
        len1 = expand_around_center(i, i)
        
        # Try even length palindromes (two char center)
        len2 = expand_around_center(i, i + 1)
        
        # Update longest palindrome if necessary
        curr_len = max(len1, len2)
        if curr_len > max_len:
            max_len = curr_len
            # Calculate start index based on length
            start = i - (curr_len - 1) // 2
            
    return s[start:start + max_len]

def longest_palindrome_dp(s: str) -> str:
    """
    Alternative implementation using dynamic programming.
    Slower but can be more intuitive for some.
    Time Complexity: O(n^2)
    Space Complexity: O(n^2)
    
    Args:
        s: Input string
        
    Returns:
        Longest palindromic substring
    """
    if not s:
        return ""
        
    n = len(s)
    # dp[i][j] represents whether s[i:j+1] is palindrome
    dp = [[False] * n for _ in range(n)]
    
    # All single characters are palindromes
    for i in range(n):
        dp[i][i] = True
        
    start = 0  # Start index of longest palindrome
    max_len = 1  # Length of longest palindrome
    
    # Check for palindromes of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2
            
    # Check for palindromes of length > 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_len:
                    start = i
                    max_len = length
                    
    return s[start:start + max_len]