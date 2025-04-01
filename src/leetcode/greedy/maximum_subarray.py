def max_subarray(nums):
    """
    LeetCode Problem 53: Maximum Subarray
    Link: https://leetcode.com/problems/maximum-subarray/

    Problem:
    Given an integer array nums, find the contiguous subarray (containing at least one number) 
    which has the largest sum and return its sum.

    Approach:
    - Use Kadane's Algorithm to find the maximum sum of a contiguous subarray.
    - Maintain two variables: max_current (current subarray sum) and max_global (maximum sum found so far).
    - Iterate through the array, updating max_current and max_global as needed.

    Args:
        nums (List[int]): List of integers.

    Returns:
        int: The largest sum of the contiguous subarray.
    """
    max_current = max_global = nums[0]  # Initialize with the first element

    for i in range(1, len(nums)):
        # Update max_current to include the current element or start a new subarray
        max_current = max(nums[i], max_current + nums[i])
        # Update max_global if the current subarray sum is the largest so far
        if max_current > max_global:
            max_global = max_current

    return max_global