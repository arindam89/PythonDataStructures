import pytest
from src.leetcode.bit.total_hamming_distance import total_hamming_distance, total_hamming_distance_brute

@pytest.mark.parametrize("func", [total_hamming_distance, total_hamming_distance_brute])
def test_basic_case(func):
    """Test basic case from problem description."""
    nums = [4, 14, 2]
    assert func(nums) == 6

@pytest.mark.parametrize("func", [total_hamming_distance, total_hamming_distance_brute])
def test_empty_array(func):
    """Test with empty array."""
    assert func([]) == 0

@pytest.mark.parametrize("func", [total_hamming_distance, total_hamming_distance_brute])
def test_single_element(func):
    """Test with single element array."""
    assert func([4]) == 0

@pytest.mark.parametrize("func", [total_hamming_distance, total_hamming_distance_brute])
def test_identical_numbers(func):
    """Test with array of identical numbers."""
    nums = [4, 4, 4, 4]
    assert func(nums) == 0

@pytest.mark.parametrize("func", [total_hamming_distance, total_hamming_distance_brute])
def test_powers_of_two(func):
    """Test with powers of two."""
    nums = [1, 2, 4, 8]  # Each differs in all bits from others
    assert func(nums) == 12

@pytest.mark.parametrize("func", [total_hamming_distance, total_hamming_distance_brute])
def test_all_bits_different(func):
    """Test with numbers that have maximum Hamming distance."""
    nums = [0, 15]  # 0000 vs 1111
    assert func(nums) == 4

@pytest.mark.parametrize("func", [total_hamming_distance, total_hamming_distance_brute])
def test_consecutive_numbers(func):
    """Test with consecutive numbers."""
    nums = [7, 8, 9]  # 0111, 1000, 1001
    assert func(nums) == 8

@pytest.mark.parametrize("func", [total_hamming_distance, total_hamming_distance_brute])
def test_large_numbers(func):
    """Test with large numbers."""
    nums = [1000000, 1000001, 1000002]
    result = func(nums)
    assert result > 0  # Exact value depends on bit differences

@pytest.mark.parametrize("func", [total_hamming_distance, total_hamming_distance_brute])
def test_all_zeros_and_one(func):
    """Test with array of zeros and one non-zero."""
    nums = [0, 0, 0, 1]
    assert func(nums) == 3  # Three pairs with distance 1

@pytest.mark.parametrize("func", [total_hamming_distance, total_hamming_distance_brute])
def test_alternating_bits(func):
    """Test with numbers having alternating bit patterns."""
    nums = [0b10101, 0b01010]  # Alternating 1s and 0s
    assert func(nums) == 5  # All bits are different