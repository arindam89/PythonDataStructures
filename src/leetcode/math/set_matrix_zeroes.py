"""
LeetCode Problem: Set Matrix Zeroes
Link: https://leetcode.com/problems/set-matrix-zeroes/

Problem Statement:
Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Approach:
1. Use the first row and first column as markers to indicate whether a row or column should be zeroed.
2. Traverse the matrix to mark rows and columns that need to be zeroed.
3. Update the matrix using the markers.
4. Handle the first row and column separately to avoid overwriting markers.

Time Complexity: O(m * n), where m is the number of rows and n is the number of columns.
Space Complexity: O(1), as the operation is done in-place.
"""

def set_zeroes(matrix):
    """Sets entire row and column to 0's if an element is 0, in-place."""
    rows, cols = len(matrix), len(matrix[0])
    first_row_has_zero = any(matrix[0][j] == 0 for j in range(cols))
    first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows))

    # Use first row and column as markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Zero out cells based on markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Handle the first row
    if first_row_has_zero:
        for j in range(cols):
            matrix[0][j] = 0

    # Handle the first column
    if first_col_has_zero:
        for i in range(rows):
            matrix[i][0] = 0