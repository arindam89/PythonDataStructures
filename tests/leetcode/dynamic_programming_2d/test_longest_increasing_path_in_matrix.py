import pytest
from src.leetcode.dynamic_programming_2d.longest_increasing_path_in_matrix import longest_increasing_path

def test_longest_increasing_path():
    # Test case 1: Example from problem statement
    matrix = [
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
    ]
    assert longest_increasing_path(matrix) == 4

    # Test case 2: Single element matrix
    assert longest_increasing_path([[1]]) == 1

    # Test case 3: All elements are the same
    assert longest_increasing_path([[7, 7], [7, 7]]) == 1

    # Test case 4: Increasing row-wise
    assert longest_increasing_path([[1, 2, 3], [6, 5, 4]]) == 6

    # Test case 5: Empty matrix
    assert longest_increasing_path([]) == 0