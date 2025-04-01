import pytest
from src.leetcode.dp.coin_change import coin_change

def test_basic_case():
    """Test basic case with solution."""
    coins = [1, 2, 5]
    amount = 11
    assert coin_change(coins, amount) == 3  # 5 + 5 + 1
    
def test_no_solution():
    """Test when no solution exists."""
    coins = [2]
    amount = 3
    assert coin_change(coins, amount) == -1
    
def test_zero_amount():
    """Test with zero amount."""
    coins = [1, 2, 5]
    amount = 0
    assert coin_change(coins, amount) == 0
    
def test_single_coin():
    """Test when amount equals a single coin."""
    coins = [1, 2, 5]
    amount = 5
    assert coin_change(coins, amount) == 1
    
def test_larger_coins():
    """Test with coins larger than amount."""
    coins = [5, 10]
    amount = 3
    assert coin_change(coins, amount) == -1
    
def test_multiple_solutions():
    """Test case with multiple possible solutions."""
    coins = [1, 5, 10, 25]
    amount = 30
    assert coin_change(coins, amount) == 2  # 25 + 5
    
def test_repeated_coins():
    """Test with multiple instances of same coin value."""
    coins = [1, 1, 1]
    amount = 3
    assert coin_change(coins, amount) == 3
    
def test_non_minimal_coins():
    """Test that solution uses minimum number of coins."""
    coins = [1, 4, 5]
    amount = 8
    assert coin_change(coins, amount) == 2  # 4 + 4, not 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
    
def test_large_amount():
    """Test with a larger amount."""
    coins = [186, 419, 83, 408]
    amount = 6249
    assert coin_change(coins, amount) == 20  # Optimal solution should use 20 coins