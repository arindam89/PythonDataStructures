"""
LeetCode Problem: Spiral Matrix
Link: https://leetcode.com/problems/spiral-matrix/

Problem Statement:
Given an m x n matrix, return all elements of the matrix in spiral order.

Approach:
1. Use four pointers (top, bottom, left, right) to define the current boundary of the spiral.
2. Traverse the matrix in the order: left to right, top to bottom, right to left, and bottom to top.
3. Adjust the pointers after each traversal to move inward.
4. Stop when the pointers overlap.

Time Complexity: O(m * n), where m is the number of rows and n is the number of columns.
Space Complexity: O(1) additional space, excluding the output list.
"""

def spiral_order(matrix):
    """Returns all elements of the matrix in spiral order."""
    result = []
    if not matrix or not matrix[0]:
        return result

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse from left to right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Traverse from top to bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            # Traverse from right to left
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            # Traverse from bottom to top
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result