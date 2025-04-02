"""
LeetCode Problem: Last Stone Weight
Link: https://leetcode.com/problems/last-stone-weight/

Approach:
- Use a Max-Heap (simulated using a Min-Heap with negative values) to always get the two heaviest stones.
- Smash the two heaviest stones and push the resulting weight (if any) back into the heap.
- Repeat until one or no stones are left.

Time Complexity:
- Each insertion and extraction from the heap takes O(log n), where n is the number of stones.
- Space Complexity: O(n) for storing the heap.
"""

import heapq

def last_stone_weight(stones: list[int]) -> int:
    """
    Return the weight of the last remaining stone (or 0 if no stones are left).
    """
    # Convert all stones to negative values to simulate a Max-Heap
    max_heap = [-stone for stone in stones]
    heapq.heapify(max_heap)

    while len(max_heap) > 1:
        # Extract the two heaviest stones
        stone1 = -heapq.heappop(max_heap)
        stone2 = -heapq.heappop(max_heap)

        # If they are not equal, push the difference back into the heap
        if stone1 != stone2:
            heapq.heappush(max_heap, -(stone1 - stone2))

    # Return the weight of the last stone (or 0 if no stones are left)
    return -max_heap[0] if max_heap else 0