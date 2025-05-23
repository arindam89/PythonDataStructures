"""
Implementation of a Min Heap data structure.
A Min Heap is a complete binary tree where each node is smaller than its children.
"""

from typing import List, Optional

class MinHeap:
    """
    MinHeap implementation using a list as the underlying data structure.
    The root element (minimum) is always at index 0.
    For any element at index i:
    - Left child is at index 2i + 1
    - Right child is at index 2i + 2
    - Parent is at index (i - 1) // 2
    
    Time Complexity:
    - Insert: O(log n)
    - Extract Min: O(log n)
    - Get Min: O(1)
    - Heapify: O(n)
    
    Space Complexity: O(n) for storage
    """
    
    def __init__(self):
        """Initialize an empty min heap."""
        self.heap: List[int] = []
        
    def parent(self, index: int) -> int:
        """Returns the parent index of the element at given index."""
        return (index - 1) // 2
        
    def left_child(self, index: int) -> int:
        """Returns the left child index of the element at given index."""
        return 2 * index + 1
        
    def right_child(self, index: int) -> int:
        """Returns the right child index of the element at given index."""
        return 2 * index + 2
        
    def swap(self, i: int, j: int) -> None:
        """Swaps elements at indices i and j."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def insert(self, key: int) -> None:
        """
        Inserts a new key into the min heap.
        Time Complexity: O(log n)
        
        Args:
            key: The key to insert
        """
        self.heap.append(key)
        self._sift_up(len(self.heap) - 1)
        
    def _sift_up(self, index: int) -> None:
        """
        Moves the element at given index up to its correct position.
        Time Complexity: O(log n)
        """
        parent = self.parent(index)
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.swap(index, parent)
            self._sift_up(parent)
            
    def extract_min(self) -> Optional[int]:
        """
        Removes and returns the minimum element from the heap.
        Time Complexity: O(log n)
        
        Returns:
            The minimum element, or None if heap is empty
        """
        if not self.heap:
            return None
            
        if len(self.heap) == 1:
            return self.heap.pop()
            
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        
        return min_val
        
    def _sift_down(self, index: int) -> None:
        """
        Moves the element at given index down to its correct position.
        Time Complexity: O(log n)
        """
        min_index = index
        left = self.left_child(index)
        right = self.right_child(index)
        
        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left
            
        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right
            
        if index != min_index:
            self.swap(index, min_index)
            self._sift_down(min_index)
            
    def get_min(self) -> Optional[int]:
        """
        Returns the minimum element without removing it.
        Time Complexity: O(1)
        
        Returns:
            The minimum element, or None if heap is empty
        """
        return self.heap[0] if self.heap else None
        
    @staticmethod
    def heapify(arr: List[int]) -> 'MinHeap':
        """
        Creates a min heap from an array.
        Time Complexity: O(n)
        
        Args:
            arr: The array to heapify
            
        Returns:
            A new MinHeap containing the elements from the array
        """
        heap = MinHeap()
        heap.heap = arr.copy()
        
        # Start from last non-leaf node and sift down
        for i in range(len(arr) // 2 - 1, -1, -1):
            heap._sift_down(i)
            
        return heap
        
    def is_empty(self) -> bool:
        """Returns True if the heap is empty, False otherwise."""
        return len(self.heap) == 0
        
    def size(self) -> int:
        """Returns the number of elements in the heap."""
        return len(self.heap)
        
    def clear(self) -> None:
        """Removes all elements from the heap."""
        self.heap = []