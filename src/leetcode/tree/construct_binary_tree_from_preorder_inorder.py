"""
Problem: Construct Binary Tree from Preorder and Inorder Traversal
Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Approach:
- Use the preorder traversal to determine the root of the tree.
- Use the inorder traversal to determine the left and right subtrees.
- Recursively construct the left and right subtrees using the respective segments of the preorder and inorder lists.
- Use a hashmap to store the indices of values in the inorder list for quick lookup.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    # Create a hashmap to store the index of each value in the inorder list
    inorder_index_map = {val: idx for idx, val in enumerate(inorder)}

    def array_to_tree(pre_left, pre_right, in_left, in_right):
        if pre_left > pre_right or in_left > in_right:
            return None

        # The first element in the preorder list is the root
        root_val = preorder[pre_left]
        root = TreeNode(root_val)

        # Find the index of the root in the inorder list
        root_index = inorder_index_map[root_val]

        # Calculate the size of the left subtree
        left_subtree_size = root_index - in_left

        # Recursively build the left and right subtrees
        root.left = array_to_tree(pre_left + 1, pre_left + left_subtree_size, in_left, root_index - 1)
        root.right = array_to_tree(pre_left + left_subtree_size + 1, pre_right, root_index + 1, in_right)

        return root

    return array_to_tree(0, len(preorder) - 1, 0, len(inorder) - 1)