# Test cases for LeetCode 90: Subsets II
from src.leetcode.backtracking.subsets_ii import subsets_with_dup

def test_subsets_with_dup():
    # Test case 1: Example input
    nums = [1, 2, 2]
    expected = [
        [], [1], [2], [1, 2], [2, 2], [1, 2, 2]
    ]
    result = subsets_with_dup(nums)
    assert sorted(result) == sorted(expected), f"Test case 1 failed: {result}"

    # Test case 2: No duplicates
    nums = [1, 2, 3]
    expected = [
        [], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]
    ]
    result = subsets_with_dup(nums)
    assert sorted(result) == sorted(expected), f"Test case 2 failed: {result}"

    # Test case 3: All duplicates
    nums = [2, 2, 2]
    expected = [
        [], [2], [2, 2], [2, 2, 2]
    ]
    result = subsets_with_dup(nums)
    assert sorted(result) == sorted(expected), f"Test case 3 failed: {result}"

    print("All test cases passed for subsets_with_dup.")