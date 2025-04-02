import pytest
from src.leetcode.dp.word_break import word_break

def test_word_break():
    assert word_break("leetcode", ["leet", "code"]) == True  # "leet" + "code"
    assert word_break("applepenapple", ["apple", "pen"]) == True  # "apple" + "pen" + "apple"
    assert word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False  # Cannot segment
    assert word_break("", ["a", "b"]) == True  # Empty string can always be segmented
    assert word_break("a", ["b"]) == False  # "a" is not in the dictionary