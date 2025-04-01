import pytest
from src.leetcode.dynamic_programming_2d.target_sum import find_target_sum_ways

def test_find_target_sum_ways():
    # Test case 1: Example from problem statement
    assert find_target_sum_ways([1, 1, 1, 1, 1], 3) == 5

    # Test case 2: Single element equal to target
    assert find_target_sum_ways([1], 1) == 1

    # Test case 3: Single element not equal to target
    assert find_target_sum_ways([1], 2) == 0

    # Test case 4: Multiple ways to achieve target
    assert find_target_sum_ways([1, 2, 3, 4, 5], 3) == 3

    # Test case 5: No possible way to achieve target
    assert find_target_sum_ways([1, 2, 7, 9], 4) == 0