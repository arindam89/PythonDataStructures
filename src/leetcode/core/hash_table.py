# Implementation of a Hash Table in Python
# Problem: Design a hash table that supports operations like put, get, and remove.
# LeetCode Link: https://leetcode.com/problems/design-hashmap/

class HashTable:
    def __init__(self, size=1000):
        """Initialize the hash table with a fixed size."""
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        """Generate a hash for a given key."""
        return key % self.size

    def put(self, key, value):
        """Insert a key-value pair into the hash table."""
        hash_key = self._hash(key)
        for i, (k, v) in enumerate(self.table[hash_key]):
            if k == key:
                self.table[hash_key][i] = (key, value)
                return
        self.table[hash_key].append((key, value))

    def get(self, key):
        """Retrieve the value associated with a key."""
        hash_key = self._hash(key)
        for k, v in self.table[hash_key]:
            if k == key:
                return v
        return -1

    def remove(self, key):
        """Remove a key-value pair from the hash table."""
        hash_key = self._hash(key)
        for i, (k, v) in enumerate(self.table[hash_key]):
            if k == key:
                del self.table[hash_key][i]
                return

    def __str__(self):
        """Return a string representation of the hash table."""
        return str(self.table)