import pytest
from src.leetcode.string.group_anagrams import group_anagrams, group_anagrams_count

@pytest.mark.parametrize("func", [group_anagrams, group_anagrams_count])
def test_basic_case(func):
    """Test basic case with multiple anagram groups."""
    strs = ["eat","tea","tan","ate","nat","bat"]
    result = func(strs)
    # Sort each group and the groups themselves for comparison
    sorted_result = sorted([sorted(group) for group in result])
    expected = [["ate","eat","tea"], ["bat"], ["nat","tan"]]
    sorted_expected = sorted([sorted(group) for group in expected])
    assert sorted_result == sorted_expected
    
@pytest.mark.parametrize("func", [group_anagrams, group_anagrams_count])
def test_empty_input(func):
    """Test with empty input."""
    assert func([]) == []
    
@pytest.mark.parametrize("func", [group_anagrams, group_anagrams_count])
def test_no_anagrams(func):
    """Test when no strings are anagrams."""
    strs = ["cat", "dog", "pig"]
    result = func(strs)
    # Each string should be in its own group
    assert len(result) == 3
    assert all(len(group) == 1 for group in result)
    
@pytest.mark.parametrize("func", [group_anagrams, group_anagrams_count])
def test_all_anagrams(func):
    """Test when all strings are anagrams."""
    strs = ["eat", "tea", "ate"]
    result = func(strs)
    assert len(result) == 1
    assert len(result[0]) == 3
    assert sorted(result[0]) == sorted(strs)
    
@pytest.mark.parametrize("func", [group_anagrams, group_anagrams_count])
def test_empty_strings(func):
    """Test with empty strings."""
    strs = ["", "", ""]
    result = func(strs)
    assert len(result) == 1
    assert len(result[0]) == 3
    assert all(s == "" for s in result[0])
    
@pytest.mark.parametrize("func", [group_anagrams, group_anagrams_count])
def test_single_character(func):
    """Test with single character strings."""
    strs = ["a", "b", "a"]
    result = func(strs)
    sorted_result = sorted([sorted(group) for group in result])
    assert sorted_result == [["a", "a"], ["b"]]
    
@pytest.mark.parametrize("func", [group_anagrams, group_anagrams_count])
def test_case_sensitivity(func):
    """Test case sensitivity."""
    strs = ["Eat", "eat", "tea"]
    result = func(strs)
    # "Eat" should be in different group than "eat" and "tea"
    assert len(result) == 2
    
@pytest.mark.parametrize("func", [group_anagrams, group_anagrams_count])
def test_different_lengths(func):
    """Test strings of different lengths."""
    strs = ["eat", "tea", "team"]
    result = func(strs)
    # "team" should be in different group than "eat" and "tea"
    assert len(result) == 2
    
@pytest.mark.parametrize("func", [group_anagrams, group_anagrams_count])
def test_with_spaces(func):
    """Test strings with spaces."""
    strs = ["ab cd", "cd ab", "ef gh"]
    result = func(strs)
    sorted_result = sorted([sorted(group) for group in result])
    assert sorted_result == [["ab cd", "cd ab"], ["ef gh"]]
    
@pytest.mark.parametrize("func", [group_anagrams, group_anagrams_count])
def test_large_groups(func):
    """Test with larger anagram groups."""
    strs = ["post", "stop", "tops", "spot", "pots"]
    result = func(strs)
    assert len(result) == 1
    assert len(result[0]) == 5