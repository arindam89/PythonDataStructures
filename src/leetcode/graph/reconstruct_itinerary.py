"""
Problem: Reconstruct Itinerary
Link: https://leetcode.com/problems/reconstruct-itinerary/

Approach:
- Use Hierholzer's algorithm to find an Eulerian path in the graph.
- Represent the graph as an adjacency list, where each node points to a sorted list of destinations.
- Perform a Depth First Search (DFS) to construct the itinerary.
- Since the graph is directed and may have multiple valid paths, always visit the smallest lexical airport first.

Time Complexity: O(E * log(E/V)), where E is the number of edges and V is the number of vertices.
Space Complexity: O(V + E) for the graph representation and recursion stack.
"""

from collections import defaultdict

def find_itinerary(tickets):
    """
    Reconstruct the itinerary from a list of flight tickets.

    Args:
        tickets: List of [from, to] flight tickets.

    Returns:
        The itinerary as a list of airport codes.
    """
    # Build the graph as an adjacency list
    graph = defaultdict(list)
    for src, dest in sorted(tickets):
        graph[src].append(dest)

    itinerary = []

    def dfs(airport):
        """
        Perform DFS to construct the itinerary.

        Args:
            airport: Current airport code.
        """
        while graph[airport]:
            next_airport = graph[airport].pop(0)
            dfs(next_airport)
        itinerary.append(airport)

    # Start the DFS from 'JFK'
    dfs('JFK')

    return itinerary[::-1]