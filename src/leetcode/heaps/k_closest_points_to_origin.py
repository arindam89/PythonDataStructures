"""
LeetCode Problem: K Closest Points to Origin
Link: https://leetcode.com/problems/k-closest-points-to-origin/

Approach:
- Use a Max-Heap to maintain the k closest points to the origin.
- For each point, calculate its squared distance from the origin (to avoid floating-point operations).
- If the heap size exceeds k, remove the farthest point.
- Return the points in the heap as the result.

Time Complexity:
- Building the heap: O(n log k), where n is the number of points.
- Space Complexity: O(k) for storing the heap.
"""

import heapq

def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    """
    Return the k closest points to the origin.
    """
    max_heap = []

    for x, y in points:
        # Calculate squared distance from the origin
        dist = -(x**2 + y**2)  # Use negative to simulate a Max-Heap
        heapq.heappush(max_heap, (dist, [x, y]))

        # If the heap size exceeds k, remove the farthest point
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    # Extract the points from the heap
    return [point for _, point in max_heap]