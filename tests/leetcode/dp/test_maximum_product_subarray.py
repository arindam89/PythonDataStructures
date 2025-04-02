import pytest
from src.leetcode.dp.maximum_product_subarray import max_product

def test_max_product():
    assert max_product([2, 3, -2, 4]) == 6  # Subarray [2, 3] has the maximum product
    assert max_product([-2, 0, -1]) == 0  # Subarray [0] has the maximum product
    assert max_product([0, 2]) == 2  # Subarray [2] has the maximum product
    assert max_product([-2, 3, -4]) == 24  # Subarray [-2, 3, -4] has the maximum product
    assert max_product([2, -5, -2, -4, 3]) == 240  # Subarray [2, -5, -2, -4, 3] has the maximum product