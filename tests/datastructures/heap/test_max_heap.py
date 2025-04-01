import pytest
from src.datastructures.heap.max_heap import MaxHeap

class TestMaxHeap:
    """Test class for MaxHeap implementation."""
    
    @pytest.fixture
    def empty_heap(self):
        """Fixture that provides an empty max heap."""
        return MaxHeap()
        
    @pytest.fixture
    def populated_heap(self):
        """Fixture that provides a populated max heap."""
        heap = MaxHeap()
        values = [4, 8, 2, 5, 1, 9, 3, 7, 6]
        for val in values:
            heap.insert(val)
        return heap
        
    def test_empty_heap(self, empty_heap):
        """Test operations on an empty heap."""
        assert empty_heap.is_empty()
        assert empty_heap.size() == 0
        assert empty_heap.get_max() is None
        assert empty_heap.extract_max() is None
        
    def test_insert(self, empty_heap):
        """Test insert operation and max heap property."""
        empty_heap.insert(3)
        assert empty_heap.get_max() == 3
        
        empty_heap.insert(5)
        assert empty_heap.get_max() == 5
        
        empty_heap.insert(4)
        assert empty_heap.get_max() == 5
        assert empty_heap.size() == 3
        
    def test_extract_max(self, populated_heap):
        """Test extract_max operation."""
        # The maximum values should come out in descending order
        assert populated_heap.extract_max() == 9
        assert populated_heap.extract_max() == 8
        assert populated_heap.extract_max() == 7
        assert populated_heap.extract_max() == 6
        assert populated_heap.extract_max() == 5
        assert populated_heap.extract_max() == 4
        assert populated_heap.extract_max() == 3
        assert populated_heap.extract_max() == 2
        assert populated_heap.extract_max() == 1
        assert populated_heap.extract_max() is None
        
    def test_heapify(self):
        """Test heapify operation."""
        arr = [4, 8, 2, 5, 1, 9, 3, 7, 6]
        heap = MaxHeap.heapify(arr)
        
        # Extract all elements - should come out in descending order
        sorted_values = []
        while not heap.is_empty():
            sorted_values.append(heap.extract_max())
            
        assert sorted_values == sorted(arr, reverse=True)
        
    def test_clear(self, populated_heap):
        """Test clear operation."""
        assert not populated_heap.is_empty()
        populated_heap.clear()
        assert populated_heap.is_empty()
        assert populated_heap.size() == 0
        assert populated_heap.get_max() is None
        
    def test_get_max(self, populated_heap):
        """Test get_max operation."""
        # get_max should return maximum without removing it
        max_val = populated_heap.get_max()
        assert max_val == 9
        assert populated_heap.get_max() == max_val  # Should still be there