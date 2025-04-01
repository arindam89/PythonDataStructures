"""
LeetCode 11: Container With Most Water
https://leetcode.com/problems/container-with-most-water/

Given n non-negative integers a1, a2, ..., an, where each represents a point
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
of the line i is at (i, ai) and (i, 0). Find two lines, which, together with
the x-axis forms a container, such that the container contains the most water.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

def max_area(height: List[int]) -> int:
    """
    Find the maximum area that can be formed between any two lines.
    Uses two-pointer technique to solve efficiently.
    
    Args:
        height: List of integers representing heights of lines
        
    Returns:
        Maximum area that can be contained
    """
    max_water = 0
    left = 0
    right = len(height) - 1
    
    while left < right:
        # Calculate width between lines
        width = right - left
        
        # Height is limited by the shorter line
        h = min(height[left], height[right])
        
        # Update maximum area if current area is larger
        max_water = max(max_water, width * h)
        
        # Move the pointer pointing to shorter line inward
        # (as moving the taller line's pointer can only decrease area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return max_water