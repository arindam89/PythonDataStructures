import heapq

"""
Problem: Meeting Rooms II
Link: https://leetcode.com/problems/meeting-rooms-ii/

Approach:
1. Sort the intervals by their start times.
2. Use a min-heap to track the end times of ongoing meetings.
3. For each interval, check if the earliest ending meeting has ended before the current meeting starts. If so, remove it from the heap.
4. Add the current meeting's end time to the heap.
5. The size of the heap at the end represents the minimum number of meeting rooms required.

Time Complexity: O(n log n), where n is the number of intervals (due to sorting and heap operations).
Space Complexity: O(n), for the heap.
"""

def min_meeting_rooms(intervals):
    """
    Finds the minimum number of meeting rooms required.

    :param intervals: List of intervals [start, end]
    :return: Minimum number of meeting rooms required
    """
    if not intervals:
        return 0

    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    min_heap = []

    for interval in intervals:
        # If the room due to free up the earliest is free, remove it from the heap
        if min_heap and min_heap[0] <= interval[0]:
            heapq.heappop(min_heap)

        # Add the current meeting's end time to the heap
        heapq.heappush(min_heap, interval[1])

    return len(min_heap)