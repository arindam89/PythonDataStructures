# Test cases for LeetCode 17: Letter Combinations of a Phone Number
from src.leetcode.backtracking.letter_combinations import letter_combinations

def test_letter_combinations():
    # Test case 1: Example input
    digits = "23"
    expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    result = letter_combinations(digits)
    assert sorted(result) == sorted(expected), f"Test case 1 failed: {result}"

    # Test case 2: Empty input
    digits = ""
    expected = []
    result = letter_combinations(digits)
    assert result == expected, f"Test case 2 failed: {result}"

    # Test case 3: Single digit
    digits = "2"
    expected = ["a", "b", "c"]
    result = letter_combinations(digits)
    assert sorted(result) == sorted(expected), f"Test case 3 failed: {result}"

    print("All test cases passed for letter_combinations.")