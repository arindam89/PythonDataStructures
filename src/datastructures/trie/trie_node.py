"""Node class for Trie implementation."""

from typing import Dict, Optional

class TrieNode:
    """
    A node in a Trie.
    Each node contains a dictionary of children nodes and a flag indicating
    if it represents the end of a word.
    """
    
    def __init__(self):
        """Initialize an empty trie node."""
        self.children: Dict[str, 'TrieNode'] = {}
        self.is_end_of_word: bool = False