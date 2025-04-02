# Implementation of a Min Heap in Python
# Problem: Design a heap that supports operations like insert, delete, and extract-min.
# LeetCode Link: https://leetcode.com/problems/minimum-cost-to-connect-sticks/ (uses heap)

import heapq

class MinHeap:
    def __init__(self):
        """Initialize the min heap."""
        self.heap = []

    def insert(self, value):
        """Insert a value into the heap."""
        heapq.heappush(self.heap, value)

    def extract_min(self):
        """Extract the minimum value from the heap."""
        if not self.heap:
            raise IndexError("Heap is empty")
        return heapq.heappop(self.heap)

    def delete(self, value):
        """Delete a specific value from the heap."""
        try:
            self.heap.remove(value)
            heapq.heapify(self.heap)
        except ValueError:
            raise ValueError("Value not found in heap")

    def __len__(self):
        """Return the number of elements in the heap."""
        return len(self.heap)

    def __str__(self):
        """Return a string representation of the heap."""
        return str(self.heap)