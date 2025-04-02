"""
LeetCode Problem: Min Cost Climbing Stairs
Link: https://leetcode.com/problems/min-cost-climbing-stairs/

You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.
You need to find the minimum cost to reach the top of the floor.

Approach:
This is a dynamic programming problem. We calculate the minimum cost to reach each step iteratively.
The cost to reach step `i` is the cost of step `i` plus the minimum of the costs to reach steps `i-1` and `i-2`.
We can solve this with O(n) time complexity and O(1) space complexity.
"""

def min_cost_climbing_stairs(cost: list[int]) -> int:
    n = len(cost)
    if n == 2:
        return min(cost)

    prev, curr = cost[0], cost[1]
    for i in range(2, n):
        prev, curr = curr, cost[i] + min(prev, curr)

    return min(prev, curr)