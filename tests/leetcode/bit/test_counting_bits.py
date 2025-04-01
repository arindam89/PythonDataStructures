import pytest
from src.leetcode.bit.counting_bits import count_bits, count_bits_pattern

@pytest.mark.parametrize("func", [count_bits, count_bits_pattern])
def test_basic_case(func):
    """Test basic case from problem description."""
    assert func(5) == [0, 1, 1, 2, 1, 2]

@pytest.mark.parametrize("func", [count_bits, count_bits_pattern])
def test_zero(func):
    """Test with n = 0."""
    assert func(0) == [0]

@pytest.mark.parametrize("func", [count_bits, count_bits_pattern])
def test_powers_of_two(func):
    """Test with numbers that are powers of 2."""
    assert func(4) == [0, 1, 1, 2, 1]
    assert func(8) == [0, 1, 1, 2, 1, 2, 2, 3, 1]

@pytest.mark.parametrize("func", [count_bits, count_bits_pattern])
def test_sequence_patterns(func):
    """Test sequence patterns in larger numbers."""
    result = func(15)
    # Verify pattern for 8-15 follows pattern of 0-7 plus 1
    base = result[:8]  # First 8 numbers
    for i in range(8):
        assert result[i + 8] == base[i] + 1

@pytest.mark.parametrize("func", [count_bits, count_bits_pattern])
def test_specific_numbers(func):
    """Test specific numbers with known bit counts."""
    result = func(16)
    assert result[7] == 3   # 7 is 111 in binary
    assert result[15] == 4  # 15 is 1111 in binary
    assert result[16] == 1  # 16 is 10000 in binary

@pytest.mark.parametrize("func", [count_bits, count_bits_pattern])
def test_consecutive_numbers(func):
    """Test consecutive numbers have expected relationships."""
    result = func(10)
    # 10 (1010) should have same count as 8 (1000) plus 1
    assert result[10] == result[8] + 1
    # 9 (1001) should have same count as 8 (1000) plus 1
    assert result[9] == result[8] + 1

@pytest.mark.parametrize("func", [count_bits, count_bits_pattern])
def test_larger_number(func):
    """Test with a larger number."""
    result = func(20)
    # Verify length
    assert len(result) == 21
    # Verify some specific values
    assert result[20] == 2  # 20 is 10100 in binary
    assert result[19] == 3  # 19 is 10011 in binary

@pytest.mark.parametrize("func", [count_bits, count_bits_pattern])
def test_all_ones(func):
    """Test numbers that are all ones in binary."""
    result = func(15)
    assert result[3] == 2   # 3 is 11
    assert result[7] == 3   # 7 is 111
    assert result[15] == 4  # 15 is 1111

@pytest.mark.parametrize("func", [count_bits, count_bits_pattern])
def test_alternating_bits(func):
    """Test numbers with alternating bits."""
    result = func(10)
    assert result[5] == 2   # 5 is 101
    assert result[10] == 2  # 10 is 1010

@pytest.mark.parametrize("func", [count_bits, count_bits_pattern])
def test_power_of_two_minus_one(func):
    """Test numbers that are one less than power of 2."""
    result = func(16)
    assert result[3] == 2   # 3 is 2^2 - 1
    assert result[7] == 3   # 7 is 2^3 - 1
    assert result[15] == 4  # 15 is 2^4 - 1