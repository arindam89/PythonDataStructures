"""
LeetCode Problem: Kth Largest Element in an Array
Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

Approach:
- Use a Min-Heap to maintain the k largest elements in the array.
- Iterate through the array, adding elements to the heap.
- If the heap size exceeds k, remove the smallest element.
- The root of the heap will be the kth largest element.

Time Complexity:
- Building the heap: O(n log k), where n is the number of elements in the array.
- Space Complexity: O(k) for storing the heap.
"""

import heapq

def find_kth_largest(nums: list[int], k: int) -> int:
    """
    Return the kth largest element in the array.
    """
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)

        # If the heap size exceeds k, remove the smallest element
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # The root of the heap is the kth largest element
    return min_heap[0]