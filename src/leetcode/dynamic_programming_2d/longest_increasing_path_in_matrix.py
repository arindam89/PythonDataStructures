def longest_increasing_path(matrix):
    """
    Find the length of the longest increasing path in a matrix.

    Args:
        matrix (List[List[int]]): 2D grid of integers.

    Returns:
        int: Length of the longest increasing path.
    """
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    dp = [[-1] * cols for _ in range(rows)]

    def dfs(r, c, prev_val):
        if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] <= prev_val:
            return 0

        if dp[r][c] != -1:
            return dp[r][c]

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        max_path = 0

        for dr, dc in directions:
            max_path = max(max_path, dfs(r + dr, c + dc, matrix[r][c]))

        dp[r][c] = 1 + max_path
        return dp[r][c]

    longest_path = 0
    for r in range(rows):
        for c in range(cols):
            longest_path = max(longest_path, dfs(r, c, -float('inf')))

    return longest_path