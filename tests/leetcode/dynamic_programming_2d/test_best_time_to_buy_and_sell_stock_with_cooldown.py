import pytest
from src.leetcode.dynamic_programming_2d.best_time_to_buy_and_sell_stock_with_cooldown import max_profit

def test_max_profit():
    # Test case 1: Example from problem statement
    assert max_profit([1, 2, 3, 0, 2]) == 3

    # Test case 2: No transactions possible
    assert max_profit([1]) == 0

    # Test case 3: Prices are decreasing
    assert max_profit([5, 4, 3, 2, 1]) == 0

    # Test case 4: Prices are increasing
    assert max_profit([1, 2, 3, 4, 5]) == 4

    # Test case 5: Random prices
    assert max_profit([3, 2, 6, 5, 0, 3]) == 7