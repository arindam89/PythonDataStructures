"""
Problem: Maximum Depth of Binary Tree
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Approach:
- Use a recursive approach to calculate the depth of the binary tree.
- Base case: If the node is None, return 0.
- Recursively calculate the depth of the left and right subtrees, and return the maximum of the two depths plus 1.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    if not root:
        return 0

    # Recursively calculate the depth of left and right subtrees
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    # Return the maximum depth plus 1 (for the current node)
    return max(left_depth, right_depth) + 1