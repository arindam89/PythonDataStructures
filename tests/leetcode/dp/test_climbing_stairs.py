import pytest
from src.leetcode.dp.climbing_stairs import climb_stairs

def test_climb_stairs():
    assert climb_stairs(1) == 1  # Only one way to climb 1 step
    assert climb_stairs(2) == 2  # Two ways: (1+1) or (2)
    assert climb_stairs(3) == 3  # Three ways: (1+1+1), (1+2), (2+1)
    assert climb_stairs(4) == 5  # Five ways: (1+1+1+1), (1+1+2), (1+2+1), (2+1+1), (2+2)
    assert climb_stairs(5) == 8  # Eight ways: Fibonacci sequence