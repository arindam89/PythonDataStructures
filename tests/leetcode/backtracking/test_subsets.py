# Test cases for LeetCode 78: Subsets
from src.leetcode.backtracking.subsets import subsets

def test_subsets():
    # Test case 1: Example input
    nums = [1, 2, 3]
    expected = [
        [], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]
    ]
    result = subsets(nums)
    assert sorted(result) == sorted(expected), f"Test case 1 failed: {result}"

    # Test case 2: Empty input
    nums = []
    expected = [[]]
    result = subsets(nums)
    assert result == expected, f"Test case 2 failed: {result}"

    # Test case 3: Single element
    nums = [1]
    expected = [[], [1]]
    result = subsets(nums)
    assert result == expected, f"Test case 3 failed: {result}"

    print("All test cases passed for subsets.")