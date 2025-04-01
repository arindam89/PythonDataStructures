"""
LeetCode 146: LRU Cache
https://leetcode.com/problems/lru-cache/

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity): Initialize the LRU cache with positive size capacity.
- int get(int key): Return the value of the key if it exists, otherwise return -1.
- void put(int key, int value): Update the value of the key if it exists. 
  Otherwise, add the key-value pair to the cache. If the number of keys exceeds
  the capacity, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Time Complexity: O(1) for all operations
Space Complexity: O(capacity)
"""

from typing import Dict, Optional, TypeVar, Generic
from .lru_cache_node import LRUNode

T = TypeVar('T')

class LRUCache(Generic[T]):
    """
    LRU Cache implementation using a hash map and doubly linked list.
    The hash map provides O(1) access to cache items, while the doubly
    linked list maintains the order of items for LRU eviction.
    """
    
    def __init__(self, capacity: int):
        """
        Initialize LRU cache with given capacity.
        
        Args:
            capacity: Maximum number of items the cache can hold
        """
        self.capacity = capacity
        self.cache: Dict[int, LRUNode[T]] = {}
        
        # Dummy head and tail nodes to simplify list operations
        self.head = LRUNode[T]()
        self.tail = LRUNode[T]()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _remove_node(self, node: LRUNode[T]) -> None:
        """Remove a node from the doubly linked list."""
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        
    def _add_node(self, node: LRUNode[T]) -> None:
        """Add node right after head (most recently used position)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        
    def _move_to_front(self, node: LRUNode[T]) -> None:
        """Move an existing node to the front (most recently used)."""
        self._remove_node(node)
        self._add_node(node)
        
    def get(self, key: int) -> Optional[T]:
        """
        Get the value associated with the key if it exists.
        Updates the item to be most recently used.
        
        Args:
            key: The key to look up
            
        Returns:
            The value if found, None otherwise
        """
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)
            return node.val
        return None
        
    def put(self, key: int, value: T) -> None:
        """
        Add or update a key-value pair in the cache.
        If key exists, update its value and move to front.
        If key doesn't exist, add it and evict LRU item if necessary.
        
        Args:
            key: The key to add or update
            value: The value to store
        """
        if key in self.cache:
            # Update existing key's value and move to front
            node = self.cache[key]
            node.val = value
            self._move_to_front(node)
        else:
            # Add new key-value pair
            new_node = LRUNode(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
            
            # If over capacity, remove least recently used item
            if len(self.cache) > self.capacity:
                lru = self.tail.prev
                self._remove_node(lru)
                del self.cache[lru.key]
                
    def clear(self) -> None:
        """Remove all items from the cache."""
        self.cache.clear()
        self.head.next = self.tail
        self.tail.prev = self.head