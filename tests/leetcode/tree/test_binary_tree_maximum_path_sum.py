"""
Test cases for the 'Binary Tree Maximum Path Sum' problem.
"""
import unittest
from src.leetcode.tree.binary_tree_maximum_path_sum import TreeNode, max_path_sum

class TestBinaryTreeMaximumPathSum(unittest.TestCase):
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

    def test_max_path_sum(self):
        # Test case 1: Example tree
        root = self.list_to_tree([1, 2, 3])
        self.assertEqual(max_path_sum(root), 6)

        # Test case 2: Tree with negative values
        root = self.list_to_tree([-10, 9, 20, None, None, 15, 7])
        self.assertEqual(max_path_sum(root), 42)

        # Test case 3: Single node tree
        root = self.list_to_tree([1])
        self.assertEqual(max_path_sum(root), 1)

        # Test case 4: Empty tree
        root = self.list_to_tree([])
        self.assertEqual(max_path_sum(root), float('-inf'))

        # Test case 5: Tree with all negative values
        root = self.list_to_tree([-3, -2, -1])
        self.assertEqual(max_path_sum(root), -1)

if __name__ == "__main__":
    unittest.main()