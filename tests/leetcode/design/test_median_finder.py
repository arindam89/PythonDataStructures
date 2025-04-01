import pytest
from src.leetcode.design.median_finder import MedianFinder

def test_basic_operations():
    """Test basic add and find operations."""
    finder = MedianFinder()
    finder.addNum(1)
    assert finder.findMedian() == 1.0
    finder.addNum(2)
    assert finder.findMedian() == 1.5
    finder.addNum(3)
    assert finder.findMedian() == 2.0
    
def test_odd_number_of_elements():
    """Test with odd number of elements."""
    finder = MedianFinder()
    nums = [2, 1, 5, 7, 4]
    for num in nums:
        finder.addNum(num)
    assert finder.findMedian() == 4.0
    
def test_even_number_of_elements():
    """Test with even number of elements."""
    finder = MedianFinder()
    nums = [2, 1, 5, 7]
    for num in nums:
        finder.addNum(num)
    assert finder.findMedian() == 3.5
    
def test_duplicate_numbers():
    """Test with duplicate numbers."""
    finder = MedianFinder()
    nums = [1, 2, 2, 3]
    for num in nums:
        finder.addNum(num)
    assert finder.findMedian() == 2.0
    
def test_negative_numbers():
    """Test with negative numbers."""
    finder = MedianFinder()
    nums = [-5, -2, 0, 1, 3]
    for num in nums:
        finder.addNum(num)
    assert finder.findMedian() == 0.0
    
def test_count():
    """Test element count."""
    finder = MedianFinder()
    assert finder.getCount() == 0
    finder.addNum(1)
    assert finder.getCount() == 1
    finder.addNum(2)
    assert finder.getCount() == 2
    
def test_clear():
    """Test clearing all elements."""
    finder = MedianFinder()
    nums = [1, 2, 3, 4, 5]
    for num in nums:
        finder.addNum(num)
    assert finder.getCount() > 0
    finder.clear()
    assert finder.getCount() == 0
    
def test_large_numbers():
    """Test with large numbers."""
    finder = MedianFinder()
    nums = [1000000, -1000000, 0, 999999, -999999]
    for num in nums:
        finder.addNum(num)
    assert finder.findMedian() == 0.0
    
def test_alternating_order():
    """Test adding numbers in alternating high-low order."""
    finder = MedianFinder()
    nums = [5, 1, 4, 2, 3]  # Will test heap balancing
    for num in nums:
        finder.addNum(num)
    assert finder.findMedian() == 3.0
    
def test_sorted_order():
    """Test adding numbers in sorted order."""
    finder = MedianFinder()
    nums = [1, 2, 3, 4, 5]
    for num in nums:
        finder.addNum(num)
    assert finder.findMedian() == 3.0