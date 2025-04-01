"""
Implementation of a Trie (prefix tree) data structure.
A trie is an efficient information retrieval data structure,
commonly used for storing and searching strings.
"""

from typing import List, Optional
from .trie_node import TrieNode

class Trie:
    """
    Trie implementation.
    
    Time Complexity:
    - Insert: O(m) where m is the length of the word
    - Search: O(m) where m is the length of the word
    - StartsWith: O(p) where p is the length of the prefix
    
    Space Complexity: O(ALPHABET_SIZE * N * M) where:
    - ALPHABET_SIZE is the number of possible characters (26 for English lowercase)
    - N is the number of words
    - M is the average length of words
    """
    
    def __init__(self):
        """Initialize an empty trie."""
        self.root = TrieNode()
        self._size = 0
        
    def insert(self, word: str) -> None:
        """
        Insert a word into the trie.
        Time Complexity: O(m) where m is the length of the word
        
        Args:
            word: The word to insert
        """
        current = self.root
        
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
            
        if not current.is_end_of_word:
            current.is_end_of_word = True
            self._size += 1
            
    def search(self, word: str) -> bool:
        """
        Search for a word in the trie.
        Time Complexity: O(m) where m is the length of the word
        
        Args:
            word: The word to search for
            
        Returns:
            True if the word exists in the trie, False otherwise
        """
        node = self._find_node(word)
        return node is not None and node.is_end_of_word
        
    def starts_with(self, prefix: str) -> bool:
        """
        Check if there is any word in the trie that starts with the given prefix.
        Time Complexity: O(p) where p is the length of the prefix
        
        Args:
            prefix: The prefix to search for
            
        Returns:
            True if any word starts with the prefix, False otherwise
        """
        return self._find_node(prefix) is not None
        
    def _find_node(self, prefix: str) -> Optional[TrieNode]:
        """Helper method to find the node corresponding to a prefix."""
        current = self.root
        
        for char in prefix:
            if char not in current.children:
                return None
            current = current.children[char]
            
        return current
        
    def remove(self, word: str) -> bool:
        """
        Remove a word from the trie.
        Time Complexity: O(m) where m is the length of the word
        
        Args:
            word: The word to remove
            
        Returns:
            True if the word was found and removed, False otherwise
        """
        def _remove_helper(node: TrieNode, word: str, depth: int) -> bool:
            if depth == len(word):
                # Word found, but it's not marked as end of word
                if not node.is_end_of_word:
                    return False
                    
                # Remove the word mark and decrease size
                node.is_end_of_word = False
                self._size -= 1
                
                # Return whether this node can be deleted
                return not node.children
                
            char = word[depth]
            if char not in node.children:
                return False
                
            should_delete_child = _remove_helper(node.children[char], word, depth + 1)
            
            if should_delete_child:
                del node.children[char]
                # Return whether this node can be deleted
                return not node.is_end_of_word and not node.children
                
            return False
            
        return _remove_helper(self.root, word, 0)
        
    def get_words_with_prefix(self, prefix: str) -> List[str]:
        """
        Find all words that start with the given prefix.
        Time Complexity: O(p + n) where:
        - p is the length of the prefix
        - n is the number of nodes in the subtrie rooted at the end of the prefix
        
        Args:
            prefix: The prefix to search for
            
        Returns:
            A list of all words that start with the prefix
        """
        node = self._find_node(prefix)
        if not node:
            return []
            
        result = []
        
        def dfs(node: TrieNode, current_word: str):
            if node.is_end_of_word:
                result.append(current_word)
                
            for char, child in node.children.items():
                dfs(child, current_word + char)
                
        dfs(node, prefix)
        return result
        
    def get_all_words(self) -> List[str]:
        """
        Get all words stored in the trie.
        Time Complexity: O(n) where n is the number of nodes in the trie
        
        Returns:
            A list of all words in the trie
        """
        return self.get_words_with_prefix("")
        
    def clear(self) -> None:
        """Remove all words from the trie."""
        self.root = TrieNode()
        self._size = 0
        
    def size(self) -> int:
        """
        Get the number of words in the trie.
        
        Returns:
            The number of words stored in the trie
        """
        return self._size
        
    def is_empty(self) -> bool:
        """
        Check if the trie is empty.
        
        Returns:
            True if the trie contains no words, False otherwise
        """
        return self._size == 0