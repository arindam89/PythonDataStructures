from typing import TypeVar, Generic, Optional, List, Callable
from ..tree.tree_node import TreeNode

T = TypeVar('T')

class BinarySearchTree(Generic[T]):
    """
    Implementation of a Binary Search Tree (BST).
    A BST is a binary tree where for each node, all elements in the left subtree
    are less than the node's value, and all elements in the right subtree are greater.
    
    Time Complexity:
    - Search: O(log n) average case, O(n) worst case (unbalanced tree)
    - Insert: O(log n) average case, O(n) worst case
    - Delete: O(log n) average case, O(n) worst case
    
    Space Complexity: O(n) for storage, O(h) for recursive operations (h is height)
    """
    
    def __init__(self):
        """Constructs an empty binary search tree."""
        self.root = None
        
    def insert(self, data: T) -> None:
        """
        Inserts an element into the tree.
        Time Complexity: O(log n) average case, O(n) worst case
        
        Args:
            data: The element to insert
        """
        self.root = self._insert(self.root, data)
        
    def _insert(self, node: Optional[TreeNode], data: T) -> TreeNode:
        """Helper method to recursively insert an element."""
        if node is None:
            return TreeNode(data)
            
        if data < node.val:
            node.left = self._insert(node.left, data)
        elif data > node.val:
            node.right = self._insert(node.right, data)
            
        return node
        
    def search(self, data: T) -> bool:
        """
        Searches for an element in the tree.
        Time Complexity: O(log n) average case, O(n) worst case
        
        Args:
            data: The element to search for
            
        Returns:
            True if the element is found, False otherwise
        """
        return self._search(self.root, data)
        
    def _search(self, node: Optional[TreeNode], data: T) -> bool:
        """Helper method to recursively search for an element."""
        if node is None:
            return False
            
        if data == node.val:
            return True
        elif data < node.val:
            return self._search(node.left, data)
        else:
            return self._search(node.right, data)
            
    def in_order_traversal(self) -> List[T]:
        """
        Performs an in-order traversal of the tree.
        In-order traversal visits left subtree, root, then right subtree.
        This produces a sorted sequence for a BST.
        
        Returns:
            A list containing the elements in sorted order
        """
        result = []
        self._in_order_traversal(self.root, result)
        return result
        
    def _in_order_traversal(self, node: Optional[TreeNode], result: List[T]) -> None:
        """Helper method for in-order traversal."""
        if node:
            self._in_order_traversal(node.left, result)
            result.append(node.val)
            self._in_order_traversal(node.right, result)
            
    def pre_order_traversal(self) -> List[T]:
        """
        Performs a pre-order traversal of the tree.
        Pre-order traversal visits root, then left subtree, then right subtree.
        
        Returns:
            A list containing the elements in pre-order
        """
        result = []
        self._pre_order_traversal(self.root, result)
        return result
        
    def _pre_order_traversal(self, node: Optional[TreeNode], result: List[T]) -> None:
        """Helper method for pre-order traversal."""
        if node:
            result.append(node.val)
            self._pre_order_traversal(node.left, result)
            self._pre_order_traversal(node.right, result)
            
    def post_order_traversal(self) -> List[T]:
        """
        Performs a post-order traversal of the tree.
        Post-order traversal visits left subtree, right subtree, then root.
        
        Returns:
            A list containing the elements in post-order
        """
        result = []
        self._post_order_traversal(self.root, result)
        return result
        
    def _post_order_traversal(self, node: Optional[TreeNode], result: List[T]) -> None:
        """Helper method for post-order traversal."""
        if node:
            self._post_order_traversal(node.left, result)
            self._post_order_traversal(node.right, result)
            result.append(node.val)
            
    def find_min(self) -> Optional[T]:
        """
        Finds the minimum element in the tree.
        Time Complexity: O(log n) average case, O(n) worst case
        
        Returns:
            The minimum element, or None if the tree is empty
        """
        if not self.root:
            return None
        return self._find_min(self.root).val
        
    def _find_min(self, node: TreeNode) -> TreeNode:
        """Helper method to find the node with minimum value."""
        current = node
        while current.left:
            current = current.left
        return current
        
    def find_max(self) -> Optional[T]:
        """
        Finds the maximum element in the tree.
        Time Complexity: O(log n) average case, O(n) worst case
        
        Returns:
            The maximum element, or None if the tree is empty
        """
        if not self.root:
            return None
        return self._find_max(self.root).val
        
    def _find_max(self, node: TreeNode) -> TreeNode:
        """Helper method to find the node with maximum value."""
        current = node
        while current.right:
            current = current.right
        return current
        
    def delete(self, data: T) -> None:
        """
        Deletes an element from the tree.
        Time Complexity: O(log n) average case, O(n) worst case
        
        Args:
            data: The element to delete
        """
        self.root = self._delete(self.root, data)
        
    def _delete(self, node: Optional[TreeNode], data: T) -> Optional[TreeNode]:
        """Helper method to recursively delete an element."""
        if not node:
            return None
            
        if data < node.val:
            node.left = self._delete(node.left, data)
        elif data > node.val:
            node.right = self._delete(node.right, data)
        else:
            # Node to delete found
            
            # Case 1: Leaf node or node with only one child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
                
            # Case 2: Node with two children
            # Find the inorder successor (smallest element in right subtree)
            successor = self._find_min(node.right)
            node.val = successor.val
            # Delete the successor
            node.right = self._delete(node.right, successor.val)
            
        return node
        
    def successor(self, data: T) -> Optional[T]:
        """
        Finds the successor of a given element (next larger element).
        Time Complexity: O(log n) average case, O(n) worst case
        
        Args:
            data: The element to find successor for
            
        Returns:
            The successor element, or None if no successor exists
        """
        # Find the node first
        node = self.root
        successor = None
        
        while node:
            if data < node.val:
                successor = node
                node = node.left
            elif data > node.val:
                node = node.right
            else:
                if node.right:
                    successor = self._find_min(node.right)
                break
                
        return successor.val if successor else None
        
    def predecessor(self, data: T) -> Optional[T]:
        """
        Finds the predecessor of a given element (next smaller element).
        Time Complexity: O(log n) average case, O(n) worst case
        
        Args:
            data: The element to find predecessor for
            
        Returns:
            The predecessor element, or None if no predecessor exists
        """
        # Find the node first
        node = self.root
        predecessor = None
        
        while node:
            if data > node.val:
                predecessor = node
                node = node.right
            elif data < node.val:
                node = node.left
            else:
                if node.left:
                    predecessor = self._find_max(node.left)
                break
                
        return predecessor.val if predecessor else None
        
    def is_valid_bst(self) -> bool:
        """
        Checks if the tree is a valid binary search tree.
        A valid BST has all left subtree elements less than the node
        and all right subtree elements greater than the node.
        
        Returns:
            True if the tree is a valid BST, False otherwise
        """
        def is_valid(node: Optional[TreeNode], min_val: Optional[T], max_val: Optional[T]) -> bool:
            if not node:
                return True
                
            if (min_val is not None and node.val <= min_val) or \
               (max_val is not None and node.val >= max_val):
                return False
                
            return is_valid(node.left, min_val, node.val) and \
                   is_valid(node.right, node.val, max_val)
                   
        return is_valid(self.root, None, None)
        
    def level_order_traversal(self) -> List[T]:
        """
        Performs a level-order (breadth-first) traversal of the tree.
        Time Complexity: O(n)
        
        Returns:
            A list containing the elements in level-order
        """
        if not self.root:
            return []
            
        result = []
        queue = [self.root]
        
        while queue:
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return result