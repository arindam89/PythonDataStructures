"""
Problem: Binary Tree Right Side View
Link: https://leetcode.com/problems/binary-tree-right-side-view/

Approach:
- Use a breadth-first search (BFS) approach to traverse the binary tree level by level.
- For each level, add the last node's value to the result list (this represents the rightmost node of that level).
- Use a queue to keep track of nodes at the current level.
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def right_side_view(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            # Add the last node of each level to the result
            if i == level_size - 1:
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result