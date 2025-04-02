"""
LeetCode Problem: Reverse Integer
Link: https://leetcode.com/problems/reverse-integer/

Problem Statement:
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Approach:
1. Extract the digits of the integer using modulo and division.
2. Reconstruct the reversed integer.
3. Check for overflow/underflow conditions.

Time Complexity: O(log(x)), where x is the input integer.
Space Complexity: O(1).
"""

def reverse(x):
    """Reverses the digits of a 32-bit signed integer."""
    INT_MAX, INT_MIN = 2**31 - 1, -2**31
    result = 0

    sign = -1 if x < 0 else 1
    x = abs(x)

    while x != 0:
        digit = x % 10
        x //= 10

        # Check for overflow/underflow
        if result > (INT_MAX - digit) // 10:
            return 0

        result = result * 10 + digit

    return sign * result