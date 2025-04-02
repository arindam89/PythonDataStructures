"""
Problem: Remove Nth Node From End of List
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Description:
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Approach:
1. Use two pointers, `first` and `second`, initialized to the head.
2. Move `first` pointer `n` steps ahead.
3. Move both pointers one step at a time until `first` reaches the end.
4. The `second` pointer will be at the node just before the one to be removed. Adjust the `next` pointer to skip the target node.

Time Complexity: O(n) - We traverse the list once.
Space Complexity: O(1) - No additional space is used.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    first = dummy
    second = dummy

    # Move `first` pointer `n + 1` steps ahead
    for _ in range(n + 1):
        first = first.next

    # Move both pointers until `first` reaches the end
    while first:
        first = first.next
        second = second.next

    # Remove the nth node from the end
    second.next = second.next.next

    return dummy.next