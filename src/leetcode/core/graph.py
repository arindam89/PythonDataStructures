# Implementation of a Graph in Python
# Problem: Design a graph that supports operations like add vertex, add edge, and check adjacency.
# LeetCode Link: Not directly available, but this is a fundamental data structure.

class Graph:
    def __init__(self):
        """Initialize the graph as an adjacency list."""
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """Add an edge between two vertices."""
        if vertex1 not in self.adjacency_list:
            self.add_vertex(vertex1)
        if vertex2 not in self.adjacency_list:
            self.add_vertex(vertex2)
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)

    def is_adjacent(self, vertex1, vertex2):
        """Check if two vertices are adjacent."""
        return vertex2 in self.adjacency_list.get(vertex1, [])

    def __str__(self):
        """Return a string representation of the graph."""
        return str(self.adjacency_list)