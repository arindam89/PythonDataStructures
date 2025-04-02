"""
Problem: Walls and Gates
Link: https://leetcode.com/problems/walls-and-gates/

Approach:
- Use Breadth First Search (BFS) starting from all gates (cells with value 0).
- For each gate, update the distance of its neighboring empty rooms (cells with value INF) to the gate.
- Continue the BFS until all reachable empty rooms are updated.

Time Complexity: O(M * N), where M is the number of rows and N is the number of columns in the grid.
Space Complexity: O(M * N) for the BFS queue.

Additional Notes:
- The grid is modified in-place to update the distances.
- The algorithm ensures that each cell is processed only once, making it efficient for large grids.
- INF is used to represent empty rooms, and the result is the minimum distance to the nearest gate for each room.
"""

from collections import deque

def walls_and_gates(rooms):
    if not rooms or not rooms[0]:
        return

    INF = 2**31 - 1
    rows, cols = len(rooms), len(rooms[0])
    queue = deque()

    # Add all gates to the queue
    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                queue.append((r, c))

    # Perform BFS from all gates
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                rooms[nr][nc] = rooms[r][c] + 1
                queue.append((nr, nc))