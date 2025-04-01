"""
LeetCode 46: Permutations
https://leetcode.com/problems/permutations/

Given an array nums of distinct integers, return all possible permutations.
You can return the answer in any order.

Example:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Time Complexity: O(n!)
Space Complexity: O(n) for recursion stack
"""

from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    """
    Generate all possible permutations of the given numbers.
    Uses backtracking approach to build permutations.
    
    Args:
        nums: List of distinct integers
        
    Returns:
        List of all possible permutations
    """
    def backtrack(curr: List[int], used: set) -> None:
        # If current permutation is complete
        if len(curr) == len(nums):
            result.append(curr[:])
            return
            
        # Try each number that hasn't been used yet
        for num in nums:
            if num not in used:
                # Add current number to permutation
                curr.append(num)
                used.add(num)
                
                # Recursively generate permutations
                backtrack(curr, used)
                
                # Backtrack by removing the current number
                curr.pop()
                used.remove(num)
                
    result = []
    backtrack([], set())
    return result