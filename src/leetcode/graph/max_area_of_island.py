"""
Problem: Max Area of Island
Link: https://leetcode.com/problems/max-area-of-island/

Approach:
- Use Depth First Search (DFS) to traverse the grid.
- For each cell in the grid, if it is part of an island (value 1), calculate the area of the island by exploring all connected cells.
- Keep track of the maximum area encountered during the traversal.

Time Complexity: O(R * C), where R is the number of rows and C is the number of columns in the grid.
Space Complexity: O(R * C) in the worst case for the recursion stack.

Additional Notes:
- The grid is modified in-place to mark visited cells as 0, avoiding the need for an additional visited array.
- The algorithm ensures that each cell is visited only once, making it efficient for large grids.
"""

def max_area_of_island(grid):
    def dfs(r, c):
        """
        Perform DFS to calculate the area of the island starting from cell (r, c).

        Args:
            r: Row index of the current cell
            c: Column index of the current cell

        Returns:
            The area of the island connected to cell (r, c)
        """
        # Base case: if out of bounds or at a water cell, return 0
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
            return 0

        # Mark the cell as visited by setting it to 0
        grid[r][c] = 0

        # Explore all 4 directions and calculate the area
        area = 1
        area += dfs(r + 1, c)  # Down
        area += dfs(r - 1, c)  # Up
        area += dfs(r, c + 1)  # Right
        area += dfs(r, c - 1)  # Left

        return area

    max_area = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:  # Start a new DFS if the cell is part of an island
                max_area = max(max_area, dfs(r, c))

    return max_area