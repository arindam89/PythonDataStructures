"""
LeetCode Problem: Plus One
Link: https://leetcode.com/problems/plus-one/

Problem Statement:
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Approach:
1. Traverse the array from the last digit to the first.
2. Add one to the last digit and handle the carry.
3. If there is a carry after processing all digits, prepend 1 to the array.

Time Complexity: O(n), where n is the number of digits.
Space Complexity: O(1) additional space.
"""

def plus_one(digits):
    """Increments the large integer represented by digits by one."""
    n = len(digits)

    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    # If all digits were 9, we need to add a leading 1
    return [1] + digits