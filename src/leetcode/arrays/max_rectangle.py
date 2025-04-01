"""
LeetCode 85: Maximal Rectangle
https://leetcode.com/problems/maximal-rectangle/

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle
containing only 1's and return its area.

Example:
Input: matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
Explanation: The maximal rectangle is 2x3, formed by the 1's in rows 1 and 2, columns 2-4.

Time Complexity: O(rows * cols)
Space Complexity: O(cols)
"""

from typing import List

def maximal_rectangle(matrix: List[List[str]]) -> int:
    """
    Find the largest rectangle containing only 1's in the matrix.
    Uses the largest rectangle in histogram approach for each row.
    
    Args:
        matrix: Binary matrix of '0's and '1's
        
    Returns:
        Area of largest rectangle of 1's
    """
    if not matrix or not matrix[0]:
        return 0
        
    def largest_rectangle_histogram(heights: List[int]) -> int:
        """
        Helper function to find largest rectangle in a histogram.
        Uses a stack to track increasing heights.
        """
        stack = []  # Stack of indices
        max_area = 0
        i = 0
        
        while i < len(heights):
            # If stack is empty or current height is larger
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                # Calculate area with height at top of stack
                curr_height = heights[stack.pop()]
                width = i - stack[-1] - 1 if stack else i
                max_area = max(max_area, curr_height * width)
                
        # Process remaining heights in stack
        while stack:
            curr_height = heights[stack.pop()]
            width = i - stack[-1] - 1 if stack else i
            max_area = max(max_area, curr_height * width)
            
        return max_area
        
    rows = len(matrix)
    cols = len(matrix[0])
    heights = [0] * cols  # Current histogram heights
    max_area = 0
    
    # Process each row
    for row in range(rows):
        # Update heights
        for col in range(cols):
            if matrix[row][col] == '1':
                heights[col] += 1
            else:
                heights[col] = 0
                
        # Find largest rectangle in current histogram
        max_area = max(max_area, largest_rectangle_histogram(heights))
        
    return max_area