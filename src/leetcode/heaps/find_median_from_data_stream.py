"""
LeetCode Problem: Find Median from Data Stream
Link: https://leetcode.com/problems/find-median-from-data-stream/

Approach:
- Use two heaps: a Max-Heap for the lower half of the numbers and a Min-Heap for the upper half.
- Ensure the heaps are balanced in size, with the Max-Heap allowed to have one extra element.
- The median is either the root of the Max-Heap (odd number of elements) or the average of the roots of both heaps (even number of elements).

Time Complexity:
- Adding a number: O(log n), where n is the number of elements.
- Finding the median: O(1).

Space Complexity: O(n) for storing the heaps.
"""

import heapq

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lower_half = []  # Max-Heap (inverted Min-Heap)
        self.upper_half = []  # Min-Heap

    def addNum(self, num: int) -> None:
        """
        Add a number to the data structure.
        """
        # Add to Max-Heap (lower half)
        heapq.heappush(self.lower_half, -num)

        # Balance the heaps by moving the largest of lower_half to upper_half
        heapq.heappush(self.upper_half, -heapq.heappop(self.lower_half))

        # Ensure lower_half can have one more element than upper_half
        if len(self.lower_half) < len(self.upper_half):
            heapq.heappush(self.lower_half, -heapq.heappop(self.upper_half))

    def findMedian(self) -> float:
        """
        Return the median of all elements so far.
        """
        if len(self.lower_half) > len(self.upper_half):
            return -self.lower_half[0]  # Max-Heap root
        return (-self.lower_half[0] + self.upper_half[0]) / 2.0  # Average of roots