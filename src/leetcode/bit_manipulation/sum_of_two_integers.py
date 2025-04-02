"""
LeetCode Problem: Sum of Two Integers
Link: https://leetcode.com/problems/sum-of-two-integers/

Problem Statement:
Given two integers a and b, return the sum of the two integers without using the operators + and -.

Approach:
1. Use bit manipulation to calculate the sum.
2. Use XOR to calculate the sum without carry.
3. Use AND and left shift to calculate the carry.
4. Repeat until there is no carry.

Time Complexity: O(1), as the number of bits is fixed (32).
Space Complexity: O(1).
"""

def get_sum(a, b):
    """Returns the sum of two integers without using + or - operators."""
    MASK = 0xFFFFFFFF  # Mask to get last 32 bits
    MAX_INT = 0x7FFFFFFF  # Maximum positive integer for 32 bits

    while b != 0:
        carry = (a & b) & MASK
        a = (a ^ b) & MASK
        b = (carry << 1) & MASK

    # If a is negative, convert it to a signed integer
    return a if a <= MAX_INT else ~(a ^ MASK)