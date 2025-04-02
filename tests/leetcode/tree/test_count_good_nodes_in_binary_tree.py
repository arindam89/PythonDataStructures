"""
Test cases for the 'Count Good Nodes in Binary Tree' problem.
"""
import unittest
from src.leetcode.tree.count_good_nodes_in_binary_tree import TreeNode, good_nodes

class TestCountGoodNodesInBinaryTree(unittest.TestCase):
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

    def test_good_nodes(self):
        # Test case 1: Example tree
        root = self.list_to_tree([3, 1, 4, 3, None, 1, 5])
        self.assertEqual(good_nodes(root), 4)

        # Test case 2: Single node tree
        root = self.list_to_tree([1])
        self.assertEqual(good_nodes(root), 1)

        # Test case 3: Empty tree
        root = self.list_to_tree([])
        self.assertEqual(good_nodes(root), 0)

        # Test case 4: Tree with increasing values
        root = self.list_to_tree([1, 2, 3, 4, 5])
        self.assertEqual(good_nodes(root), 5)

        # Test case 5: Tree with decreasing values
        root = self.list_to_tree([5, 4, 3, 2, 1])
        self.assertEqual(good_nodes(root), 1)

if __name__ == "__main__":
    unittest.main()