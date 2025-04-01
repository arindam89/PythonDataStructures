"""
LeetCode 295: Find Median from Data Stream
https://leetcode.com/problems/find-median-from-data-stream/

Implement the MedianFinder class:
- MedianFinder(): Initialize the MedianFinder object.
- void addNum(int num): Adds the integer num from the data stream to the data structure.
- double findMedian(): Returns the median of all elements so far.

Time Complexity:
- addNum: O(log n)
- findMedian: O(1)
Space Complexity: O(n)

The solution uses two heaps:
- A max heap for the lower half of numbers
- A min heap for the upper half of numbers
The median is either the max of lower half, min of upper half, or their average.
"""

import heapq
from typing import List

class MedianFinder:
    """
    Maintains a running median of a stream of numbers using two heaps.
    """
    
    def __init__(self):
        """Initialize two heaps for storing numbers."""
        # Max heap for lower half (multiply by -1 to simulate max heap)
        self.lower_half = []
        # Min heap for upper half
        self.upper_half = []
        
    def addNum(self, num: int) -> None:
        """
        Add a number to the data structure.
        Maintains balance between heaps such that their size differs by at most 1.
        
        Args:
            num: Number to add
        """
        # First try adding to lower half (as negative for max heap)
        heapq.heappush(self.lower_half, -num)
        
        # Make sure every number in lower half is <= every number in upper half
        if (self.lower_half and self.upper_half and
            -self.lower_half[0] > self.upper_half[0]):
            # Move the largest value from lower to upper
            value = -heapq.heappop(self.lower_half)
            heapq.heappush(self.upper_half, value)
            
        # Balance the heaps if necessary
        while len(self.lower_half) > len(self.upper_half) + 1:
            value = -heapq.heappop(self.lower_half)
            heapq.heappush(self.upper_half, value)
            
        while len(self.upper_half) > len(self.lower_half):
            value = heapq.heappop(self.upper_half)
            heapq.heappush(self.lower_half, -value)
            
    def findMedian(self) -> float:
        """
        Find the median of all numbers added so far.
        
        Returns:
            The median value
        """
        if len(self.lower_half) > len(self.upper_half):
            return float(-self.lower_half[0])
        elif len(self.lower_half) == len(self.upper_half):
            return (-self.lower_half[0] + self.upper_half[0]) / 2.0
        else:
            return float(self.upper_half[0])
            
    def getCount(self) -> int:
        """
        Get the total number of elements.
        
        Returns:
            Number of elements in the data structure
        """
        return len(self.lower_half) + len(self.upper_half)
        
    def clear(self) -> None:
        """Remove all elements."""
        self.lower_half = []
        self.upper_half = []