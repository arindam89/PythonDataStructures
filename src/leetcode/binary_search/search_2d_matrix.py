# Problem: Search a 2D Matrix
# Link: https://leetcode.com/problems/search-a-2d-matrix/
# Difficulty: Medium
#
# Approach:
# - Treat the 2D matrix as a flattened sorted array.
# - Use binary search to locate the target.
# - Calculate the row and column indices from the mid index during the search.
#
# Time Complexity: O(log(m * n)), where m is the number of rows and n is the number of columns.
# Space Complexity: O(1)

def search_matrix(matrix, target):
    """
    Perform binary search to find the target in a 2D matrix.

    :param matrix: List[List[int]] - A 2D matrix where each row is sorted and the first element of each row is greater than the last of the previous row.
    :param target: int - The target integer to find.
    :return: bool - True if the target is found, otherwise False.
    """
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = left + (right - left) // 2
        mid_value = matrix[mid // cols][mid % cols]

        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False