import unittest
from leetcode.core.dijkstra import dijkstra

class TestDijkstra(unittest.TestCase):

    def test_shortest_path(self):
        graph = {
            'A': [('B', 1), ('C', 4)],
            'B': [('A', 1), ('C', 2), ('D', 6)],
            'C': [('A', 4), ('B', 2), ('D', 3)],
            'D': [('B', 6), ('C', 3)]
        }
        result = dijkstra(graph, 'A')
        expected = {'A': 0, 'B': 1, 'C': 3, 'D': 6}
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()