"""
Test cases for the 'Invert Binary Tree' problem.
"""
import unittest
from src.leetcode.tree.invert_binary_tree import TreeNode, invert_tree

class TestInvertBinaryTree(unittest.TestCase):
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

    def test_invert_tree(self):
        # Test case 1: Example tree
        root = self.list_to_tree([4, 2, 7, 1, 3, 6, 9])
        inverted = invert_tree(root)
        self.assertEqual(self.tree_to_list(inverted), [4, 7, 2, 9, 6, 3, 1])

        # Test case 2: Single node tree
        root = self.list_to_tree([1])
        inverted = invert_tree(root)
        self.assertEqual(self.tree_to_list(inverted), [1])

        # Test case 3: Empty tree
        root = self.list_to_tree([])
        inverted = invert_tree(root)
        self.assertEqual(self.tree_to_list(inverted), [])

        # Test case 4: Tree with only left children
        root = self.list_to_tree([1, 2, None, 3])
        inverted = invert_tree(root)
        self.assertEqual(self.tree_to_list(inverted), [1, None, 2, None, 3])

        # Test case 5: Tree with only right children
        root = self.list_to_tree([1, None, 2, None, None, None, 3])
        inverted = invert_tree(root)
        self.assertEqual(self.tree_to_list(inverted), [1, 2, None, 3])

if __name__ == "__main__":
    unittest.main()