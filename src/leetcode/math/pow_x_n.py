"""
LeetCode Problem: Pow(x, n)
Link: https://leetcode.com/problems/powx-n/

Problem Statement:
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Approach:
1. Use a recursive approach to calculate the power efficiently.
2. If n is negative, calculate the power for -n and take the reciprocal.
3. Use the property x^n = x^(n//2) * x^(n//2) for even n, and x^n = x^(n//2) * x^(n//2) * x for odd n.

Time Complexity: O(log n), where n is the exponent.
Space Complexity: O(log n), due to the recursion stack.
"""

def my_pow(x, n):
    """Calculates x raised to the power n."""
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n = -n

    half = my_pow(x, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return half * half * x