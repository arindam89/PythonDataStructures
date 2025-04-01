def unique_paths(m: int, n: int) -> int:
    """
    Calculate the number of unique paths in an m x n grid.

    Args:
        m (int): Number of rows.
        n (int): Number of columns.

    Returns:
        int: Number of unique paths.
    """
    # Create a 2D DP array
    dp = [[1] * n for _ in range(m)]

    # Fill the DP table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]

# Move this file to the dynamic_programming_2d folder.