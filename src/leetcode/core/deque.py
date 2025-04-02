# Implementation of a Double-ended Queue (Deque) in Python
# Problem: Design a deque that supports operations like add to front, add to rear, delete from front, delete from rear, and check if empty.
# LeetCode Link: Not directly available, but this is a fundamental data structure.

class Deque:
    def __init__(self):
        """Initialize the deque."""
        self.items = []

    def add_front(self, value):
        """Add an element to the front of the deque."""
        self.items.insert(0, value)

    def add_rear(self, value):
        """Add an element to the rear of the deque."""
        self.items.append(value)

    def delete_front(self):
        """Delete an element from the front of the deque."""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items.pop(0)

    def delete_rear(self):
        """Delete an element from the rear of the deque."""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items.pop()

    def is_empty(self):
        """Check if the deque is empty."""
        return len(self.items) == 0

    def __len__(self):
        """Return the number of elements in the deque."""
        return len(self.items)

    def __str__(self):
        """Return a string representation of the deque."""
        return str(self.items)