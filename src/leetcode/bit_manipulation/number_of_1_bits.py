"""
LeetCode Problem: Number of 1 Bits
Link: https://leetcode.com/problems/number-of-1-bits/

Problem Statement:
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Approach:
1. Use bit manipulation to count the number of 1s.
2. Perform n & (n - 1) to turn off the rightmost 1 bit until n becomes 0.

Time Complexity: O(k), where k is the number of 1 bits in the integer.
Space Complexity: O(1).
"""

def hamming_weight(n):
    """Returns the number of '1' bits in the binary representation of n."""
    count = 0
    while n:
        n &= (n - 1)  # Turn off the rightmost 1 bit
        count += 1
    return count