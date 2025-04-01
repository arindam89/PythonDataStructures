import pytest
from src.leetcode.arrays.two_sum import two_sum

def test_two_sum_basic():
    """Test basic case with positive integers."""
    nums = [2, 7, 11, 15]
    target = 9
    assert sorted(two_sum(nums, target)) == [0, 1]
    
def test_two_sum_negative():
    """Test with negative numbers."""
    nums = [3, -2, 4, -1]
    target = 2
    assert sorted(two_sum(nums, target)) == [0, 3]
    
def test_two_sum_duplicates():
    """Test with duplicate numbers."""
    nums = [3, 3]
    target = 6
    assert sorted(two_sum(nums, target)) == [0, 1]
    
def test_two_sum_no_solution():
    """Test when no solution exists."""
    nums = [2, 7, 11, 15]
    target = 100
    assert two_sum(nums, target) == []
    
def test_two_sum_zero():
    """Test with zero and negative numbers."""
    nums = [-1, 0, 1, 2]
    target = 0
    assert sorted(two_sum(nums, target)) == [0, 2]