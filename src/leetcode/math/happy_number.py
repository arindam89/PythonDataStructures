"""
LeetCode Problem: Happy Number
Link: https://leetcode.com/problems/happy-number/

Problem Statement:
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (it will stay at 1), or it loops endlessly in a cycle that does not include 1.
- Those numbers for which this process ends in 1 are happy.

Approach:
1. Use a set to track numbers we've seen to detect cycles.
2. Calculate the sum of the squares of the digits repeatedly.
3. If the number becomes 1, return True. If a cycle is detected, return False.

Time Complexity: O(log n), where n is the input number.
Space Complexity: O(log n), due to the storage of seen numbers.
"""

def is_happy(n):
    """Determines if a number is happy."""
    def get_next(number):
        return sum(int(digit) ** 2 for digit in str(number))

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)

    return n == 1