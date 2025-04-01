import pytest
from src.leetcode.dynamic_programming_2d.distinct_subsequences import num_distinct

def test_num_distinct():
    # Test case 1: Example from problem statement
    assert num_distinct("rabbbit", "rabbit") == 3

    # Test case 2: No subsequences match
    assert num_distinct("abc", "d") == 0

    # Test case 3: Source and target are the same
    assert num_distinct("abc", "abc") == 1

    # Test case 4: Target is empty
    assert num_distinct("abc", "") == 1

    # Test case 5: Source is empty
    assert num_distinct("", "abc") == 0