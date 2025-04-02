"""
Test cases for the 'Construct Binary Tree from Preorder and Inorder Traversal' problem.
"""
import unittest
from src.leetcode.tree.construct_binary_tree_from_preorder_inorder import TreeNode, build_tree

class TestConstructBinaryTreeFromPreorderInorder(unittest.TestCase):
    def tree_to_list(self, root):
        """Helper function to convert a binary tree to a list (level-order traversal)."""
        if not root:
            return []

        result, queue = [], [root]
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        # Remove trailing None values
        while result and result[-1] is None:
            result.pop()

        return result

    def test_build_tree(self):
        # Test case 1: Example tree
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        root = build_tree(preorder, inorder)
        self.assertEqual(self.tree_to_list(root), [3, 9, 20, None, None, 15, 7])

        # Test case 2: Single node tree
        preorder = [1]
        inorder = [1]
        root = build_tree(preorder, inorder)
        self.assertEqual(self.tree_to_list(root), [1])

        # Test case 3: Empty tree
        preorder = []
        inorder = []
        root = build_tree(preorder, inorder)
        self.assertEqual(self.tree_to_list(root), [])

        # Test case 4: Tree with only left children
        preorder = [1, 2, 3]
        inorder = [3, 2, 1]
        root = build_tree(preorder, inorder)
        self.assertEqual(self.tree_to_list(root), [1, 2, None, 3])

        # Test case 5: Tree with only right children
        preorder = [1, 2, 3]
        inorder = [1, 2, 3]
        root = build_tree(preorder, inorder)
        self.assertEqual(self.tree_to_list(root), [1, None, 2, None, 3])

if __name__ == "__main__":
    unittest.main()