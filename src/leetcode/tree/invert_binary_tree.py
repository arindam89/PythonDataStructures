"""
Problem: Invert Binary Tree
Link: https://leetcode.com/problems/invert-binary-tree/

Approach:
- Use a recursive approach to swap the left and right children of each node in the binary tree.
- Base case: If the node is None, return None.
- Recursively invert the left and right subtrees, then swap them.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root):
    if not root:
        return None

    # Swap the left and right children
    root.left, root.right = root.right, root.left

    # Recursively invert the left and right subtrees
    invert_tree(root.left)
    invert_tree(root.right)

    return root