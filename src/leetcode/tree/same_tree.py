"""
Problem: Same Tree
Link: https://leetcode.com/problems/same-tree/

Approach:
- Use a recursive approach to check if two binary trees are the same.
- Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
- Base case: If both nodes are None, return True. If one is None and the other is not, return False.
- Recursively check the left and right subtrees.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False

    # Recursively check the left and right subtrees
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)