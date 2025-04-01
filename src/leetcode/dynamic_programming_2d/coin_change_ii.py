def change(amount, coins):
    """
    Calculate the number of combinations to make up the amount.

    Args:
        amount (int): Total amount of money.
        coins (List[int]): List of coin denominations.

    Returns:
        int: Number of combinations to make up the amount.
    """
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]

    return dp[amount]