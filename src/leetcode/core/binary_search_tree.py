# Implementation of a Binary Search Tree (BST) in Python
# Problem: Design a binary search tree that supports operations like insert, delete, and search.
# LeetCode Link: https://leetcode.com/problems/insert-into-a-binary-search-tree/

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        """Initialize the binary search tree."""
        self.root = None

    def insert(self, value):
        """Insert a value into the BST."""
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left:
                self._insert(node.left, value)
            else:
                node.left = TreeNode(value)
        else:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = TreeNode(value)

    def search(self, value):
        """Search for a value in the BST."""
        return self._search(self.root, value)

    def _search(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    def delete(self, value):
        """Delete a value from the BST."""
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if not node:
            return None
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            min_larger_node = self._get_min(node.right)
            node.value = min_larger_node.value
            node.right = self._delete(node.right, min_larger_node.value)
        return node

    def _get_min(self, node):
        while node.left:
            node = node.left
        return node

    def inorder(self):
        """Return an inorder traversal of the BST."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)