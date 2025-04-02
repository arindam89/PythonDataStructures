# Problem: Binary Search
# Link: https://leetcode.com/problems/binary-search/
# Difficulty: Easy
#
# Approach:
# - Use a classic binary search algorithm to find the target in a sorted array.
# - Start with two pointers, left and right, representing the bounds of the search space.
# - Calculate the middle index and compare the middle element with the target.
# - Adjust the pointers based on the comparison until the target is found or the search space is empty.
#
# Time Complexity: O(log n), where n is the length of the array.
# Space Complexity: O(1)

def binary_search(nums, target):
    """
    Perform binary search to find the target in a sorted array.

    :param nums: List[int] - A sorted list of integers.
    :param target: int - The target integer to find.
    :return: int - The index of the target if found, otherwise -1.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1