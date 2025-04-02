"""
LeetCode Problem: Reverse Bits
Link: https://leetcode.com/problems/reverse-bits/

Problem Statement:
Reverse bits of a given 32 bits unsigned integer.

Approach:
1. Use bit manipulation to reverse the bits.
2. Iterate through all 32 bits, shifting the result left and adding the last bit of n.
3. Shift n right to process the next bit.

Time Complexity: O(1), as the number of bits is fixed (32).
Space Complexity: O(1).
"""

def reverse_bits(n):
    """Reverses the bits of a 32-bit unsigned integer."""
    result = 0
    for i in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result