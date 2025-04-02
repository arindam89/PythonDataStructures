import unittest
from leetcode.core.topological_sort import topological_sort

class TestTopologicalSort(unittest.TestCase):

    def test_dag(self):
        num_nodes = 6
        edges = [
            (5, 2),
            (5, 0),
            (4, 0),
            (4, 1),
            (2, 3),
            (3, 1)
        ]
        result = topological_sort(num_nodes, edges)
        expected = [5, 4, 2, 3, 1, 0]  # One possible valid order
        self.assertEqual(result, expected)

    def test_cycle(self):
        num_nodes = 3
        edges = [
            (0, 1),
            (1, 2),
            (2, 0)
        ]
        result = topological_sort(num_nodes, edges)
        self.assertEqual(result, [])  # Cycle detected, no valid order

if __name__ == "__main__":
    unittest.main()