"""
LeetCode 322: Coin Change
https://leetcode.com/problems/coin-change/

You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money. Return the fewest
number of coins that you need to make up that amount. If that amount of money
cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Time Complexity: O(amount * len(coins))
Space Complexity: O(amount)
"""

from typing import List

def coin_change(coins: List[int], amount: int) -> int:
    """
    Find the minimum number of coins needed to make up the amount.
    Uses bottom-up dynamic programming approach.
    
    Args:
        coins: List of coin denominations
        amount: Target amount
        
    Returns:
        Minimum number of coins needed, or -1 if impossible
    """
    # dp[i] represents the minimum coins needed for amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0
    
    # Build up solution for all amounts from 1 to target
    for i in range(1, amount + 1):
        # Try each coin denomination
        for coin in coins:
            if coin <= i:
                # Use this coin + minimum coins needed for remaining amount
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
    return dp[amount] if dp[amount] != float('inf') else -1