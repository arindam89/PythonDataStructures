"""
Problem: Clone Graph
Link: https://leetcode.com/problems/clone-graph/

Approach:
- Use Depth First Search (DFS) or Breadth First Search (BFS) to traverse the graph.
- Maintain a mapping of original nodes to their cloned counterparts to avoid revisiting nodes.
- For each node, clone it and recursively clone its neighbors.

Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges.
Space Complexity: O(V) for the visited dictionary and recursion stack.

Additional Notes:
- This implementation uses DFS for graph traversal.
- The `visited` dictionary ensures that each node is cloned only once, preventing infinite loops in cyclic graphs.
- The `Node` class represents a graph node with a value and a list of neighbors.
"""

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node):
    if not node:
        return None

    # Dictionary to store the mapping from original nodes to their clones
    visited = {}

    def dfs(original_node):
        # If the node is already cloned, return the clone
        if original_node in visited:
            return visited[original_node]

        # Clone the node (without neighbors initially)
        clone = Node(original_node.val)
        visited[original_node] = clone

        # Recursively clone all neighbors
        for neighbor in original_node.neighbors:
            clone.neighbors.append(dfs(neighbor))

        return clone

    # Start DFS from the given node
    return dfs(node)