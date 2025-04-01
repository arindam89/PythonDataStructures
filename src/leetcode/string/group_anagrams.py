"""
LeetCode 49: Group Anagrams
https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer
in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word
or phrase, typically using all the original letters exactly once.

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Time Complexity: O(n * k * log k) where n is number of strings and k is max string length
Space Complexity: O(n * k)
"""

from typing import List
from collections import defaultdict

def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Group strings that are anagrams of each other.
    Uses sorted string as key to group anagrams efficiently.
    
    Args:
        strs: List of strings to group
        
    Returns:
        List of groups of anagrams
    """
    # Map sorted string to list of anagrams
    groups = defaultdict(list)
    
    for s in strs:
        # Sort characters to get canonical form
        sorted_str = ''.join(sorted(s))
        groups[sorted_str].append(s)
        
    # Return list of groups
    return list(groups.values())
    
def group_anagrams_count(strs: List[str]) -> List[List[str]]:
    """
    Alternative implementation using character count as key.
    More efficient for strings with known character set (e.g., lowercase letters).
    Time Complexity: O(n * k) where n is number of strings and k is max string length.
    
    Args:
        strs: List of strings to group
        
    Returns:
        List of groups of anagrams
    """
    groups = defaultdict(list)
    
    for s in strs:
        # Create count array for lowercase letters
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
            
        # Convert count array to tuple to use as dictionary key
        groups[tuple(count)].append(s)
        
    return list(groups.values())