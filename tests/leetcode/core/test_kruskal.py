import unittest
from leetcode.core.kruskal import kruskal

class TestKruskal(unittest.TestCase):

    def test_mst(self):
        edges = [
            (0, 1, 1),
            (1, 2, 2),
            (0, 2, 4),
            (1, 3, 6),
            (2, 3, 3)
        ]
        num_nodes = 4
        result = kruskal(edges, num_nodes)
        expected = [(0, 1, 1), (1, 2, 2), (2, 3, 3)]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()