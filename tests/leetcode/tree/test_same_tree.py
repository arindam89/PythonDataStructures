"""
Test cases for the 'Same Tree' problem.
"""
import unittest
from src.leetcode.tree.same_tree import TreeNode, is_same_tree

class TestSameTree(unittest.TestCase):
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

    def test_is_same_tree(self):
        # Test case 1: Identical trees
        p = self.list_to_tree([1, 2, 3])
        q = self.list_to_tree([1, 2, 3])
        self.assertTrue(is_same_tree(p, q))

        # Test case 2: Different structure
        p = self.list_to_tree([1, 2])
        q = self.list_to_tree([1, None, 2])
        self.assertFalse(is_same_tree(p, q))

        # Test case 3: Different values
        p = self.list_to_tree([1, 2, 1])
        q = self.list_to_tree([1, 1, 2])
        self.assertFalse(is_same_tree(p, q))

        # Test case 4: Both trees are empty
        p = self.list_to_tree([])
        q = self.list_to_tree([])
        self.assertTrue(is_same_tree(p, q))

        # Test case 5: One tree is empty
        p = self.list_to_tree([1])
        q = self.list_to_tree([])
        self.assertFalse(is_same_tree(p, q))

if __name__ == "__main__":
    unittest.main()