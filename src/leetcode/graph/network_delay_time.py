"""
Problem: Network Delay Time
Link: https://leetcode.com/problems/network-delay-time/

Approach:
- Use Dijkstra's algorithm to find the shortest time to reach all nodes from the source node.
- Represent the graph as an adjacency list.
- Use a priority queue to process nodes in order of their current shortest distance.
- If all nodes are reachable, return the maximum time among the shortest times to each node. Otherwise, return -1.

Time Complexity: O((V + E) * log(V)), where V is the number of nodes and E is the number of edges.
Space Complexity: O(V + E) for the graph representation and priority queue.
"""

import heapq
from collections import defaultdict

def network_delay_time(times, n, k):
    """
    Calculate the time it takes for all nodes to receive a signal from the source node.

    Args:
        times: List of edges represented as (u, v, w), where u is the source node,
               v is the target node, and w is the travel time.
        n: Total number of nodes.
        k: Starting node.

    Returns:
        The time it takes for all nodes to receive the signal, or -1 if not all nodes are reachable.
    """
    # Build the graph as an adjacency list
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    # Min-heap to store (time, node)
    min_heap = [(0, k)]
    shortest_time = {}

    while min_heap:
        time, node = heapq.heappop(min_heap)

        if node in shortest_time:
            continue

        shortest_time[node] = time

        for neighbor, weight in graph[node]:
            if neighbor not in shortest_time:
                heapq.heappush(min_heap, (time + weight, neighbor))

    return max(shortest_time.values()) if len(shortest_time) == n else -1