"""
LeetCode 200: Number of Islands
https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water),
return the number of islands. An island is surrounded by water and is formed by
connecting adjacent lands horizontally or vertically.

Example:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Time Complexity: O(m * n) where m and n are the dimensions of the grid
Space Complexity: O(m * n) in worst case for recursion stack
"""

from typing import List

def num_islands(grid: List[List[str]]) -> int:
    """
    Count the number of islands in the grid using DFS.
    
    Args:
        grid: 2D grid of '1's and '0's
        
    Returns:
        Number of islands
    """
    if not grid:
        return 0
        
    rows = len(grid)
    cols = len(grid[0])
    islands = 0
    
    def dfs(row: int, col: int) -> None:
        """
        Perform DFS to mark all connected land cells as visited.
        Modifies the grid in-place to mark visited cells.
        """
        # Check bounds and if current cell is land
        if (row < 0 or row >= rows or 
            col < 0 or col >= cols or 
            grid[row][col] != '1'):
            return
            
        # Mark as visited by changing to '0'
        grid[row][col] = '0'
        
        # Check all adjacent cells
        dfs(row + 1, col)  # Down
        dfs(row - 1, col)  # Up
        dfs(row, col + 1)  # Right
        dfs(row, col - 1)  # Left
    
    # Scan the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                islands += 1
                dfs(i, j)  # Mark this island as visited
                
    return islands