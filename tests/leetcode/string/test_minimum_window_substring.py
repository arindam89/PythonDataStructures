import pytest
from src.leetcode.string.minimum_window_substring import min_window

def test_basic_case():
    """Test basic case with solution."""
    s = "ADOBECODEBANC"
    t = "ABC"
    assert min_window(s, t) == "BANC"
    
def test_no_solution():
    """Test when no solution exists."""
    s = "ADOBECODEBANC"
    t = "XYZ"
    assert min_window(s, t) == ""
    
def test_empty_strings():
    """Test with empty strings."""
    assert min_window("", "") == ""
    assert min_window("ABC", "") == ""
    assert min_window("", "ABC") == ""
    
def test_single_char():
    """Test with single character strings."""
    s = "A"
    t = "A"
    assert min_window(s, t) == "A"
    
def test_duplicate_chars():
    """Test with duplicate characters in target."""
    s = "ADOBECODEBANCAA"
    t = "AA"
    assert min_window(s, t) == "AA"
    
def test_entire_string():
    """Test when minimum window is entire string."""
    s = "ABC"
    t = "CBA"
    assert min_window(s, t) == "ABC"
    
def test_substring_at_start():
    """Test when minimum window is at start of string."""
    s = "ABCDEFG"
    t = "ABC"
    assert min_window(s, t) == "ABC"
    
def test_substring_at_end():
    """Test when minimum window is at end of string."""
    s = "DEFGABC"
    t = "ABC"
    assert min_window(s, t) == "ABC"
    
def test_complex_case():
    """Test with more complex pattern."""
    s = "aaaaaaaaaaaabbbcccc"
    t = "abc"
    assert min_window(s, t) == "abbc"
    
def test_overlapping_chars():
    """Test with overlapping required characters."""
    s = "ABBCBECODEBANC"
    t = "ABC"
    assert min_window(s, t) == "BANC"