"""
LeetCode 77: Combinations
https://leetcode.com/problems/combinations/

Given two integers n and k, return all possible combinations of k numbers
chosen from the range [1, n]. You may return the answer in any order.

Example:
Input: n = 4, k = 2
Output: [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]

Time Complexity: O(n! / (k! * (n-k)!))
Space Complexity: O(k) for recursion stack
"""

from typing import List

def combine(n: int, k: int) -> List[List[int]]:
    """
    Generate all possible combinations of k numbers from range [1, n].
    Uses backtracking approach to build combinations.
    
    Args:
        n: Upper bound of the range (inclusive)
        k: Number of elements in each combination
        
    Returns:
        List of all possible combinations
    """
    def backtrack(start: int, curr: List[int]) -> None:
        # If we have k numbers, we found a valid combination
        if len(curr) == k:
            result.append(curr[:])
            return
            
        # Try adding each number from start to n
        for i in range(start, n + 1):
            # Add current number
            curr.append(i)
            # Recursively generate combinations starting from next number
            backtrack(i + 1, curr)
            # Backtrack by removing the current number
            curr.pop()
            
    result = []
    backtrack(1, [])
    return result