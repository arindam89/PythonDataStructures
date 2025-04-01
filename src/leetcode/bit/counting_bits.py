"""
LeetCode 338: Counting Bits
https://leetcode.com/problems/counting-bits/

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.

Example:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0  (0)
1 --> 1  (1)
2 --> 10 (1)
3 --> 11 (2)
4 --> 100 (1)
5 --> 101 (2)

Time Complexity: O(n)
Space Complexity: O(n) to store the results
"""

from typing import List

def count_bits(n: int) -> List[int]:
    """
    Count the number of 1's in binary representation of numbers from 0 to n.
    Uses dynamic programming: for number x, x//2 has same bits except possibly last one.
    
    Args:
        n: Upper bound integer
        
    Returns:
        List where index i contains count of 1's in binary representation of i
    """
    result = [0] * (n + 1)
    for i in range(1, n + 1):
        # i//2 has same bits as i except for least significant bit
        # Add 1 if i is odd (has 1 in least significant position)
        result[i] = result[i >> 1] + (i & 1)
    return result

def count_bits_pattern(n: int) -> List[int]:
    """
    Alternative implementation using pattern observation:
    Numbers can be grouped by their highest power of 2.
    
    Args:
        n: Upper bound integer
        
    Returns:
        List where index i contains count of 1's in binary representation of i
    """
    result = [0] * (n + 1)
    highest_power = 1  # Current highest power of 2
    
    for i in range(1, n + 1):
        if i == highest_power * 2:
            # When we reach a power of 2, update highest_power
            highest_power = i
            
        # Each number's count is 1 plus count in number without highest 1 bit
        result[i] = 1 + result[i - highest_power]
        
    return result