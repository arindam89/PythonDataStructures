"""
Test cases for the 'Subtree of Another Tree' problem.
"""
import unittest
from src.leetcode.tree.subtree_of_another_tree import TreeNode, is_subtree

class TestSubtreeOfAnotherTree(unittest.TestCase):
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

    def test_is_subtree(self):
        # Test case 1: Subtree exists
        root = self.list_to_tree([3, 4, 5, 1, 2])
        sub_root = self.list_to_tree([4, 1, 2])
        self.assertTrue(is_subtree(root, sub_root))

        # Test case 2: Subtree does not exist
        root = self.list_to_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
        sub_root = self.list_to_tree([4, 1, 2])
        self.assertFalse(is_subtree(root, sub_root))

        # Test case 3: Both trees are empty
        root = self.list_to_tree([])
        sub_root = self.list_to_tree([])
        self.assertTrue(is_subtree(root, sub_root))

        # Test case 4: Main tree is empty
        root = self.list_to_tree([])
        sub_root = self.list_to_tree([1])
        self.assertFalse(is_subtree(root, sub_root))

        # Test case 5: Subtree is empty
        root = self.list_to_tree([1])
        sub_root = self.list_to_tree([])
        self.assertTrue(is_subtree(root, sub_root))

if __name__ == "__main__":
    unittest.main()