import pytest
from src.leetcode.dynamic_programming_2d.interleaving_string import is_interleave

def test_is_interleave():
    # Test case 1: Example from problem statement
    assert is_interleave("aab", "axy", "aaxaby") == True

    # Test case 2: Not an interleaving
    assert is_interleave("aab", "axy", "abaaxy") == False

    # Test case 3: Empty strings
    assert is_interleave("", "", "") == True

    # Test case 4: One string empty
    assert is_interleave("abc", "", "abc") == True
    assert is_interleave("", "def", "def") == True

    # Test case 5: Unequal lengths
    assert is_interleave("abc", "def", "abdecf") == False