# Implementation of Prim's Algorithm in Python
# Problem: Find the Minimum Spanning Tree (MST) of a graph using Prim's algorithm.
# LeetCode Link: https://leetcode.com/problems/connecting-cities-with-minimum-cost/ (uses Prim's algorithm)
import heapq

def prim(graph, start):
    """Find the MST of a graph using Prim's algorithm."""
    mst = []
    visited = set()
    min_heap = [(0, start, None)]  # (weight, current_node, parent_node)

    while min_heap:
        weight, current, parent = heapq.heappop(min_heap)
        if current in visited:
            continue
        visited.add(current)
        if parent is not None:
            mst.append((parent, current, weight))

        for neighbor, edge_weight in graph[current]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current))

    return mst