"""
Test cases for the 'Validate Binary Search Tree' problem.
"""
import unittest
from src.leetcode.tree.validate_binary_search_tree import TreeNode, is_valid_bst

class TestValidateBinarySearchTree(unittest.TestCase):
    def list_to_tree(self, values):
        """Helper function to convert a list to a binary tree."""
        if not values:
            return None

        root = TreeNode(values[0])
        queue = [root]
        i = 1
        while queue and i < len(values):
            node = queue.pop(0)
            if node:
                if i < len(values) and values[i] is not None:
                    node.left = TreeNode(values[i])
                    queue.append(node.left)
                i += 1
                if i < len(values) and values[i] is not None:
                    node.right = TreeNode(values[i])
                    queue.append(node.right)
                i += 1

        return root

    def test_is_valid_bst(self):
        # Test case 1: Valid BST
        root = self.list_to_tree([2, 1, 3])
        self.assertTrue(is_valid_bst(root))

        # Test case 2: Invalid BST
        root = self.list_to_tree([5, 1, 4, None, None, 3, 6])
        self.assertFalse(is_valid_bst(root))

        # Test case 3: Single node tree
        root = self.list_to_tree([1])
        self.assertTrue(is_valid_bst(root))

        # Test case 4: Empty tree
        root = self.list_to_tree([])
        self.assertTrue(is_valid_bst(root))

        # Test case 5: Tree with duplicate values
        root = self.list_to_tree([2, 2, 2])
        self.assertFalse(is_valid_bst(root))

if __name__ == "__main__":
    unittest.main()