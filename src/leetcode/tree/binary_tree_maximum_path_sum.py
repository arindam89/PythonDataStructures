"""
Problem: Binary Tree Maximum Path Sum
Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/

Approach:
- Use a recursive approach to calculate the maximum path sum.
- For each node, calculate the maximum path sum that includes the node and its left and right subtrees.
- Keep track of the global maximum path sum during the recursion.
- Return the maximum path sum that can be extended to the parent node.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_path_sum(root):
    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0

        # Recursively calculate the maximum path sum for left and right subtrees
        left_max = max(dfs(node.left), 0)  # Ignore negative paths
        right_max = max(dfs(node.right), 0)  # Ignore negative paths

        # Update the global maximum path sum
        max_sum = max(max_sum, node.val + left_max + right_max)

        # Return the maximum path sum that can be extended to the parent node
        return node.val + max(left_max, right_max)

    max_sum = float('-inf')
    dfs(root)
    return max_sum