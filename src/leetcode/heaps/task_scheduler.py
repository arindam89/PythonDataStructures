"""
LeetCode Problem: Task Scheduler
Link: https://leetcode.com/problems/task-scheduler/

Approach:
- Use a Max-Heap to schedule tasks with the highest frequency first.
- Maintain a cooldown queue to track tasks that are cooling down.
- At each time step, either execute a task from the heap or wait (idle).
- Push tasks back into the heap after their cooldown period ends.

Time Complexity:
- O(n log k), where n is the total number of tasks and k is the number of unique tasks.
- Space Complexity: O(k) for the heap and cooldown queue.
"""

import heapq
from collections import Counter, deque

def least_interval(tasks: list[str], n: int) -> int:
    """
    Return the least number of units of time required to finish all tasks.
    """
    # Count the frequency of each task
    task_counts = Counter(tasks)

    # Use a Max-Heap to store task frequencies (negative values for Max-Heap simulation)
    max_heap = [-count for count in task_counts.values()]
    heapq.heapify(max_heap)

    # Cooldown queue to track tasks and their cooldown times
    cooldown = deque()
    time = 0

    while max_heap or cooldown:
        time += 1

        if max_heap:
            # Execute the most frequent task
            count = heapq.heappop(max_heap) + 1  # Increment because we use negative values
            if count < 0:
                cooldown.append((count, time + n))

        if cooldown and cooldown[0][1] == time:
            # Push the task back into the heap after cooldown
            heapq.heappush(max_heap, cooldown.popleft()[0])

    return time