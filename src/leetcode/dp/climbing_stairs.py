"""
LeetCode Problem: Climbing Stairs
Link: https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Approach:
This is a classic dynamic programming problem. The number of ways to reach step `i` is the sum of the ways to reach step `i-1` and step `i-2`.
We can solve this iteratively with O(n) time complexity and O(1) space complexity.
"""

def climb_stairs(n: int) -> int:
    if n <= 2:
        return n

    prev, curr = 1, 2
    for i in range(3, n + 1):
        prev, curr = curr, prev + curr

    return curr