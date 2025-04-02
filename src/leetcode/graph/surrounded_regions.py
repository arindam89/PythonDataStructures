"""
Problem: Surrounded Regions
Link: https://leetcode.com/problems/surrounded-regions/

Approach:
- Use Depth First Search (DFS) or Breadth First Search (BFS) to mark all 'O's connected to the border as safe.
- Traverse the grid and flip all unmarked 'O's to 'X' (as they are surrounded) and revert marked 'O's back to 'O'.

Time Complexity: O(M * N), where M is the number of rows and N is the number of columns in the grid.
Space Complexity: O(M * N) for the visited set or recursion stack.

Additional Notes:
- The algorithm ensures that only 'O's not connected to the border are flipped to 'X'.
- The grid is modified in-place to mark safe cells temporarily as 'S'.
"""

def solve(board):
    if not board or not board[0]:
        return

    rows, cols = len(board), len(board[0])

    def dfs(r, c):
        """
        Perform DFS to mark all 'O's connected to the border as safe.

        Args:
            r: Row index of the current cell
            c: Column index of the current cell
        """
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
            return

        board[r][c] = 'S'  # Mark as safe
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in directions:
            dfs(r + dr, c + dc)

    # Mark all 'O's connected to the border as safe
    for r in range(rows):
        dfs(r, 0)
        dfs(r, cols - 1)
    for c in range(cols):
        dfs(0, c)
        dfs(rows - 1, c)

    # Flip all unmarked 'O's to 'X' and revert 'S' back to 'O'
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            elif board[r][c] == 'S':
                board[r][c] = 'O'