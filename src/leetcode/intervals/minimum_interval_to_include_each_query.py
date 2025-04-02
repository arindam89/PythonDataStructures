import heapq

"""
Problem: Minimum Interval to Include Each Query
Link: https://leetcode.com/problems/minimum-interval-to-include-each-query/

Approach:
1. Sort the intervals by their start times.
2. Sort the queries and process them in ascending order.
3. Use a min-heap to track intervals that can include the current query.
4. Remove intervals from the heap that cannot include the current query.
5. The top of the heap gives the smallest interval that includes the query.
6. Store the result for each query.

Time Complexity: O((n + m) log n), where n is the number of intervals and m is the number of queries.
Space Complexity: O(n), for the heap.
"""

def min_interval(intervals, queries):
    """
    Finds the minimum interval size that includes each query.

    :param intervals: List of intervals [start, end]
    :param queries: List of query points
    :return: List of minimum interval sizes for each query
    """
    intervals.sort(key=lambda x: x[0])
    queries_with_index = sorted((q, i) for i, q in enumerate(queries))
    result = [-1] * len(queries)
    min_heap = []
    i = 0

    for query, index in queries_with_index:
        while i < len(intervals) and intervals[i][0] <= query:
            start, end = intervals[i]
            heapq.heappush(min_heap, (end - start + 1, end, start))
            i += 1

        while min_heap and min_heap[0][1] < query:
            heapq.heappop(min_heap)

        if min_heap:
            result[index] = min_heap[0][0]

    return result