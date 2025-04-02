"""
Problem: Find the Duplicate Number
Link: https://leetcode.com/problems/find-the-duplicate-number/

Description:
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive. There is only one repeated number in nums, return this repeated number.

Approach:
1. Use Floyd's Tortoise and Hare (Cycle Detection) algorithm to detect the cycle.
2. Treat the array as a linked list where the value at each index points to the next index.
3. Find the intersection point of the cycle and then determine the entrance to the cycle, which is the duplicate number.

Time Complexity: O(n) - We traverse the array multiple times.
Space Complexity: O(1) - No additional space is used.
"""

def find_duplicate(nums):
    # Step 1: Detect the cycle
    slow, fast = nums[0], nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Step 2: Find the entrance to the cycle
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow