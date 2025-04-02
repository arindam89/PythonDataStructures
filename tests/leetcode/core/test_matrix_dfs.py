import unittest
from leetcode.core.matrix_dfs import matrix_dfs

class TestMatrixDFS(unittest.TestCase):

    def test_dfs(self):
        matrix = [
            [1, 1, 0, 0],
            [1, 0, 0, 1],
            [0, 0, 1, 1],
            [0, 1, 1, 0]
        ]
        visited = matrix_dfs(matrix)
        expected = [
            [True, True, False, False],
            [True, False, False, True],
            [False, False, True, True],
            [False, True, True, False]
        ]
        self.assertEqual(visited, expected)

if __name__ == "__main__":
    unittest.main()