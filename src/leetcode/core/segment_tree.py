# Implementation of a Segment Tree in Python
# Problem: Design a segment tree that supports range queries and updates.
# LeetCode Link: https://leetcode.com/problems/range-sum-query-mutable/

class SegmentTree:
    def __init__(self, nums):
        """Initialize the segment tree with the given array."""
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        # Build the tree
        for i in range(self.n):
            self.tree[self.n + i] = nums[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, value):
        """Update the value at a specific index."""
        pos = self.n + index
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]

    def range_query(self, left, right):
        """Query the sum in the range [left, right)."""
        result = 0
        left += self.n
        right += self.n
        while left < right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            if right % 2 == 1:
                right -= 1
                result += self.tree[right]
            left //= 2
            right //= 2
        return result