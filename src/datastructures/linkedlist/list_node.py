"""Node class for LinkedList implementation."""

from typing import Optional, TypeVar, Generic

T = TypeVar('T')

class ListNode(Generic[T]):
    """
    A node in a linked list.
    
    Attributes:
        val: The value stored in the node
        next: Reference to the next node, or None if this is the last node
    """
    
    def __init__(self, val: T, next: Optional['ListNode[T]'] = None):
        """
        Initialize a new node.
        
        Args:
            val: The value to store in the node
            next: Reference to the next node (optional)
        """
        self.val = val
        self.next = next