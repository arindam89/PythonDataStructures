"""
Test cases for the Clone Graph problem.

Additional Notes:
- The test cases cover various scenarios, including:
  1. A graph with multiple nodes and edges.
  2. An empty graph (None input).
  3. A graph with a single node and no edges.
  4. A cyclic graph to ensure no infinite loops occur.
"""

import unittest
from src.leetcode.graph.clone_graph import Node, clone_graph

class TestCloneGraph(unittest.TestCase):
    def test_example_case(self):
        # Create a graph: 1 -- 2
        #                 |    |
        #                 4 -- 3
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)

        node1.neighbors = [node2, node4]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node2, node4]
        node4.neighbors = [node1, node3]

        cloned = clone_graph(node1)

        self.assertEqual(cloned.val, 1)
        self.assertEqual(len(cloned.neighbors), 2)
        self.assertEqual(cloned.neighbors[0].val, 2)
        self.assertEqual(cloned.neighbors[1].val, 4)

    def test_empty_graph(self):
        self.assertIsNone(clone_graph(None))

    def test_single_node(self):
        node = Node(1)
        cloned = clone_graph(node)
        self.assertEqual(cloned.val, 1)
        self.assertEqual(len(cloned.neighbors), 0)

    def test_cyclic_graph(self):
        # Create a cyclic graph: 1 -- 2
        #                        |    |
        #                        \-- 3
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)

        node1.neighbors = [node2, node3]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node1, node2]

        cloned = clone_graph(node1)

        self.assertEqual(cloned.val, 1)
        self.assertEqual(len(cloned.neighbors), 2)
        self.assertEqual(cloned.neighbors[0].val, 2)
        self.assertEqual(cloned.neighbors[1].val, 3)

if __name__ == "__main__":
    unittest.main()