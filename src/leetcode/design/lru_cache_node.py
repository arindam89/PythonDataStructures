"""Node class for LRU Cache implementation."""

from typing import Optional, TypeVar, Generic

T = TypeVar('T')

class LRUNode(Generic[T]):
    """
    A node in the LRU Cache's doubly linked list.
    Maintains references to previous and next nodes, and stores key-value pairs.
    """
    
    def __init__(self, key: int = 0, val: T = None):
        """
        Initialize a new LRU node.
        
        Args:
            key: The key associated with the value
            val: The value to store
        """
        self.key = key
        self.val = val
        self.prev: Optional[LRUNode] = None
        self.next: Optional[LRUNode] = None