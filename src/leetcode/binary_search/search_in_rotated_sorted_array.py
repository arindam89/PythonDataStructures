# Problem: Search in Rotated Sorted Array
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
# Difficulty: Medium
#
# Approach:
# - Use binary search to find the target in a rotated sorted array.
# - Determine which half of the array is sorted and decide the search space accordingly.
# - Adjust the pointers based on the comparison with the target.
#
# Time Complexity: O(log n), where n is the length of the array.
# Space Complexity: O(1)

def search(nums, target):
    """
    Search for a target in a rotated sorted array.

    :param nums: List[int] - A rotated sorted array.
    :param target: int - The target integer to find.
    :return: int - The index of the target if found, otherwise -1.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        # Determine which half is sorted
        if nums[left] <= nums[mid]:
            # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1