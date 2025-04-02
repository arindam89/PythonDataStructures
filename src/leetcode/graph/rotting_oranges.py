"""
Problem: Rotting Oranges
Link: https://leetcode.com/problems/rotting-oranges/

Approach:
- Use Breadth First Search (BFS) to simulate the rotting process.
- Start with all initially rotten oranges and process them level by level.
- For each rotten orange, rot its adjacent fresh oranges and add them to the queue.
- Keep track of the time taken to rot all oranges.
- If there are still fresh oranges left after the BFS, return -1.

Time Complexity: O(M * N), where M is the number of rows and N is the number of columns in the grid.
Space Complexity: O(M * N) for the BFS queue.

Additional Notes:
- The grid is modified in-place to mark fresh oranges as rotten.
- The algorithm ensures that each cell is processed only once, making it efficient for large grids.
- The result is the minimum time required to rot all oranges or -1 if not all oranges can be rotted.
"""

from collections import deque

def oranges_rotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_count = 0

    # Initialize the queue with all rotten oranges and count fresh oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh_count += 1

    # Directions for adjacent cells
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    minutes = 0

    # Perform BFS
    while queue and fresh_count > 0:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_count -= 1
                    queue.append((nr, nc))
        minutes += 1

    return minutes if fresh_count == 0 else -1