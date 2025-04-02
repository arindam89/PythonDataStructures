"""
Problem: Copy List with Random Pointer
Link: https://leetcode.com/problems/copy-list-with-random-pointer/

Description:
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null. Construct a deep copy of the list.

Approach:
1. Create a copy of each node and insert it right after the original node.
2. Update the random pointers for the copied nodes.
3. Separate the original and copied nodes to form two independent lists.

Time Complexity: O(n) - We traverse the list multiple times.
Space Complexity: O(1) - No additional space is used (excluding the output list).
"""

class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copy_random_list(head):
    if not head:
        return None

    # Step 1: Create a copy of each node and insert it right after the original node
    current = head
    while current:
        new_node = Node(current.val, current.next)
        current.next = new_node
        current = new_node.next

    # Step 2: Update the random pointers for the copied nodes
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next

    # Step 3: Separate the original and copied nodes
    current = head
    copy_head = head.next
    while current:
        copy = current.next
        current.next = copy.next
        current = current.next
        if copy.next:
            copy.next = copy.next.next

    return copy_head