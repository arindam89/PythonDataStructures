# Test cases for LeetCode 79: Word Search
from src.leetcode.backtracking.word_search import exist

def test_exist():
    # Test case 1: Example input
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCCED"
    assert exist(board, word), "Test case 1 failed"

    # Test case 2: Word not in board
    word = "SEE"
    assert exist(board, word), "Test case 2 failed"

    # Test case 3: Word not possible
    word = "ABCB"
    assert not exist(board, word), "Test case 3 failed"

    # Test case 4: Single letter match
    board = [['A']]
    word = "A"
    assert exist(board, word), "Test case 4 failed"

    # Test case 5: Single letter no match
    word = "B"
    assert not exist(board, word), "Test case 5 failed"

    print("All test cases passed for exist.")