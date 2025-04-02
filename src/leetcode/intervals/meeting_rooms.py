"""
Problem: Meeting Rooms
Link: https://leetcode.com/problems/meeting-rooms/

Approach:
1. Sort the intervals by their start times.
2. Traverse the sorted intervals and check if the start of the current interval is less than the end of the previous interval.
3. If any overlap is found, return False. Otherwise, return True.

Time Complexity: O(n log n), where n is the number of intervals (due to sorting).
Space Complexity: O(1), as no extra space is used apart from variables.
"""

def can_attend_meetings(intervals):
    """
    Determines if a person can attend all meetings without overlap.

    :param intervals: List of intervals [start, end]
    :return: True if a person can attend all meetings, False otherwise
    """
    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False

    return True