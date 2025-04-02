"""
Problem: Linked List Cycle
Link: https://leetcode.com/problems/linked-list-cycle/

Description:
Given the head of a linked list, determine if the linked list has a cycle in it.

Approach:
1. Use the Floyd's Cycle Detection Algorithm (Tortoise and Hare).
2. Use two pointers, `slow` and `fast`. Move `slow` one step and `fast` two steps.
3. If there is a cycle, `slow` and `fast` will eventually meet.
4. If `fast` or `fast.next` becomes `None`, there is no cycle.

Time Complexity: O(n) - We traverse the list once.
Space Complexity: O(1) - No additional space is used.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False