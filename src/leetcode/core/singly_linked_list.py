# Implementation of a Singly Linked List in Python
# Problem: Design a singly linked list that supports operations like add, delete, and search.
# LeetCode Link: https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        """Initialize the singly linked list."""
        self.head = None

    def add_at_head(self, value):
        """Add a node at the head of the list."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def add_at_tail(self, value):
        """Add a node at the tail of the list."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, value):
        """Delete the first occurrence of a node with the given value."""
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        if current.next:
            current.next = current.next.next

    def search(self, value):
        """Search for a node with the given value."""
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def __str__(self):
        """Return a string representation of the list."""
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return "->".join(map(str, result))