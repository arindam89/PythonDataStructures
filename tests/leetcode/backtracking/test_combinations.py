import pytest
from src.leetcode.backtracking.combinations import combine

def test_basic_combination():
    """Test basic case with n=4, k=2."""
    n, k = 4, 2
    result = combine(n, k)
    expected = [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]
    assert len(result) == len(expected)
    assert all(sorted(combo) in [sorted(exp) for exp in expected] for combo in result)
    
def test_single_element():
    """Test when k=1."""
    n, k = 3, 1
    result = combine(n, k)
    expected = [[1], [2], [3]]
    assert sorted(result) == sorted(expected)
    
def test_all_elements():
    """Test when k=n."""
    n = 3
    result = combine(n, n)
    expected = [[1, 2, 3]]
    assert sorted(result) == sorted(expected)
    
def test_empty_result():
    """Test when k > n (should return empty list)."""
    n, k = 3, 4
    assert combine(n, k) == []
    
def test_large_combination():
    """Test with larger n and k."""
    n, k = 5, 3
    result = combine(n, k)
    # Number of combinations should be C(5,3) = 10
    assert len(result) == 10
    # Each combination should have exactly k elements
    assert all(len(combo) == k for combo in result)
    # Elements should be in range [1, n]
    assert all(1 <= x <= n for combo in result for x in combo)
    # Combinations should be unique
    assert len(set(tuple(sorted(c)) for c in result)) == len(result)