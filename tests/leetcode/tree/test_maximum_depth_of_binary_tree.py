"""
Test cases for the 'Maximum Depth of Binary Tree' problem.
"""
import unittest
from src.leetcode.tree.maximum_depth_of_binary_tree import TreeNode, max_depth

class TestMaximumDepthOfBinaryTree(unittest.TestCase):
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

    def test_max_depth(self):
        # Test case 1: Example tree
        root = self.list_to_tree([3, 9, 20, None, None, 15, 7])
        self.assertEqual(max_depth(root), 3)

        # Test case 2: Single node tree
        root = self.list_to_tree([1])
        self.assertEqual(max_depth(root), 1)

        # Test case 3: Empty tree
        root = self.list_to_tree([])
        self.assertEqual(max_depth(root), 0)

        # Test case 4: Tree with only left children
        root = self.list_to_tree([1, 2, None, 3, None, None, None])
        self.assertEqual(max_depth(root), 3)

        # Test case 5: Tree with only right children
        root = self.list_to_tree([1, None, 2, None, 3])
        self.assertEqual(max_depth(root), 3)

if __name__ == "__main__":
    unittest.main()