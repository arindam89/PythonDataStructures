from typing import Optional, List
from .tree_node import TreeNode

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val: int) -> None:
        if not self.root:
            self.root = TreeNode(val)
            return
            
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if not node.left:
                node.left = TreeNode(val)
                return
            if not node.right:
                node.right = TreeNode(val)
                return
            queue.append(node.left)
            queue.append(node.right)
    
    def level_order_traversal(self) -> List[int]:
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