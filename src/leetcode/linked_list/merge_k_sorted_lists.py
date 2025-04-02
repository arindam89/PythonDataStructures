"""
Problem: Merge K Sorted Lists
Link: https://leetcode.com/problems/merge-k-sorted-lists/

Description:
You are given an array of k linked-lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.

Approach:
1. Use a priority queue (min-heap) to efficiently get the smallest node among the k lists.
2. Add the smallest node to the merged list and push its next node into the heap.
3. Continue until all nodes are processed.

Time Complexity: O(N log k) - Where N is the total number of nodes and k is the number of lists.
Space Complexity: O(k) - For the heap.
"""

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_sorted_lists(lists):
    heap = []

    # Initialize the heap with the head of each list
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode()
    current = dummy

    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next