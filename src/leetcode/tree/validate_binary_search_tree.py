"""
Problem: Validate Binary Search Tree
Link: https://leetcode.com/problems/validate-binary-search-tree/

Approach:
- Use a recursive approach to validate the binary search tree (BST).
- For each node, ensure that its value lies within a valid range defined by its ancestors.
- Pass the valid range (min and max values) as parameters during the recursion.
- If a node violates the BST property, return False.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root):
    def validate(node, low, high):
        if not node:
            return True

        # Check if the current node's value is within the valid range
        if not (low < node.val < high):
            return False

        # Recursively validate the left and right subtrees
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)

    return validate(root, float('-inf'), float('inf'))