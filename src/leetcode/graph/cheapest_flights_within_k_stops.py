"""
Problem: Cheapest Flights Within K Stops
Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/

Approach:
- Use a modified version of Dijkstra's algorithm to find the cheapest flight within K stops.
- Represent the graph as an adjacency list, where each node points to its neighbors with the cost of the flight.
- Use a priority queue to process nodes in order of their current cost.
- Keep track of the number of stops to ensure the constraint is met.

Time Complexity: O(E + V * log(V)), where E is the number of edges and V is the number of vertices.
Space Complexity: O(V + E) for the graph representation and priority queue.
"""

import heapq
from collections import defaultdict

def find_cheapest_price(n, flights, src, dst, k):
    """
    Calculate the cheapest price to travel from src to dst with at most k stops.

    Args:
        n: Number of cities.
        flights: List of [from, to, price] flights.
        src: Starting city.
        dst: Destination city.
        k: Maximum number of stops.

    Returns:
        The cheapest price, or -1 if no such route exists.
    """
    # Build the graph as an adjacency list
    graph = defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))

    # Min-heap to store (cost, city, stops)
    min_heap = [(0, src, 0)]

    while min_heap:
        cost, city, stops = heapq.heappop(min_heap)

        # If we reach the destination, return the cost
        if city == dst:
            return cost

        # If we have stops left, explore neighbors
        if stops <= k:
            for neighbor, price in graph[city]:
                heapq.heappush(min_heap, (cost + price, neighbor, stops + 1))

    return -1