"""
Problem: Add Two Numbers
Link: https://leetcode.com/problems/add-two-numbers/

Description:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

Approach:
1. Use two pointers to traverse the two linked lists.
2. Use a carry variable to handle sums greater than 9.
3. Create a new linked list to store the result.

Time Complexity: O(max(m, n)) - Where `m` and `n` are the lengths of the two lists.
Space Complexity: O(max(m, n)) - For the output list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    dummy = ListNode()
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry

        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next