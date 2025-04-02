# Test cases for LeetCode 40: Combination Sum II
from src.leetcode.backtracking.combination_sum_ii import combination_sum_ii

def test_combination_sum_ii():
    # Test case 1: Example input
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    expected = [
        [1, 1, 6],
        [1, 2, 5],
        [1, 7],
        [2, 6]
    ]
    result = combination_sum_ii(candidates, target)
    assert sorted(result) == sorted(expected), f"Test case 1 failed: {result}"

    # Test case 2: No solution
    candidates = [2, 4, 6]
    target = 1
    expected = []
    result = combination_sum_ii(candidates, target)
    assert result == expected, f"Test case 2 failed: {result}"

    # Test case 3: Single candidate used once
    candidates = [1]
    target = 1
    expected = [[1]]
    result = combination_sum_ii(candidates, target)
    assert result == expected, f"Test case 3 failed: {result}"

    print("All test cases passed for combination_sum_ii.")