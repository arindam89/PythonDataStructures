"""
Test cases for the Network Delay Time problem.

Additional Notes:
- The test cases cover various scenarios, including:
  1. A graph where all nodes are reachable.
  2. A graph where not all nodes are reachable.
  3. A graph with a single node.
  4. A graph with multiple paths to the same node.
"""

import unittest
from src.leetcode.graph.network_delay_time import network_delay_time

class TestNetworkDelayTime(unittest.TestCase):
    def test_all_nodes_reachable(self):
        times = [
            [2, 1, 1],
            [2, 3, 1],
            [3, 4, 1]
        ]
        n = 4
        k = 2
        self.assertEqual(network_delay_time(times, n, k), 2)

    def test_not_all_nodes_reachable(self):
        times = [
            [1, 2, 1]
        ]
        n = 2
        k = 1
        self.assertEqual(network_delay_time(times, n, k), -1)

    def test_single_node(self):
        times = []
        n = 1
        k = 1
        self.assertEqual(network_delay_time(times, n, k), 0)

    def test_multiple_paths(self):
        times = [
            [1, 2, 1],
            [1, 3, 4],
            [2, 3, 2]
        ]
        n = 3
        k = 1
        self.assertEqual(network_delay_time(times, n, k), 3)

if __name__ == "__main__":
    unittest.main()