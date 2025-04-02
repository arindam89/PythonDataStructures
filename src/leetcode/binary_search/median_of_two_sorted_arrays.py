# Problem: Median of Two Sorted Arrays
# Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
# Difficulty: Hard
#
# Approach:
# - Use binary search to partition the smaller array such that the left and right partitions of both arrays are balanced.
# - Ensure that all elements in the left partition are less than or equal to all elements in the right partition.
# - Calculate the median based on the partitioning.
#
# Time Complexity: O(log(min(m, n))), where m and n are the lengths of the two arrays.
# Space Complexity: O(1)

def find_median_sorted_arrays(nums1, nums2):
    """
    Find the median of two sorted arrays.

    :param nums1: List[int] - The first sorted array.
    :param nums2: List[int] - The second sorted array.
    :return: float - The median of the two arrays.
    """
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    x, y = len(nums1), len(nums2)
    low, high = 0, x

    while low <= high:
        partition_x = (low + high) // 2
        partition_y = (x + y + 1) // 2 - partition_x

        max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
        min_right_x = float('inf') if partition_x == x else nums1[partition_x]

        max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
        min_right_y = float('inf') if partition_y == y else nums2[partition_y]

        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            if (x + y) % 2 == 0:
                return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
            else:
                return max(max_left_x, max_left_y)
        elif max_left_x > min_right_y:
            high = partition_x - 1
        else:
            low = partition_x + 1

    raise ValueError("Input arrays are not sorted.")