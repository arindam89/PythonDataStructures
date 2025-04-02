"""
Test cases for the 'Binary Tree Right Side View' problem.
"""
import unittest
from src.leetcode.tree.binary_tree_right_side_view import TreeNode, right_side_view

class TestBinaryTreeRightSideView(unittest.TestCase):
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

    def test_right_side_view(self):
        # Test case 1: Example tree
        root = self.list_to_tree([1, 2, 3, None, 5, None, 4])
        self.assertEqual(right_side_view(root), [1, 3, 4])

        # Test case 2: Single node tree
        root = self.list_to_tree([1])
        self.assertEqual(right_side_view(root), [1])

        # Test case 3: Empty tree
        root = self.list_to_tree([])
        self.assertEqual(right_side_view(root), [])

        # Test case 4: Tree with only left children
        root = self.list_to_tree([1, 2, None, 3])
        self.assertEqual(right_side_view(root), [1, 2, 3])

        # Test case 5: Tree with only right children
        root = self.list_to_tree([1, None, 2, None, 3])
        self.assertEqual(right_side_view(root), [1, 2, 3])

if __name__ == "__main__":
    unittest.main()