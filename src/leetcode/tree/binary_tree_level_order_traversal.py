"""
Problem: Binary Tree Level Order Traversal
Link: https://leetcode.com/problems/binary-tree-level-order-traversal/

Approach:
- Use a breadth-first search (BFS) approach to traverse the binary tree level by level.
- Use a queue to keep track of nodes at the current level.
- For each level, process all nodes in the queue and add their children to the queue for the next level.
- Append the values of nodes at each level to the result list.
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result