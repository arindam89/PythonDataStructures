import pytest
from src.leetcode.dynamic_programming_2d.coin_change_ii import change

def test_change():
    # Test case 1: Example from problem statement
    assert change(5, [1, 2, 5]) == 4

    # Test case 2: No coins available
    assert change(3, []) == 0

    # Test case 3: Amount is zero
    assert change(0, [1, 2, 5]) == 1

    # Test case 4: Single coin type
    assert change(10, [10]) == 1

    # Test case 5: Multiple coin types
    assert change(7, [1, 2, 3]) == 8