"""
LeetCode 207: Course Schedule
https://leetcode.com/problems/course-schedule/

There are a total of numCourses courses you have to take, labeled from 0 to
numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi]
indicates that you must take course bi first if you want to take course ai.

Return true if you can finish all courses. Otherwise, return false.

Example:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are 2 courses to take. To take course 1 you should have finished course 0.
So it is possible.

Time Complexity: O(V + E) where V is number of courses and E is number of prerequisites
Space Complexity: O(V + E)
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