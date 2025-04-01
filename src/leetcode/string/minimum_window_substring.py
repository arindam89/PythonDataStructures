"""
LeetCode 76: Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t of lengths m and n respectively, return the minimum 
window substring of s such that every character in t (including duplicates) 
is included in the window. If there is no such substring, return the empty string "".

Example:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Time Complexity: O(n) where n is length of string s
Space Complexity: O(k) where k is size of character set
"""

from collections import Counter, defaultdict

def min_window(s: str, t: str) -> str:
    """
    Find the minimum window substring containing all characters from t.
    Uses sliding window technique with two pointers.
    
    Args:
        s: Source string to search in
        t: Target string containing required characters
        
    Returns:
        Minimum window substring, or empty string if no solution exists
    """
    if not s or not t:
        return ""
        
    # Count required characters
    required = Counter(t)
    required_chars = len(required)
    
    # Track current window character counts
    window = defaultdict(int)
    formed = 0  # Count of characters with sufficient frequency
    
    # Track minimum window
    min_window_size = float('inf')
    min_window_start = 0
    
    left = right = 0
    
    while right < len(s):
        # Add right character to window
        char = s[right]
        window[char] += 1
        
        # Check if this character completes a required count
        if char in required and window[char] == required[char]:
            formed += 1
            
        # Try to minimize window by moving left pointer
        while formed == required_chars and left <= right:
            # Update minimum window if current is smaller
            if right - left + 1 < min_window_size:
                min_window_size = right - left + 1
                min_window_start = left
                
            # Remove left character from window
            char = s[left]
            window[char] -= 1
            
            # Check if removing this char breaks required count
            if char in required and window[char] < required[char]:
                formed -= 1
                
            left += 1
            
        right += 1
        
    return "" if min_window_size == float('inf') else s[min_window_start:min_window_start + min_window_size]