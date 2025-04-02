"""
Problem: Alien Dictionary
Link: https://leetcode.com/problems/alien-dictionary/

Approach:
- Use Topological Sort to determine the order of characters in the alien language.
- Build a graph where each character is a node, and edges represent the precedence between characters.
- Perform a BFS (Kahn's Algorithm) or DFS to find the topological order of the graph.
- If a cycle is detected, return an empty string.

Time Complexity: O(C), where C is the total number of characters in all words.
Space Complexity: O(1) for the graph and in-degree array (bounded by the number of unique characters).
"""

from collections import defaultdict, deque

def alien_order(words):
    """
    Determine the order of characters in an alien language.

    Args:
        words: List of words sorted lexicographically in the alien language.

    Returns:
        A string representing the order of characters, or an empty string if invalid.
    """
    # Step 1: Build the graph
    graph = defaultdict(set)
    in_degree = {char: 0 for word in words for char in word}

    for i in range(len(words) - 1):
        first, second = words[i], words[i + 1]
        min_length = min(len(first), len(second))

        # Check for invalid order (prefix case)
        if len(first) > len(second) and first[:min_length] == second[:min_length]:
            return ""

        for j in range(min_length):
            if first[j] != second[j]:
                if second[j] not in graph[first[j]]:
                    graph[first[j]].add(second[j])
                    in_degree[second[j]] += 1
                break

    # Step 2: Perform Topological Sort (Kahn's Algorithm)
    queue = deque([char for char in in_degree if in_degree[char] == 0])
    order = []

    while queue:
        char = queue.popleft()
        order.append(char)

        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If all characters are not in the order, there is a cycle
    if len(order) < len(in_degree):
        return ""

    return "".join(order)