"""
Problem: Balanced Binary Tree
Link: https://leetcode.com/problems/balanced-binary-tree/

Approach:
- A binary tree is balanced if the height difference between the left and right subtrees of every node is at most 1.
- Use a recursive approach to calculate the height of the tree and check if it is balanced.
- Return -1 if the tree is not balanced, otherwise return the height of the tree.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root):
    def check_height(node):
        if not node:
            return 0

        # Recursively check the height of left and right subtrees
        left_height = check_height(node.left)
        if left_height == -1:
            return -1

        right_height = check_height(node.right)
        if right_height == -1:
            return -1

        # If the height difference is more than 1, return -1
        if abs(left_height - right_height) > 1:
            return -1

        # Return the height of the current node
        return max(left_height, right_height) + 1

    return check_height(root) != -1