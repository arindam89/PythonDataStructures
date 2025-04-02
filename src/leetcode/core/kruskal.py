# Implementation of Kruskal's Algorithm in Python
# Problem: Find the Minimum Spanning Tree (MST) of a graph using Kruskal's algorithm.
# LeetCode Link: https://leetcode.com/problems/min-cost-to-connect-all-points/ (uses Kruskal's algorithm)

def kruskal(edges, num_nodes):
    """Find the MST of a graph using Kruskal's algorithm."""
    edges.sort(key=lambda x: x[2])  # Sort edges by weight
    parent = list(range(num_nodes))
    rank = [0] * num_nodes

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])  # Path compression
        return parent[node]

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1

    mst = []
    for u, v, weight in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, weight))

    return mst