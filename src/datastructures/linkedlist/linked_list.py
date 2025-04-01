"""
Implementation of a singly linked list data structure.
"""

from typing import Optional, List, TypeVar, Generic, Iterator
from .list_node import ListNode

T = TypeVar('T')

class LinkedList(Generic[T]):
    """
    Singly linked list implementation.
    
    Time Complexity:
    - Access: O(n)
    - Search: O(n)
    - Insert at beginning: O(1)
    - Insert at end: O(1) with tail pointer, O(n) without
    - Delete at beginning: O(1)
    - Delete at end: O(n)
    - Delete at position: O(n)
    
    Space Complexity: O(n)
    """
    
    def __init__(self):
        """Initialize an empty linked list."""
        self.head: Optional[ListNode[T]] = None
        self.tail: Optional[ListNode[T]] = None
        self._size = 0
        
    def append(self, val: T) -> None:
        """
        Append a value to the end of the list.
        Time Complexity: O(1) with tail pointer
        
        Args:
            val: The value to append
        """
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
        
    def prepend(self, val: T) -> None:
        """
        Add a value to the beginning of the list.
        Time Complexity: O(1)
        
        Args:
            val: The value to prepend
        """
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        if not self.tail:
            self.tail = new_node
        self._size += 1
        
    def insert_at(self, index: int, val: T) -> bool:
        """
        Insert a value at a specific position.
        Time Complexity: O(n)
        
        Args:
            index: The position to insert at (0-based)
            val: The value to insert
            
        Returns:
            True if insertion was successful, False if index is invalid
        """
        if index < 0 or index > len(self):
            return False
            
        if index == 0:
            self.prepend(val)
            return True
            
        if index == len(self):
            self.append(val)
            return True
            
        current = self.head
        for _ in range(index - 1):
            current = current.next
            
        new_node = ListNode(val)
        new_node.next = current.next
        current.next = new_node
        self._size += 1
        return True
        
    def delete_at(self, index: int) -> bool:
        """
        Delete the element at a specific position.
        Time Complexity: O(n)
        
        Args:
            index: The position to delete from (0-based)
            
        Returns:
            True if deletion was successful, False if index is invalid
        """
        if not self.head or index < 0 or index >= len(self):
            return False
            
        if index == 0:
            self.head = self.head.next
            self._size -= 1
            if self._size == 0:
                self.tail = None
            return True
            
        current = self.head
        for _ in range(index - 1):
            current = current.next
            
        # If deleting the last node, update tail
        if current.next == self.tail:
            self.tail = current
            
        current.next = current.next.next
        self._size -= 1
        return True
        
    def delete_value(self, val: T) -> bool:
        """
        Delete the first occurrence of a value.
        Time Complexity: O(n)
        
        Args:
            val: The value to delete
            
        Returns:
            True if the value was found and deleted, False otherwise
        """
        if not self.head:
            return False
            
        if self.head.val == val:
            self.head = self.head.next
            self._size -= 1
            if self._size == 0:
                self.tail = None
            return True
            
        current = self.head
        while current.next and current.next.val != val:
            current = current.next
            
        if current.next:
            # If deleting the last node, update tail
            if current.next == self.tail:
                self.tail = current
                
            current.next = current.next.next
            self._size -= 1
            return True
            
        return False
        
    def get(self, index: int) -> Optional[T]:
        """
        Get the value at a specific position.
        Time Complexity: O(n)
        
        Args:
            index: The position to get the value from (0-based)
            
        Returns:
            The value at the given position, or None if index is invalid
        """
        if index < 0 or index >= len(self):
            return None
            
        current = self.head
        for _ in range(index):
            current = current.next
            
        return current.val
        
    def index_of(self, val: T) -> int:
        """
        Find the index of the first occurrence of a value.
        Time Complexity: O(n)
        
        Args:
            val: The value to search for
            
        Returns:
            The index of the value, or -1 if not found
        """
        current = self.head
        index = 0
        
        while current:
            if current.val == val:
                return index
            current = current.next
            index += 1
            
        return -1
        
    def clear(self) -> None:
        """Clear all elements from the list."""
        self.head = None
        self.tail = None
        self._size = 0
        
    def to_list(self) -> List[T]:
        """
        Convert the linked list to a Python list.
        Time Complexity: O(n)
        
        Returns:
            A list containing all elements in order
        """
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result
        
    def reverse(self) -> None:
        """
        Reverse the linked list in-place.
        Time Complexity: O(n)
        """
        if not self.head or not self.head.next:
            return
            
        prev = None
        current = self.head
        self.tail = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
        self.head = prev
        
    def __len__(self) -> int:
        """Returns the number of elements in the list."""
        return self._size
        
    def __iter__(self) -> Iterator[T]:
        """Returns an iterator over the list's elements."""
        current = self.head
        while current:
            yield current.val
            current = current.next
            
    def __str__(self) -> str:
        """Returns a string representation of the list."""
        return str(self.to_list())
        
    def __eq__(self, other: object) -> bool:
        """Check if two linked lists are equal."""
        if not isinstance(other, LinkedList):
            return False
            
        if len(self) != len(other):
            return False
            
        current_self = self.head
        current_other = other.head
        
        while current_self and current_other:
            if current_self.val != current_other.val:
                return False
            current_self = current_self.next
            current_other = current_other.next
            
        return True