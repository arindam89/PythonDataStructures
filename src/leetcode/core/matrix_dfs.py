# Implementation of Matrix Depth-First Search (DFS) in Python
# Problem: Perform DFS on a 2D matrix.
# LeetCode Link: https://leetcode.com/problems/number-of-islands/ (uses DFS)

def matrix_dfs(matrix):
    """Perform DFS on a 2D matrix and return the visited nodes."""
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or visited[r][c] or matrix[r][c] == 0:
            return
        visited[r][c] = True
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1 and not visited[r][c]:
                dfs(r, c)

    return visited