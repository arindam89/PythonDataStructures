import pytest
from src.leetcode.bit.single_number_iii import single_number_iii, single_number_iii_hash

@pytest.mark.parametrize("func", [single_number_iii, single_number_iii_hash])
def test_basic_case(func):
    """Test basic case from problem description."""
    nums = [1, 2, 1, 3, 2, 5]
    result = func(nums)
    assert sorted(result) == [3, 5]

@pytest.mark.parametrize("func", [single_number_iii, single_number_iii_hash])
def test_consecutive_numbers(func):
    """Test with consecutive numbers."""
    nums = [1, 2, 3, 4, 1, 2]
    result = func(nums)
    assert sorted(result) == [3, 4]

@pytest.mark.parametrize("func", [single_number_iii, single_number_iii_hash])
def test_with_zero(func):
    """Test with zero as one of the numbers."""
    nums = [0, 1, 2, 1, 2, 3]
    result = func(nums)
    assert sorted(result) == [0, 3]

@pytest.mark.parametrize("func", [single_number_iii, single_number_iii_hash])
def test_negative_numbers(func):
    """Test with negative numbers."""
    nums = [-1, 2, -1, 3, 2, 4]
    result = func(nums)
    assert sorted(result) == [3, 4]

@pytest.mark.parametrize("func", [single_number_iii, single_number_iii_hash])
def test_large_numbers(func):
    """Test with large numbers."""
    nums = [1000000, 2, 1000000, 3, 2, 5]
    result = func(nums)
    assert sorted(result) == [3, 5]

@pytest.mark.parametrize("func", [single_number_iii, single_number_iii_hash])
def test_power_of_two(func):
    """Test with powers of two."""
    nums = [2, 4, 8, 2, 4, 16]
    result = func(nums)
    assert sorted(result) == [8, 16]

@pytest.mark.parametrize("func", [single_number_iii, single_number_iii_hash])
def test_same_bit_patterns(func):
    """Test with numbers having similar bit patterns."""
    nums = [3, 5, 3, 7, 5, 9]  # 3=11, 5=101, 7=111, 9=1001
    result = func(nums)
    assert sorted(result) == [7, 9]

@pytest.mark.parametrize("func", [single_number_iii, single_number_iii_hash])
def test_minimal_array(func):
    """Test with minimal possible array length."""
    nums = [1, 2]
    result = func(nums)
    assert sorted(result) == [1, 2]

@pytest.mark.parametrize("func", [single_number_iii, single_number_iii_hash])
def test_alternating_pattern(func):
    """Test with alternating repeated and unique numbers."""
    nums = [1, 3, 1, 5, 2, 2]
    result = func(nums)
    assert sorted(result) == [3, 5]

@pytest.mark.parametrize("func", [single_number_iii, single_number_iii_hash])
def test_mixed_signs(func):
    """Test with mix of positive and negative numbers."""
    nums = [-2, 1, -2, 3, 1, -5]
    result = func(nums)
    assert sorted(result) == [-5, 3]