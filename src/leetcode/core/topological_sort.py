# Implementation of Topological Sort in Python
# Problem: Perform topological sort on a Directed Acyclic Graph (DAG).
# LeetCode Link: https://leetcode.com/problems/course-schedule-ii/ (uses topological sort)
from collections import defaultdict, deque

def topological_sort(num_nodes, edges):
    """Perform topological sort on a DAG and return the sorted order."""
    in_degree = {i: 0 for i in range(num_nodes)}
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    queue = deque([node for node in in_degree if in_degree[node] == 0])
    sorted_order = []

    while queue:
        node = queue.popleft()
        sorted_order.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(sorted_order) == num_nodes:
        return sorted_order
    else:
        return []  # Return an empty list if there is a cycle