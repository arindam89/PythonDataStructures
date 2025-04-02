# Test cases for LeetCode 131: Palindrome Partitioning
from src.leetcode.backtracking.palindrome_partitioning import partition

def test_partition():
    # Test case 1: Example input
    s = "aab"
    expected = [["a", "a", "b"], ["aa", "b"]]
    result = partition(s)
    assert sorted(result) == sorted(expected), f"Test case 1 failed: {result}"

    # Test case 2: Single character
    s = "a"
    expected = [["a"]]
    result = partition(s)
    assert result == expected, f"Test case 2 failed: {result}"

    # Test case 3: All characters are the same
    s = "aaa"
    expected = [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]
    result = partition(s)
    assert sorted(result) == sorted(expected), f"Test case 3 failed: {result}"

    # Test case 4: No palindrome partitions
    s = "abc"
    expected = [["a", "b", "c"]]
    result = partition(s)
    assert result == expected, f"Test case 4 failed: {result}"

    print("All test cases passed for partition.")