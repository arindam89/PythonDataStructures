"""
LeetCode 297: Serialize and Deserialize Binary Tree
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Design an algorithm to serialize and deserialize a binary tree. There is no
restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and
this string can be deserialized to the original tree structure.

Time Complexity: O(n) for both operations
Space Complexity: O(n) for both operations
"""

from typing import Optional, List
from src.datastructures.tree.tree_node import TreeNode

class Codec:
    """
    Codec to serialize and deserialize binary trees.
    Uses preorder traversal with null markers for serialization.
    """
    
    def serialize(self, root: Optional[TreeNode]) -> str:
        """
        Serialize a binary tree to a string.
        Uses preorder traversal (root -> left -> right).
        Null nodes are represented by 'null'.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            String representation of the tree
        """
        if not root:
            return "null"
            
        # Use preorder traversal: root,left,right
        return (f"{root.val}," + 
                self.serialize(root.left) + "," +
                self.serialize(root.right))
                
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """
        Deserialize a string to a binary tree.
        
        Args:
            data: String representation of the tree
            
        Returns:
            Root node of the reconstructed tree
        """
        def dfs() -> Optional[TreeNode]:
            """Helper function to build tree using DFS."""
            val = next(values)
            if val == "null":
                return None
                
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
            
        values = iter(data.split(","))
        return dfs()
        
    def deserialize_list(self, data: List[str]) -> Optional[TreeNode]:
        """
        Alternative deserialization that takes a list of strings.
        Useful for testing without string split operations.
        
        Args:
            data: List of string values representing the tree
            
        Returns:
            Root node of the reconstructed tree
        """
        def dfs() -> Optional[TreeNode]:
            """Helper function to build tree using DFS."""
            if not data:
                return None
                
            val = data.pop(0)
            if val == "null":
                return None
                
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
            
        return dfs()