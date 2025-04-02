"""
LeetCode Problem: Kth Largest Element in a Stream
Link: https://leetcode.com/problems/kth-largest-element-in-a-stream/

Approach:
- Use a Min-Heap to maintain the k largest elements seen so far.
- The root of the heap will always be the kth largest element.
- Insert new elements into the heap and ensure the size of the heap does not exceed k.

Time Complexity:
- Adding an element: O(log k), where k is the size of the heap.
- Space Complexity: O(k) for storing the heap.
"""

import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        """
        Initialize the object with the integer k and the stream of integers nums.
        """
        self.k = k
        self.min_heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        """
        Add the integer val to the stream and return the kth largest element.
        """
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]