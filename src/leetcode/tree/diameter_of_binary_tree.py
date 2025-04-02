"""
Problem: Diameter of Binary Tree
Link: https://leetcode.com/problems/diameter-of-binary-tree/

Approach:
- Use a recursive approach to calculate the diameter of the binary tree.
- The diameter of a tree is the length of the longest path between any two nodes in a tree.
- For each node, calculate the depth of its left and right subtrees, and update the diameter as the sum of these two depths.
- Use a helper function to calculate the depth and update the diameter simultaneously.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameter_of_binary_tree(root):
    def depth(node):
        nonlocal diameter
        if not node:
            return 0

        # Recursively calculate the depth of left and right subtrees
        left_depth = depth(node.left)
        right_depth = depth(node.right)

        # Update the diameter (longest path through the current node)
        diameter = max(diameter, left_depth + right_depth)

        # Return the depth of the current node
        return max(left_depth, right_depth) + 1

    diameter = 0
    depth(root)
    return diameter