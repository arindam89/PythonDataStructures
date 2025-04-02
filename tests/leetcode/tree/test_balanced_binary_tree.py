"""
Test cases for the 'Balanced Binary Tree' problem.
"""
import unittest
from src.leetcode.tree.balanced_binary_tree import TreeNode, is_balanced

class TestBalancedBinaryTree(unittest.TestCase):
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

    def test_is_balanced(self):
        # Test case 1: Balanced tree
        root = self.list_to_tree([3, 9, 20, None, None, 15, 7])
        self.assertTrue(is_balanced(root))

        # Test case 2: Unbalanced tree
        root = self.list_to_tree([1, 2, 2, 3, 3, None, None, 4, 4])
        self.assertFalse(is_balanced(root))

        # Test case 3: Single node tree
        root = self.list_to_tree([1])
        self.assertTrue(is_balanced(root))

        # Test case 4: Empty tree
        root = self.list_to_tree([])
        self.assertTrue(is_balanced(root))

        # Test case 5: Tree with only left children
        root = self.list_to_tree([1, 2, None, 3, None, None, None])
        self.assertFalse(is_balanced(root))

if __name__ == "__main__":
    unittest.main()