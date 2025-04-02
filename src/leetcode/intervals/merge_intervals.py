"""
Problem: Merge Intervals
Link: https://leetcode.com/problems/merge-intervals/

Approach:
1. Sort the intervals by their start times.
2. Traverse the sorted intervals and merge overlapping intervals by updating the end of the current interval.
3. Add non-overlapping intervals directly to the result.

Time Complexity: O(n log n), where n is the number of intervals (due to sorting).
Space Complexity: O(n), for the result list.
"""

def merge(intervals):
    """
    Merges all overlapping intervals in a list.

    :param intervals: List of intervals [start, end]
    :return: List of merged intervals
    """
    if not intervals:
        return []

    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:
            # Merge intervals
            previous[1] = max(previous[1], current[1])
        else:
            merged.append(current)

    return merged