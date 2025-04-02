# Implementation of Disjoint Set (Union-Find) in Python
# Problem: Design a disjoint set that supports union and find operations.
# LeetCode Link: https://leetcode.com/problems/redundant-connection/ (uses union-find)

class DisjointSet:
    def __init__(self, size):
        """Initialize the disjoint set with the given size."""
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        """Find the representative of the set containing x."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        """Union the sets containing x and y."""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

    def connected(self, x, y):
        """Check if x and y are in the same set."""
        return self.find(x) == self.find(y)