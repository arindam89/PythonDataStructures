# Implementation of Dijkstra's Algorithm in Python
# Problem: Find the shortest path in a graph using Dijkstra's algorithm.
# LeetCode Link: https://leetcode.com/problems/network-delay-time/ (uses Dijkstra's algorithm)
import heapq

def dijkstra(graph, start):
    """Find the shortest path from the start node to all other nodes in the graph."""
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances