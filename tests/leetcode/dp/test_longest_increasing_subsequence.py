import pytest
from src.leetcode.dp.longest_increasing_subsequence import length_of_lis, length_of_lis_dp

@pytest.mark.parametrize("func", [length_of_lis, length_of_lis_dp])
def test_basic_sequence(func):
    """Test basic increasing sequence."""
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    assert func(nums) == 4  # [2, 5, 7, 101] or [2, 3, 7, 101]

@pytest.mark.parametrize("func", [length_of_lis, length_of_lis_dp])
def test_strictly_increasing(func):
    """Test with strictly increasing sequence."""
    nums = [1, 2, 3, 4, 5]
    assert func(nums) == 5

@pytest.mark.parametrize("func", [length_of_lis, length_of_lis_dp])
def test_strictly_decreasing(func):
    """Test with strictly decreasing sequence."""
    nums = [5, 4, 3, 2, 1]
    assert func(nums) == 1

@pytest.mark.parametrize("func", [length_of_lis, length_of_lis_dp])
def test_all_same(func):
    """Test with all same numbers."""
    nums = [1, 1, 1, 1]
    assert func(nums) == 1

@pytest.mark.parametrize("func", [length_of_lis, length_of_lis_dp])
def test_empty_sequence(func):
    """Test with empty sequence."""
    nums = []
    assert func(nums) == 0

@pytest.mark.parametrize("func", [length_of_lis, length_of_lis_dp])
def test_single_element(func):
    """Test with single element."""
    nums = [42]
    assert func(nums) == 1

@pytest.mark.parametrize("func", [length_of_lis, length_of_lis_dp])
def test_multiple_increasing_subsequences(func):
    """Test with multiple possible increasing subsequences."""
    nums = [3, 10, 2, 1, 20]
    assert func(nums) == 3  # [3, 10, 20] or [2, 3, 20] or [1, 3, 20]

@pytest.mark.parametrize("func", [length_of_lis, length_of_lis_dp])
def test_negative_numbers(func):
    """Test with negative numbers."""
    nums = [-2, -1, -3, 0, 1]
    assert func(nums) == 4  # [-2, -1, 0, 1]

@pytest.mark.parametrize("func", [length_of_lis, length_of_lis_dp])
def test_duplicate_numbers(func):
    """Test with duplicate numbers."""
    nums = [1, 2, 2, 3]
    assert func(nums) == 3  # [1, 2, 3]