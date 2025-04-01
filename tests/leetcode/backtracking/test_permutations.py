import pytest
from src.leetcode.backtracking.permutations import permute

def test_basic_permutation():
    """Test basic case with three numbers."""
    nums = [1, 2, 3]
    result = permute(nums)
    expected = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
    assert len(result) == len(expected)
    assert all(perm in expected for perm in result)
    assert all(perm in result for perm in expected)
    
def test_single_element():
    """Test with single element."""
    nums = [1]
    result = permute(nums)
    assert result == [[1]]
    
def test_two_elements():
    """Test with two elements."""
    nums = [1, 2]
    result = permute(nums)
    expected = [[1, 2], [2, 1]]
    assert sorted(result) == sorted(expected)
    
def test_negative_numbers():
    """Test with negative numbers."""
    nums = [-1, 0, 1]
    result = permute(nums)
    # Should have 6 permutations
    assert len(result) == 6
    # Each permutation should contain all numbers
    assert all(sorted(perm) == [-1, 0, 1] for perm in result)
    # All permutations should be unique
    assert len(set(tuple(p) for p in result)) == 6
    
def test_empty_list():
    """Test with empty list."""
    nums = []
    result = permute(nums)
    assert result == [[]]  # One empty permutation

def test_larger_input():
    """Test with more numbers."""
    nums = [1, 2, 3, 4]
    result = permute(nums)
    # Should have 24 permutations (4!)
    assert len(result) == 24
    # Each permutation should have all numbers
    assert all(sorted(perm) == sorted(nums) for perm in result)
    # All permutations should be unique
    assert len(set(tuple(p) for p in result)) == 24