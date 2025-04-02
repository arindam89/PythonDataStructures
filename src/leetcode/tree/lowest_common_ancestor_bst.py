"""
Problem: Lowest Common Ancestor of a Binary Search Tree
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Approach:
- Use the properties of a Binary Search Tree (BST) to find the Lowest Common Ancestor (LCA).
- If both nodes `p` and `q` are smaller than the current node, the LCA lies in the left subtree.
- If both nodes `p` and `q` are greater than the current node, the LCA lies in the right subtree.
- Otherwise, the current node is the LCA.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root, p, q):
    while root:
        # If both nodes are smaller than the current node, go left
        if p.val < root.val and q.val < root.val:
            root = root.left
        # If both nodes are greater than the current node, go right
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            # The current node is the LCA
            return root