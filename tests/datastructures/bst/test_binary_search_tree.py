import pytest
from src.datastructures.bst.binary_search_tree import BinarySearchTree

class TestBinarySearchTree:
    """Test class for BinarySearchTree implementation."""
    
    @pytest.fixture
    def bst(self):
        """Fixture to create a fresh BST for each test."""
        return BinarySearchTree()
        
    def test_empty_bst(self, bst):
        """Test operations on an empty BST."""
        assert bst.root is None
        assert bst.find_min() is None
        assert bst.find_max() is None
        assert bst.level_order_traversal() == []
        assert bst.is_valid_bst()
        
    def test_insert(self, bst):
        """Test insert operation and resulting tree structure."""
        bst.insert(50)
        assert bst.root.val == 50
        assert bst.find_min() == 50
        assert bst.find_max() == 50
        
        bst.insert(30)
        bst.insert(70)
        assert bst.find_min() == 30
        assert bst.find_max() == 70
        
        bst.insert(20)
        bst.insert(40)
        bst.insert(60)
        bst.insert(80)
        
        assert bst.find_min() == 20
        assert bst.find_max() == 80
        assert bst.is_valid_bst()
        
    def test_search(self, bst):
        """Test search operation."""
        assert not bst.search(50)
        
        values = [50, 30, 70, 20, 40, 60, 80]
        for val in values:
            bst.insert(val)
            
        for val in values:
            assert bst.search(val)
            
        assert not bst.search(10)
        assert not bst.search(90)
        
    def test_delete(self, bst):
        """Test deletion operation for different cases."""
        values = [50, 30, 70, 20, 40, 60, 80]
        for val in values:
            bst.insert(val)
            
        # Delete leaf node
        bst.delete(20)
        assert not bst.search(20)
        assert bst.is_valid_bst()
        
        # Delete node with one child
        bst.delete(60)
        assert not bst.search(60)
        assert bst.is_valid_bst()
        
        # Delete node with two children
        bst.delete(30)
        assert not bst.search(30)
        assert bst.is_valid_bst()
        
        # Delete root
        bst.delete(50)
        assert not bst.search(50)
        assert bst.is_valid_bst()
        
    def test_traversals(self, bst):
        """Test all traversal methods."""
        values = [50, 30, 70, 20, 40, 60, 80]
        for val in values:
            bst.insert(val)
            
        assert bst.in_order_traversal() == [20, 30, 40, 50, 60, 70, 80]
        assert bst.pre_order_traversal() == [50, 30, 20, 40, 70, 60, 80]
        assert bst.post_order_traversal() == [20, 40, 30, 60, 80, 70, 50]
        assert bst.level_order_traversal() == [50, 30, 70, 20, 40, 60, 80]
        
    def test_successor_predecessor(self, bst):
        """Test successor and predecessor operations."""
        values = [50, 30, 70, 20, 40, 60, 80]
        for val in values:
            bst.insert(val)
            
        # Test successors
        assert bst.successor(20) == 30
        assert bst.successor(30) == 40
        assert bst.successor(40) == 50
        assert bst.successor(50) == 60
        assert bst.successor(60) == 70
        assert bst.successor(70) == 80
        assert bst.successor(80) is None
        
        # Test predecessors
        assert bst.predecessor(20) is None
        assert bst.predecessor(30) == 20
        assert bst.predecessor(40) == 30
        assert bst.predecessor(50) == 40
        assert bst.predecessor(60) == 50
        assert bst.predecessor(70) == 60
        assert bst.predecessor(80) == 70