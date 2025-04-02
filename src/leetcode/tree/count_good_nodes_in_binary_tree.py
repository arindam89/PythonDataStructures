"""
Problem: Count Good Nodes in Binary Tree
Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/

Approach:
- Use a depth-first search (DFS) approach to traverse the binary tree.
- A node is considered "good" if its value is greater than or equal to the maximum value encountered along the path from the root to that node.
- Pass the maximum value encountered so far as a parameter during the DFS traversal.
- Increment the count whenever a "good" node is found.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def good_nodes(root):
    def dfs(node, max_val):
        if not node:
            return 0

        # Check if the current node is a "good" node
        is_good = node.val >= max_val
        count = 1 if is_good else 0

        # Update the maximum value for the path
        max_val = max(max_val, node.val)

        # Recur for left and right subtrees
        count += dfs(node.left, max_val)
        count += dfs(node.right, max_val)

        return count

    return dfs(root, root.val) if root else 0