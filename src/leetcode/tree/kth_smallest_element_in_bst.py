"""
Problem: Kth Smallest Element in a BST
Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Approach:
- Use an in-order traversal of the BST to retrieve elements in sorted order.
- Keep a counter to track the number of elements visited.
- Stop the traversal once the kth element is found.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest(root, k):
    def in_order_traversal(node):
        if not node:
            return []
        # Perform in-order traversal: left, root, right
        return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)

    # Get all elements in sorted order
    sorted_elements = in_order_traversal(root)
    # Return the kth smallest element (1-indexed)
    return sorted_elements[k - 1]