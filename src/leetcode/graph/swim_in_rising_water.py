"""
Problem: Swim in Rising Water
Link: https://leetcode.com/problems/swim-in-rising-water/

Approach:
- Use a modified version of Dijkstra's algorithm to find the minimum time required to reach the bottom-right corner.
- Represent the grid as a graph where each cell is a node, and the weight of an edge is the maximum elevation encountered so far.
- Use a priority queue to process cells in order of their elevation.
- Stop when the bottom-right corner is reached.

Time Complexity: O(N^2 * log(N)), where N is the number of rows/columns in the grid.
Space Complexity: O(N^2) for the priority queue and visited set.
"""

import heapq

def swim_in_water(grid):
    """
    Calculate the minimum time required to swim from the top-left to the bottom-right corner.

    Args:
        grid: 2D grid of elevations.

    Returns:
        The minimum time required to reach the bottom-right corner.
    """
    n = len(grid)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    min_heap = [(grid[0][0], 0, 0)]  # (time, row, col)
    visited = set()
    visited.add((0, 0))

    while min_heap:
        time, r, c = heapq.heappop(min_heap)

        # If we reach the bottom-right corner, return the time
        if r == n - 1 and c == n - 1:
            return time

        # Explore neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                visited.add((nr, nc))
                heapq.heappush(min_heap, (max(time, grid[nr][nc]), nr, nc))