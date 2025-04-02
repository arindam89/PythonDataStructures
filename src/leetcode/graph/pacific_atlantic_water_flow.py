"""
Problem: Pacific Atlantic Water Flow
Link: https://leetcode.com/problems/pacific-atlantic-water-flow/

Approach:
- Use Depth First Search (DFS) or Breadth First Search (BFS) to determine which cells can flow to both the Pacific and Atlantic oceans.
- Start from the edges of the grid (Pacific and Atlantic borders) and mark reachable cells for each ocean.
- The intersection of cells reachable from both oceans gives the result.

Time Complexity: O(M * N), where M is the number of rows and N is the number of columns in the grid.
Space Complexity: O(M * N) for the visited sets.

Additional Notes:
- The algorithm ensures that each cell is visited only once for each ocean, making it efficient for large grids.
- The result is returned as a list of tuples representing the coordinates of the cells that can flow to both oceans.
"""

def pacific_atlantic(heights):
    if not heights or not heights[0]:
        return []

    rows, cols = len(heights), len(heights[0])
    pacific_reachable = set()
    atlantic_reachable = set()

    def dfs(r, c, reachable, prev_height):
        """
        Perform DFS to mark all cells reachable from the current cell.

        Args:
            r: Row index of the current cell
            c: Column index of the current cell
            reachable: Set to store reachable cells
            prev_height: Height of the previous cell to ensure water can flow
        """
        if (
            (r, c) in reachable or
            r < 0 or r >= rows or c < 0 or c >= cols or
            heights[r][c] < prev_height
        ):
            return

        reachable.add((r, c))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in directions:
            dfs(r + dr, c + dc, reachable, heights[r][c])

    # Perform DFS from Pacific and Atlantic borders
    for c in range(cols):
        dfs(0, c, pacific_reachable, heights[0][c])  # Top row (Pacific)
        dfs(rows - 1, c, atlantic_reachable, heights[rows - 1][c])  # Bottom row (Atlantic)

    for r in range(rows):
        dfs(r, 0, pacific_reachable, heights[r][0])  # Left column (Pacific)
        dfs(r, cols - 1, atlantic_reachable, heights[r][cols - 1])  # Right column (Atlantic)

    # Return the intersection of cells reachable from both oceans
    return list(pacific_reachable & atlantic_reachable)