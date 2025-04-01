def jump(nums):
    """
    LeetCode Problem 45: Jump Game II
    Link: https://leetcode.com/problems/jump-game-ii/

    Problem:
    Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
    Each element in the array represents your maximum jump length at that position.
    Your goal is to reach the last index in the minimum number of jumps.

    Approach:
    - Use a greedy approach to minimize the number of jumps.
    - Track the farthest index that can be reached in the current jump range.
    - Increment the jump count whenever the end of the current range is reached.

    Args:
        nums (List[int]): List of non-negative integers representing the maximum jump length at each position.

    Returns:
        int: Minimum number of jumps to reach the last index.
    """
    jumps = 0  # Number of jumps made so far
    current_end = 0  # End of the current jump range
    farthest = 0  # Farthest index that can be reached

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])  # Update the farthest reachable index
        if i == current_end:  # If the end of the current range is reached
            jumps += 1  # Increment the jump count
            current_end = farthest  # Update the current range to the farthest index

    return jumps