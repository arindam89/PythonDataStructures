def is_interleave(s1, s2, s3):
    """
    Determine if s3 is formed by interleaving s1 and s2.

    Args:
        s1 (str): First string.
        s2 (str): Second string.
        s3 (str): Target string.

    Returns:
        bool: True if s3 is an interleaving of s1 and s2, False otherwise.
    """
    if len(s1) + len(s2) != len(s3):
        return False

    dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    dp[0][0] = True

    for i in range(1, len(s1) + 1):
        dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

    for j in range(1, len(s2) + 1):
        dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                       (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])

    return dp[len(s1)][len(s2)]