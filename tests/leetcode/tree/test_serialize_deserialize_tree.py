import pytest
from src.leetcode.tree.serialize_deserialize_tree import Codec
from src.datastructures.tree.tree_node import TreeNode

def assert_trees_equal(t1: TreeNode, t2: TreeNode) -> bool:
    """Helper function to check if two trees are structurally identical."""
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    return (t1.val == t2.val and 
            assert_trees_equal(t1.left, t2.left) and 
            assert_trees_equal(t1.right, t2.right))

def test_empty_tree():
    """Test serialization/deserialization of empty tree."""
    codec = Codec()
    assert codec.deserialize(codec.serialize(None)) is None
    
def test_single_node():
    """Test with single node tree."""
    codec = Codec()
    root = TreeNode(1)
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    assert assert_trees_equal(root, deserialized)
    
def test_full_binary_tree():
    """Test with a complete binary tree."""
    codec = Codec()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    assert assert_trees_equal(root, deserialized)
    
def test_unbalanced_tree():
    """Test with an unbalanced tree."""
    codec = Codec()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    assert assert_trees_equal(root, deserialized)
    
def test_right_skewed_tree():
    """Test with a right-skewed tree."""
    codec = Codec()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    assert assert_trees_equal(root, deserialized)
    
def test_negative_values():
    """Test with negative values in tree."""
    codec = Codec()
    root = TreeNode(-1)
    root.left = TreeNode(-2)
    root.right = TreeNode(-3)
    
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    assert assert_trees_equal(root, deserialized)
    
def test_list_deserialization():
    """Test the alternative list deserialization method."""
    codec = Codec()
    data = ["1", "2", "null", "null", "3", "null", "null"]
    root = codec.deserialize_list(data.copy())
    
    # Verify the structure
    assert root.val == 1
    assert root.left.val == 2
    assert root.right.val == 3
    assert root.left.left is None
    assert root.left.right is None
    assert root.right.left is None
    assert root.right.right is None
    
def test_complex_tree():
    """Test with a more complex tree structure."""
    codec = Codec()
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)
    
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    assert assert_trees_equal(root, deserialized)