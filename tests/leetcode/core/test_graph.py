import unittest
from leetcode.core.graph import Graph

class TestGraph(unittest.TestCase):

    def test_add_vertex(self):
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        self.assertIn("A", graph.adjacency_list)
        self.assertIn("B", graph.adjacency_list)

    def test_add_edge(self):
        graph = Graph()
        graph.add_edge("A", "B")
        self.assertIn("B", graph.adjacency_list["A"])
        self.assertIn("A", graph.adjacency_list["B"])

    def test_is_adjacent(self):
        graph = Graph()
        graph.add_edge("A", "B")
        self.assertTrue(graph.is_adjacent("A", "B"))
        self.assertFalse(graph.is_adjacent("A", "C"))

if __name__ == "__main__":
    unittest.main()