# Test cases for LeetCode 39: Combination Sum
from src.leetcode.backtracking.combination_sum import combination_sum

def test_combination_sum():
    # Test case 1: Example input
    candidates = [2, 3, 6, 7]
    target = 7
    expected = [[2, 2, 3], [7]]
    result = combination_sum(candidates, target)
    assert sorted(result) == sorted(expected), f"Test case 1 failed: {result}"

    # Test case 2: No solution
    candidates = [2, 4]
    target = 1
    expected = []
    result = combination_sum(candidates, target)
    assert result == expected, f"Test case 2 failed: {result}"

    # Test case 3: Single candidate
    candidates = [1]
    target = 2
    expected = [[1, 1]]
    result = combination_sum(candidates, target)
    assert result == expected, f"Test case 3 failed: {result}"

    print("All test cases passed for combination_sum.")