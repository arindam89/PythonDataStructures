import pytest
from src.leetcode.arrays.max_sum_three_subarrays import max_sum_of_three_subarrays

def test_basic_case():
    """Test basic case from problem description."""
    nums = [1, 2, 1, 2, 6, 7, 5, 1]
    k = 2
    assert max_sum_of_three_subarrays(nums, k) == [0, 3, 5]

def test_empty_array():
    """Test with empty array."""
    nums = []
    k = 2
    assert max_sum_of_three_subarrays(nums, k) == []

def test_minimum_length():
    """Test with array of minimum required length."""
    nums = [1, 2, 3, 4, 5, 6]
    k = 2
    assert max_sum_of_three_subarrays(nums, k) == [0, 2, 4]

def test_equal_values():
    """Test with array of equal values."""
    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    k = 2
    # Should return lexicographically smallest valid result
    assert max_sum_of_three_subarrays(nums, k) == [0, 3, 6]

def test_negative_values():
    """Test with negative values."""
    nums = [-1, -2, 5, 6, 2, 4, -7, 8, 9]
    k = 2
    assert max_sum_of_three_subarrays(nums, k) == [2, 4, 7]

def test_large_k():
    """Test with larger k value."""
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    k = 3
    assert max_sum_of_three_subarrays(nums, k) == [0, 4, 8]

def test_alternating_values():
    """Test with alternating high and low values."""
    nums = [1, 10, 1, 10, 1, 10, 1, 10]
    k = 2
    assert max_sum_of_three_subarrays(nums, k) == [1, 3, 5]

def test_descending_values():
    """Test with descending values."""
    nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    k = 2
    assert max_sum_of_three_subarrays(nums, k) == [0, 2, 4]

def test_sparse_array():
    """Test with sparse array (many zeros)."""
    nums = [0, 0, 5, 0, 0, 5, 0, 0, 5, 0, 0]
    k = 2
    result = max_sum_of_three_subarrays(nums, k)
    # Verify each window contains at least one non-zero value
    assert sum(nums[result[0]:result[0]+k]) > 0
    assert sum(nums[result[1]:result[1]+k]) > 0
    assert sum(nums[result[2]:result[2]+k]) > 0

def test_lexicographically_smallest():
    """Test that function returns lexicographically smallest result."""
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    k = 2
    result = max_sum_of_three_subarrays(nums, k)
    # For equal sums, should choose earliest possible positions
    assert result == [0, 2, 4]