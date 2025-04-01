"""
LeetCode 300: Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/

Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no elements
without changing the order of the remaining elements.

Example:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Time Complexity: O(n log n) using binary search approach
Space Complexity: O(n)
"""

from typing import List
import bisect

def length_of_lis(nums: List[int]) -> int:
    """
    Find the length of longest increasing subsequence using binary search approach.
    Maintains a sorted array of potential values that could form an increasing subsequence.
    
    Args:
        nums: List of integers
        
    Returns:
        Length of longest increasing subsequence
    """
    if not nums:
        return 0
        
    # tails[i] represents the smallest value that can end an increasing 
    # subsequence of length i+1
    tails = []
    
    for num in nums:
        # Find the position where num should be inserted
        pos = bisect.bisect_left(tails, num)
        
        # If num is larger than all values in tails, append it
        if pos == len(tails):
            tails.append(num)
        # Otherwise, replace the first value >= num
        else:
            tails[pos] = num
            
    return len(tails)

def length_of_lis_dp(nums: List[int]) -> int:
    """
    Alternative implementation using dynamic programming approach.
    Slower but easier to understand and modify if needed.
    Time Complexity: O(n^2)
    
    Args:
        nums: List of integers
        
    Returns:
        Length of longest increasing subsequence
    """
    if not nums:
        return 0
        
    n = len(nums)
    # dp[i] represents the length of LIS ending at index i
    dp = [1] * n
    
    # For each position, look back at previous positions
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    return max(dp)