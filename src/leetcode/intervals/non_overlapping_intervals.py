"""
Problem: Non-Overlapping Intervals
Link: https://leetcode.com/problems/non-overlapping-intervals/

Approach:
1. Sort the intervals by their end times.
2. Traverse the intervals and count overlapping intervals by checking if the start of the current interval is less than the end of the previous interval.
3. Increment the count for each overlapping interval.

Time Complexity: O(n log n), where n is the number of intervals (due to sorting).
Space Complexity: O(1), as no extra space is used apart from variables.
"""

def erase_overlap_intervals(intervals):
    """
    Finds the minimum number of intervals to remove to make the rest non-overlapping.

    :param intervals: List of intervals [start, end]
    :return: Minimum number of intervals to remove
    """
    if not intervals:
        return 0

    # Sort intervals by end time
    intervals.sort(key=lambda x: x[1])
    count = 0
    end = float('-inf')

    for interval in intervals:
        if interval[0] >= end:
            end = interval[1]
        else:
            count += 1

    return count