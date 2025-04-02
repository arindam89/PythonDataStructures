"""
Problem: Insert Interval
Link: https://leetcode.com/problems/insert-interval/

Approach:
1. Traverse the list of intervals and add all intervals that end before the new interval starts.
2. Merge all overlapping intervals with the new interval by updating its start and end.
3. Add the merged interval to the result.
4. Append all remaining intervals that start after the new interval ends.

Time Complexity: O(n), where n is the number of intervals.
Space Complexity: O(n), for the result list.
"""

def insert(intervals, new_interval):
    """
    Inserts a new interval into a list of non-overlapping intervals and merges if necessary.

    :param intervals: List of intervals [start, end]
    :param new_interval: Interval to insert [start, end]
    :return: List of merged intervals
    """
    result = []
    i = 0
    # Add all intervals before the new interval
    while i < len(intervals) and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    # Merge overlapping intervals
    while i < len(intervals) and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    result.append(new_interval)

    # Add all intervals after the new interval
    while i < len(intervals):
        result.append(intervals[i])
        i += 1

    return result