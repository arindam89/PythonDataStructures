import pytest
from src.leetcode.string.longest_palindromic_substring import (
    longest_palindrome,
    longest_palindrome_dp
)

@pytest.mark.parametrize("func", [longest_palindrome, longest_palindrome_dp])
def test_basic_case(func):
    """Test basic case with multiple possible answers."""
    s = "babad"
    result = func(s)
    assert result in ["bab", "aba"]
    
@pytest.mark.parametrize("func", [longest_palindrome, longest_palindrome_dp])
def test_even_length_palindrome(func):
    """Test with even length palindrome."""
    s = "cbbd"
    assert func(s) == "bb"
    
@pytest.mark.parametrize("func", [longest_palindrome, longest_palindrome_dp])
def test_entire_string_palindrome(func):
    """Test when entire string is palindrome."""
    s = "racecar"
    assert func(s) == "racecar"
    
@pytest.mark.parametrize("func", [longest_palindrome, longest_palindrome_dp])
def test_single_char(func):
    """Test with single character string."""
    s = "a"
    assert func(s) == "a"
    
@pytest.mark.parametrize("func", [longest_palindrome, longest_palindrome_dp])
def test_empty_string(func):
    """Test with empty string."""
    s = ""
    assert func(s) == ""
    
@pytest.mark.parametrize("func", [longest_palindrome, longest_palindrome_dp])
def test_two_char_same(func):
    """Test with two same characters."""
    s = "aa"
    assert func(s) == "aa"
    
@pytest.mark.parametrize("func", [longest_palindrome, longest_palindrome_dp])
def test_two_char_different(func):
    """Test with two different characters."""
    s = "ab"
    assert func(s) in ["a", "b"]
    
@pytest.mark.parametrize("func", [longest_palindrome, longest_palindrome_dp])
def test_multiple_palindromes(func):
    """Test string with multiple palindromes of same length."""
    s = "aaa111aaa222aaa"
    result = func(s)
    assert len(result) == 7
    assert result in ["aaa111a", "111aaa2", "2aaa222", "222aaa"]
    
@pytest.mark.parametrize("func", [longest_palindrome, longest_palindrome_dp])
def test_complex_string(func):
    """Test with more complex string."""
    s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendure"
    result = func(s)
    assert result == "ranynar"  # Length 7 palindrome
    
@pytest.mark.parametrize("func", [longest_palindrome, longest_palindrome_dp])
def test_repeating_chars(func):
    """Test with repeating characters."""
    s = "bbbbbb"
    assert func(s) == "bbbbbb"