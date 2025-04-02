"""
Problem: Design Singly Linked List
Link: https://leetcode.com/problems/design-linked-list/

Description:
Design a singly linked list with the following operations:
1. get(index): Get the value of the index-th node in the linked list. If the index is invalid, return -1.
2. addAtHead(val): Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
3. addAtTail(val): Append a node of value val as the last element of the linked list.
4. addAtIndex(index, val): Add a node of value val before the index-th node in the linked list. If index equals the length of the linked list, the node will be appended to the end. If index is greater than the length, the node will not be inserted.
5. deleteAtIndex(index): Delete the index-th node in the linked list, if the index is valid.

Approach:
- Use a simple ListNode class to represent each node in the linked list.
- Maintain a head pointer to track the start of the list and a size variable to track the number of elements.

Time Complexity:
- get: O(n)
- addAtHead: O(1)
- addAtTail: O(n)
- addAtIndex: O(n)
- deleteAtIndex: O(n)

Space Complexity: O(n)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        for _ in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val, self.head)
        self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node = ListNode(val, current.next)
        current.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1