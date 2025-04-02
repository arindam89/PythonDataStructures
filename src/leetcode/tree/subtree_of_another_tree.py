"""
Problem: Subtree of Another Tree
Link: https://leetcode.com/problems/subtree-of-another-tree/

Approach:
- Use a recursive approach to check if one tree is a subtree of another.
- For each node in the main tree, check if the subtree rooted at that node is identical to the given subtree.
- Use a helper function to check if two trees are identical.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_subtree(root, sub_root):
    def is_same_tree(p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        # Recursively check the left and right subtrees
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

    if not root:
        return False
    if is_same_tree(root, sub_root):
        return True

    # Recursively check the left and right subtrees
    return is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)