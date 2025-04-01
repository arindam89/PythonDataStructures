def can_jump(nums):
    """
    LeetCode Problem 55: Jump Game
    Link: https://leetcode.com/problems/jump-game/

    Problem:
    Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
    Each element in the array represents your maximum jump length at that position.
    Determine if you are able to reach the last index.

    Approach:
    - Use a greedy approach to track the farthest index that can be reached.
    - Iterate through the array and update the maximum reachable index.
    - If at any point the current index exceeds the maximum reachable index, return False.

    Args:
        nums (List[int]): List of non-negative integers representing the maximum jump length at each position.

    Returns:
        bool: True if you can reach the last index, False otherwise.
    """
    max_reachable = 0  # Tracks the farthest index that can be reached

    for i, num in enumerate(nums):
        if i > max_reachable:  # If the current index is not reachable, return False
            return False
        max_reachable = max(max_reachable, i + num)  # Update the farthest reachable index

    return True