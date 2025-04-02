"""
LeetCode 207: Course Schedule
Link: https://leetcode.com/problems/course-schedule/

Approach:
- Use Kahn's Algorithm (Topological Sort) to determine if the course dependency graph has a cycle.
- Build an adjacency list to represent the graph and an in-degree array to track the number of prerequisites for each course.
- Start with courses that have no prerequisites (in-degree 0) and process them in topological order.
- If all courses can be processed, return True. Otherwise, return False (cycle detected).

Time Complexity: O(V + E), where V is the number of courses and E is the number of prerequisites.
Space Complexity: O(V + E) for the graph representation and in-degree array.

Additional Notes:
- This implementation assumes that the input is valid and does not contain duplicate edges.
- The algorithm is efficient for large graphs with many dependencies.
"""

from typing import List
from collections import defaultdict, deque

def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """
    Determine if it's possible to finish all courses using topological sort.
    Uses Kahn's algorithm to detect cycles in the course dependency graph.

    Args:
        num_courses: Number of courses
        prerequisites: List of prerequisite pairs [course, prereq]

    Returns:
        True if all courses can be completed, False if there's a cycle
    """
    # Build adjacency list and in-degree count
    graph = defaultdict(list)
    in_degree = [0] * num_courses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    # Start with all courses that have no prerequisites
    queue = deque(
        course for course in range(num_courses) 
        if in_degree[course] == 0
    )

    courses_taken = 0

    # Process courses in topological order
    while queue:
        current = queue.popleft()
        courses_taken += 1

        # For each course that depends on current course
        for next_course in graph[current]:
            in_degree[next_course] -= 1
            # If all prerequisites are satisfied
            if in_degree[next_course] == 0:
                queue.append(next_course)

    # If we can take all courses, there's no cycle
    return courses_taken == num_courses