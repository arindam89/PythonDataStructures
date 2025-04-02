"""
Test cases for the 'Kth Smallest Element in a BST' problem.
"""
import unittest
from src.leetcode.tree.kth_smallest_element_in_bst import TreeNode, kth_smallest

class TestKthSmallestElementInBST(unittest.TestCase):
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

    def test_kth_smallest(self):
        # Test case 1: Example tree
        root = self.list_to_tree([3, 1, 4, None, 2])
        self.assertEqual(kth_smallest(root, 1), 1)
        self.assertEqual(kth_smallest(root, 2), 2)
        self.assertEqual(kth_smallest(root, 3), 3)
        self.assertEqual(kth_smallest(root, 4), 4)

        # Test case 2: Single node tree
        root = self.list_to_tree([1])
        self.assertEqual(kth_smallest(root, 1), 1)

        # Test case 3: Tree with duplicate values
        root = self.list_to_tree([2, 2, 2])
        self.assertEqual(kth_smallest(root, 1), 2)
        self.assertEqual(kth_smallest(root, 2), 2)
        self.assertEqual(kth_smallest(root, 3), 2)

if __name__ == "__main__":
    unittest.main()