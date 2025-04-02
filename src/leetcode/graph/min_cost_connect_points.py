"""
Problem: Min Cost to Connect All Points
Link: https://leetcode.com/problems/min-cost-to-connect-all-points/

Approach:
- Use Prim's algorithm to find the Minimum Spanning Tree (MST).
- Start from an arbitrary point and use a priority queue to select the next point with the minimum cost.
- Keep track of visited points to avoid cycles.
- Continue until all points are connected.

Time Complexity: O(N^2 * log(N)), where N is the number of points.
Space Complexity: O(N^2) for the graph representation and priority queue.
"""

import heapq

def min_cost_connect_points(points):
    """
    Calculate the minimum cost to connect all points.

    Args:
        points: List of [x, y] coordinates of points.

    Returns:
        The minimum cost to connect all points.
    """
    n = len(points)
    graph = {i: [] for i in range(n)}

    # Build the graph with Manhattan distances
    for i in range(n):
        for j in range(i + 1, n):
            dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            graph[i].append((dist, j))
            graph[j].append((dist, i))

    # Prim's algorithm
    min_heap = [(0, 0)]  # (cost, point)
    visited = set()
    total_cost = 0

    while len(visited) < n:
        cost, point = heapq.heappop(min_heap)
        if point in visited:
            continue

        visited.add(point)
        total_cost += cost

        for next_cost, next_point in graph[point]:
            if next_point not in visited:
                heapq.heappush(min_heap, (next_cost, next_point))

    return total_cost