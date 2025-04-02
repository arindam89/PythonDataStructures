"""
LeetCode Problem: Rotate Image
Link: https://leetcode.com/problems/rotate-image/

Problem Statement:
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Approach:
1. Transpose the matrix: Convert rows to columns.
2. Reverse each row: This will achieve a 90-degree clockwise rotation.

Time Complexity: O(n^2), where n is the number of rows (or columns) in the matrix.
Space Complexity: O(1), as the rotation is done in-place.
"""

def rotate(matrix):
    """Rotates the given n x n matrix by 90 degrees clockwise in-place."""
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()