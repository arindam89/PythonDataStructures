import pytest
from src.leetcode.dp.longest_palindromic_substring import longest_palindrome

def test_longest_palindrome():
    assert longest_palindrome("babad") in ["bab", "aba"]  # Both are valid palindromes
    assert longest_palindrome("cbbd") == "bb"  # Longest palindrome is "bb"
    assert longest_palindrome("a") == "a"  # Single character is a palindrome
    assert longest_palindrome("ac") in ["a", "c"]  # Either "a" or "c" is valid
    assert longest_palindrome("racecar") == "racecar"  # Entire string is a palindrome