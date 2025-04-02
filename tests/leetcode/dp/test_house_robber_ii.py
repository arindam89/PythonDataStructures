import pytest
from src.leetcode.dp.house_robber_ii import rob

def test_rob():
    assert rob([2, 3, 2]) == 3  # Rob house 2
    assert rob([1, 2, 3, 1]) == 4  # Rob houses 2 and 4
    assert rob([0]) == 0  # No money to rob
    assert rob([1, 2, 3]) == 3  # Rob houses 2 and 3
    assert rob([5, 5, 10, 100, 10, 5]) == 110  # Rob houses 1, 4, 6