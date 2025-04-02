import pytest
from src.leetcode.dp.min_cost_climbing_stairs import min_cost_climbing_stairs

def test_min_cost_climbing_stairs():
    assert min_cost_climbing_stairs([10, 15, 20]) == 15  # Minimum cost is 15 (10 -> 20)
    assert min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6  # Minimum cost is 6
    assert min_cost_climbing_stairs([0, 0, 0, 0]) == 0  # All costs are zero
    assert min_cost_climbing_stairs([10, 15]) == 10  # Only two steps, take the cheaper one
    assert min_cost_climbing_stairs([1, 2, 3, 4, 5]) == 6  # Minimum cost path is 1 -> 2 -> 4