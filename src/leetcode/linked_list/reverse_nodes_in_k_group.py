"""
Problem: Reverse Nodes in K Group
Link: https://leetcode.com/problems/reverse-nodes-in-k-group/

Description:
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list. k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k, leave the remaining nodes as is.

Approach:
1. Count the total number of nodes in the list.
2. Reverse the first k nodes, then recursively reverse the remaining nodes in groups of k.
3. Use a helper function to reverse k nodes at a time.

Time Complexity: O(n) - We traverse the list multiple times.
Space Complexity: O(1) - No additional space is used (excluding recursion stack).
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_k_group(head, k):
    # Helper function to check if there are at least k nodes left
    def has_k_nodes(node, k):
        count = 0
        while node and count < k:
            node = node.next
            count += 1
        return count == k

    # Helper function to reverse k nodes
    def reverse_k_nodes(node, k):
        prev, current = None, node
        for _ in range(k):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    if not has_k_nodes(head, k):
        return head

    new_head = reverse_k_nodes(head, k)
    head.next = reverse_k_group(head.next, k)
    return new_head