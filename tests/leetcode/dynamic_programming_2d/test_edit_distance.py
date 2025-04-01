import pytest
from src.leetcode.dynamic_programming_2d.edit_distance import min_distance

def test_min_distance():
    # Test case 1: Example from problem statement
    assert min_distance("horse", "ros") == 3

    # Test case 2: Both strings are empty
    assert min_distance("", "") == 0

    # Test case 3: One string is empty
    assert min_distance("abc", "") == 3
    assert min_distance("", "abc") == 3

    # Test case 4: Strings are the same
    assert min_distance("abc", "abc") == 0

    # Test case 5: General case
    assert min_distance("intention", "execution") == 5