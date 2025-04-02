import pytest
from src.leetcode.dp.house_robber import rob

def test_rob():
    assert rob([1, 2, 3, 1]) == 4  # Rob houses 1 and 3
    assert rob([2, 7, 9, 3, 1]) == 12  # Rob houses 2, 4
    assert rob([0]) == 0  # No money to rob
    assert rob([5, 5, 10, 100, 10, 5]) == 110  # Rob houses 1, 4, 6
    assert rob([]) == 0  # No houses to rob