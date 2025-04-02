"""
Problem: LRU Cache
Link: https://leetcode.com/problems/lru-cache/

Description:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Approach:
1. Use a combination of a dictionary and a doubly linked list.
2. The dictionary provides O(1) access to cache items.
3. The doubly linked list maintains the order of usage, with the most recently used item at the head and the least recently used item at the tail.

Time Complexity:
- O(1) for get and put operations.

Space Complexity: O(capacity) - For storing the cache items.
"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Remove a node from the doubly linked list."""
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def _add(self, node):
        """Add a node right after the head."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._add(node)
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]