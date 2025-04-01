"""
LeetCode 477: Total Hamming Distance
https://leetcode.com/problems/total-hamming-distance/

Given an integer array nums, return the sum of Hamming distances between all 
pairs of numbers in the array. The Hamming distance between two integers is 
the number of positions at which their binary representations differ.

Example:
Input: nums = [4,14,2]
Output: 6
Explanation: 
4  (0100)
14 (1110)
2  (0010)
The Hamming distances are:
4 ↔ 14 = 2
4 ↔ 2 = 2
14 ↔ 2 = 2
Total = 6

Time Complexity: O(n * 32) = O(n) where n is length of array
Space Complexity: O(1)
"""

from typing import List

def total_hamming_distance(nums: List[int]) -> int:
    """
    Calculate sum of Hamming distances between all pairs of numbers.
    Uses bit manipulation to count differences at each bit position.
    
    Args:
        nums: Array of integers
        
    Returns:
        Sum of Hamming distances between all pairs
    """
    if not nums:
        return 0
        
    total = 0
    n = len(nums)
    
    # Check each of the 32 bits
    for i in range(32):
        ones = sum(1 for num in nums if num & (1 << i))
        # For each bit position, contribution to total is:
        # (numbers with 1) * (numbers with 0)
        total += ones * (n - ones)
        
    return total

def total_hamming_distance_brute(nums: List[int]) -> int:
    """
    Alternative brute force implementation.
    Time: O(n^2), Space: O(1)
    Used for testing and verification.
    
    Args:
        nums: Array of integers
        
    Returns:
        Sum of Hamming distances between all pairs
    """
    def hamming_distance(x: int, y: int) -> int:
        """Calculate Hamming distance between two numbers."""
        return bin(x ^ y).count('1')
    
    total = 0
    n = len(nums)
    
    # Check each pair of numbers
    for i in range(n):
        for j in range(i + 1, n):
            total += hamming_distance(nums[i], nums[j])
            
    return total