import pytest
from src.datastructures.tree.binary_tree import BinaryTree

def test_binary_tree_insert():
    tree = BinaryTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    assert tree.root.val == 1
    assert tree.root.left.val == 2
    assert tree.root.right.val == 3

def test_binary_tree_level_order_traversal():
    tree = BinaryTree()
    values = [1, 2, 3, 4, 5]
    for val in values:
        tree.insert(val)
    
    result = tree.level_order_traversal()
    assert result == values

def test_empty_tree():
    tree = BinaryTree()
    assert tree.level_order_traversal() == []