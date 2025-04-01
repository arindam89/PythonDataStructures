import pytest
from src.datastructures.heap.min_heap import MinHeap

class TestMinHeap:
    """Test class for MinHeap implementation."""
    
    @pytest.fixture
    def empty_heap(self):
        """Fixture that provides an empty min heap."""
        return MinHeap()
        
    @pytest.fixture
    def populated_heap(self):
        """Fixture that provides a populated min heap."""
        heap = MinHeap()
        values = [4, 8, 2, 5, 1, 9, 3, 7, 6]
        for val in values:
            heap.insert(val)
        return heap
        
    def test_empty_heap(self, empty_heap):
        """Test operations on an empty heap."""
        assert empty_heap.is_empty()
        assert empty_heap.size() == 0
        assert empty_heap.get_min() is None
        assert empty_heap.extract_min() is None
        
    def test_insert(self, empty_heap):
        """Test insert operation and min heap property."""
        empty_heap.insert(3)
        assert empty_heap.get_min() == 3
        
        empty_heap.insert(1)
        assert empty_heap.get_min() == 1
        
        empty_heap.insert(2)
        assert empty_heap.get_min() == 1
        assert empty_heap.size() == 3
        
    def test_extract_min(self, populated_heap):
        """Test extract_min operation."""
        # The minimum values should come out in ascending order
        assert populated_heap.extract_min() == 1
        assert populated_heap.extract_min() == 2
        assert populated_heap.extract_min() == 3
        assert populated_heap.extract_min() == 4
        assert populated_heap.extract_min() == 5
        assert populated_heap.extract_min() == 6
        assert populated_heap.extract_min() == 7
        assert populated_heap.extract_min() == 8
        assert populated_heap.extract_min() == 9
        assert populated_heap.extract_min() is None
        
    def test_heapify(self):
        """Test heapify operation."""
        arr = [4, 8, 2, 5, 1, 9, 3, 7, 6]
        heap = MinHeap.heapify(arr)
        
        # Extract all elements - should come out in ascending order
        sorted_values = []
        while not heap.is_empty():
            sorted_values.append(heap.extract_min())
            
        assert sorted_values == sorted(arr)
        
    def test_clear(self, populated_heap):
        """Test clear operation."""
        assert not populated_heap.is_empty()
        populated_heap.clear()
        assert populated_heap.is_empty()
        assert populated_heap.size() == 0
        assert populated_heap.get_min() is None
        
    def test_get_min(self, populated_heap):
        """Test get_min operation."""
        # get_min should return minimum without removing it
        min_val = populated_heap.get_min()
        assert min_val == 1
        assert populated_heap.get_min() == min_val  # Should still be there