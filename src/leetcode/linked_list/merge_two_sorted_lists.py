"""
Problem: Merge Two Sorted Lists
Link: https://leetcode.com/problems/merge-two-sorted-lists/

Description:
You are given the heads of two sorted linked lists `list1` and `list2`. Merge the two lists into one sorted linked list and return its head.

Approach:
1. Use a dummy node to simplify the merging process.
2. Compare the nodes of both lists and attach the smaller node to the merged list.
3. Continue until one of the lists is exhausted, then attach the remaining nodes of the other list.

Time Complexity: O(n + m) - Where `n` and `m` are the lengths of the two lists.
Space Complexity: O(1) - No additional space is used.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_sorted_lists(list1, list2):
    dummy = ListNode(-1)
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Attach the remaining nodes of the non-empty list
    current.next = list1 if list1 else list2

    return dummy.next