"""
Test cases for the 'Lowest Common Ancestor of a Binary Search Tree' problem.
"""
import unittest
from src.leetcode.tree.lowest_common_ancestor_bst import TreeNode, lowest_common_ancestor

class TestLowestCommonAncestorBST(unittest.TestCase):
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

    def find_node(self, root, val):
        """Helper function to find a node with a given value in the tree."""
        if not root or root.val == val:
            return root
        left = self.find_node(root.left, val)
        return left if left else self.find_node(root.right, val)

    def test_lowest_common_ancestor(self):
        # Test case 1: Example tree
        root = self.list_to_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = self.find_node(root, 2)
        q = self.find_node(root, 8)
        self.assertEqual(lowest_common_ancestor(root, p, q).val, 6)

        # Test case 2: LCA is one of the nodes
        p = self.find_node(root, 2)
        q = self.find_node(root, 4)
        self.assertEqual(lowest_common_ancestor(root, p, q).val, 2)

        # Test case 3: Both nodes are in the left subtree
        p = self.find_node(root, 0)
        q = self.find_node(root, 5)
        self.assertEqual(lowest_common_ancestor(root, p, q).val, 2)

        # Test case 4: Both nodes are in the right subtree
        p = self.find_node(root, 7)
        q = self.find_node(root, 9)
        self.assertEqual(lowest_common_ancestor(root, p, q).val, 8)

        # Test case 5: Tree with only one node
        root = self.list_to_tree([1])
        p = self.find_node(root, 1)
        q = self.find_node(root, 1)
        self.assertEqual(lowest_common_ancestor(root, p, q).val, 1)

if __name__ == "__main__":
    unittest.main()