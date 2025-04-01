import pytest
from src.datastructures.linkedlist.linked_list import LinkedList

class TestLinkedList:
    """Test class for LinkedList implementation."""
    
    @pytest.fixture
    def empty_list(self):
        """Fixture that provides an empty linked list."""
        return LinkedList()
        
    @pytest.fixture
    def populated_list(self):
        """Fixture that provides a populated linked list."""
        lst = LinkedList()
        values = [1, 2, 3, 4, 5]
        for val in values:
            lst.append(val)
        return lst
        
    def test_empty_list(self, empty_list):
        """Test operations on an empty list."""
        assert len(empty_list) == 0
        assert empty_list.get(0) is None
        assert empty_list.index_of(1) == -1
        assert not empty_list.delete_at(0)
        assert not empty_list.delete_value(1)
        assert empty_list.to_list() == []
        
    def test_append(self, empty_list):
        """Test append operation."""
        empty_list.append(1)
        assert len(empty_list) == 1
        assert empty_list.get(0) == 1
        
        empty_list.append(2)
        assert len(empty_list) == 2
        assert empty_list.get(1) == 2
        
    def test_prepend(self, empty_list):
        """Test prepend operation."""
        empty_list.prepend(1)
        assert len(empty_list) == 1
        assert empty_list.get(0) == 1
        
        empty_list.prepend(2)
        assert len(empty_list) == 2
        assert empty_list.get(0) == 2
        assert empty_list.get(1) == 1
        
    def test_insert_at(self, populated_list):
        """Test insert_at operation."""
        # Insert at beginning
        assert populated_list.insert_at(0, 0)
        assert populated_list.get(0) == 0
        
        # Insert in middle
        assert populated_list.insert_at(3, 10)
        assert populated_list.get(3) == 10
        
        # Insert at end
        assert populated_list.insert_at(len(populated_list), 6)
        assert populated_list.get(len(populated_list) - 1) == 6
        
        # Invalid index
        assert not populated_list.insert_at(-1, 0)
        assert not populated_list.insert_at(len(populated_list) + 1, 0)
        
    def test_delete_at(self, populated_list):
        """Test delete_at operation."""
        initial_size = len(populated_list)
        
        # Delete from beginning
        assert populated_list.delete_at(0)
        assert len(populated_list) == initial_size - 1
        assert populated_list.get(0) == 2
        
        # Delete from middle
        assert populated_list.delete_at(1)
        assert populated_list.get(1) == 4
        
        # Delete from end
        assert populated_list.delete_at(len(populated_list) - 1)
        
        # Invalid index
        assert not populated_list.delete_at(-1)
        assert not populated_list.delete_at(len(populated_list))
        
    def test_delete_value(self, populated_list):
        """Test delete_value operation."""
        initial_size = len(populated_list)
        
        # Delete existing value
        assert populated_list.delete_value(3)
        assert len(populated_list) == initial_size - 1
        assert populated_list.index_of(3) == -1
        
        # Delete non-existing value
        assert not populated_list.delete_value(10)
        assert len(populated_list) == initial_size - 1
        
        # Delete first value
        assert populated_list.delete_value(1)
        assert populated_list.get(0) == 2
        
        # Delete last value
        assert populated_list.delete_value(5)
        
    def test_get(self, populated_list):
        """Test get operation."""
        assert populated_list.get(0) == 1
        assert populated_list.get(2) == 3
        assert populated_list.get(4) == 5
        assert populated_list.get(-1) is None
        assert populated_list.get(5) is None
        
    def test_index_of(self, populated_list):
        """Test index_of operation."""
        assert populated_list.index_of(1) == 0
        assert populated_list.index_of(3) == 2
        assert populated_list.index_of(5) == 4
        assert populated_list.index_of(6) == -1
        
    def test_clear(self, populated_list):
        """Test clear operation."""
        assert len(populated_list) > 0
        populated_list.clear()
        assert len(populated_list) == 0
        assert populated_list.to_list() == []
        
    def test_to_list(self, populated_list):
        """Test to_list operation."""
        assert populated_list.to_list() == [1, 2, 3, 4, 5]
        
    def test_reverse(self, populated_list):
        """Test reverse operation."""
        original = populated_list.to_list()
        populated_list.reverse()
        assert populated_list.to_list() == original[::-1]
        
    def test_iteration(self, populated_list):
        """Test iteration over the list."""
        values = []
        for val in populated_list:
            values.append(val)
        assert values == populated_list.to_list()
        
    def test_equality(self, populated_list):
        """Test equality comparison."""
        other_list = LinkedList()
        for val in [1, 2, 3, 4, 5]:
            other_list.append(val)
            
        assert populated_list == other_list
        other_list.append(6)
        assert populated_list != other_list