"""
LeetCode 200: Number of Islands
Link: https://leetcode.com/problems/number-of-islands/

Approach:
- Use Depth First Search (DFS) to traverse the grid.
- For each cell in the grid, if it is part of an island ('1'), perform a DFS to mark all connected land cells as visited.
- Increment the island count for each DFS traversal.

Time Complexity: O(M * N), where M is the number of rows and N is the number of columns in the grid.
Space Complexity: O(M * N) in the worst case for the recursion stack.

Additional Notes:
- The grid is modified in-place to mark visited cells as '0', avoiding the need for an additional visited array.
- The algorithm ensures that each cell is visited only once, making it efficient for large grids.
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

        Args:
            row: Row index of the current cell
            col: Column index of the current cell
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
            if grid[i][j] == '1':  # Start a new DFS if the cell is part of an island
                islands += 1
                dfs(i, j)  # Mark this island as visited

    return islands