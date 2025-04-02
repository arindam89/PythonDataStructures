"""
Problem: Reverse Linked List
Link: https://leetcode.com/problems/reverse-linked-list/

Description:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Approach:
1. Use an iterative approach with two pointers: `prev` and `current`.
2. Traverse the list, reversing the `next` pointer of each node.
3. At the end, `prev` will point to the new head of the reversed list.

Time Complexity: O(n) - We traverse the list once.
Space Complexity: O(1) - No additional space is used.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next  # Store the next node
        current.next = prev      # Reverse the link
        prev = current           # Move `prev` to the current node
        current = next_node      # Move to the next node

    return prev  # `prev` is the new head