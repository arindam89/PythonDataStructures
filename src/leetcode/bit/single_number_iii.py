"""
LeetCode 260: Single Number III
https://leetcode.com/problems/single-number-iii/

Given an integer array nums, in which exactly two elements appear only once and all
other elements appear exactly twice, find the two elements that appear only once.
You can return the answer in any order.

Example:
Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation: 3 and 5 appear only once while 1 and 2 appear twice.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

def single_number_iii(nums: List[int]) -> List[int]:
    """
    Find two numbers that appear only once in array where all others appear twice.
    Uses XOR to separate numbers into two groups based on a differing bit.
    
    Args:
        nums: Array of integers where two numbers appear once, others twice
        
    Returns:
        List containing the two numbers that appear only once
    """
    # Get XOR of all numbers
    # Result will be XOR of two unique numbers (all others cancel out)
    xor_all = 0
    for num in nums:
        xor_all ^= num
        
    # Find rightmost set bit in xor_all
    # This bit differs in the two numbers we're looking for
    rightmost_set = xor_all & -xor_all
    
    # Use this bit to separate numbers into two groups
    x = 0  # Will hold one of the unique numbers
    
    for num in nums:
        # One group has this bit set, other doesn't
        if num & rightmost_set:
            x ^= num
            
    # Other unique number is XOR of x with xor_all
    return [x, xor_all ^ x]

def single_number_iii_hash(nums: List[int]) -> List[int]:
    """
    Alternative implementation using hash set.
    Time: O(n), Space: O(n)
    
    Args:
        nums: Array of integers where two numbers appear once, others twice
        
    Returns:
        List containing the two numbers that appear only once
    """
    # Track numbers we've seen
    seen = set()
    
    for num in nums:
        if num in seen:
            seen.remove(num)  # Remove when seen second time
        else:
            seen.add(num)    # Add when seen first time
            
    # seen now contains only the two unique numbers
    return list(seen)