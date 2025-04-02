import pytest
from src.leetcode.dp.palindromic_substrings import count_substrings

def test_count_substrings():
    assert count_substrings("abc") == 3  # Each character is a palindrome
    assert count_substrings("aaa") == 6  # "a", "a", "a", "aa", "aa", "aaa"
    assert count_substrings("racecar") == 10  # Multiple palindromes including "racecar"
    assert count_substrings("") == 0  # Empty string has no palindromes
    assert count_substrings("abccba") == 9  # Multiple palindromes including "abccba"