# Implementation of Matrix Breadth-First Search (BFS) in Python
# Problem: Perform BFS on a 2D matrix.
# LeetCode Link: https://leetcode.com/problems/shortest-path-in-binary-matrix/ (uses BFS)
from collections import deque

def matrix_bfs(matrix):
    """Perform BFS on a 2D matrix and return the visited nodes."""
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs(r, c):
        queue = deque([(r, c)])
        visited[r][c] = True
        while queue:
            x, y = queue.popleft()
            for dr, dc in directions:
                nr, nc = x + dr, y + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and matrix[nr][nc] == 1:
                    visited[nr][nc] = True
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1 and not visited[r][c]:
                bfs(r, c)

    return visited