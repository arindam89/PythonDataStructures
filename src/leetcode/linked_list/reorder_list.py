"""
Problem: Reorder List
Link: https://leetcode.com/problems/reorder-list/

Description:
You are given the head of a singly linked list. Reorder the list to follow the pattern:
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

Approach:
1. Find the middle of the linked list using the slow and fast pointer technique.
2. Reverse the second half of the list.
3. Merge the two halves by alternating nodes from each half.

Time Complexity: O(n) - We traverse the list multiple times.
Space Complexity: O(1) - No additional space is used.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorder_list(head):
    if not head or not head.next:
        return

    # Step 1: Find the middle of the list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the list
    prev, current = None, slow.next
    slow.next = None  # Split the list into two halves
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    # Step 3: Merge the two halves
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2