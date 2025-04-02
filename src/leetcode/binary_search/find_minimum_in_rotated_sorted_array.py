# Problem: Find Minimum in Rotated Sorted Array
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Difficulty: Medium
#
# Approach:
# - Use binary search to find the minimum element in a rotated sorted array.
# - Compare the middle element with the rightmost element to decide the search space.
# - If the middle element is greater than the rightmost, the minimum is in the right half.
# - Otherwise, the minimum is in the left half.
#
# Time Complexity: O(log n), where n is the length of the array.
# Space Complexity: O(1)

def find_min(nums):
    """
    Find the minimum element in a rotated sorted array.

    :param nums: List[int] - A rotated sorted array.
    :return: int - The minimum element in the array.
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]