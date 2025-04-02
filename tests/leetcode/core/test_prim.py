import unittest
from leetcode.core.prim import prim

class TestPrim(unittest.TestCase):

    def test_mst(self):
        graph = {
            'A': [('B', 1), ('C', 4)],
            'B': [('A', 1), ('C', 2), ('D', 6)],
            'C': [('A', 4), ('B', 2), ('D', 3)],
            'D': [('B', 6), ('C', 3)]
        }
        result = prim(graph, 'A')
        expected = [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 3)]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()