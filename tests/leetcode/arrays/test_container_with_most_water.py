import pytest
from src.leetcode.arrays.container_with_most_water import max_area

def test_max_area_basic():
    """Test basic case."""
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert max_area(height) == 49  # Between lines at indices 1 and 8
    
def test_max_area_ascending():
    """Test with ascending heights."""
    height = [1, 2, 3, 4, 5]
    assert max_area(height) == 6  # Between lines at indices 0 and 4
    
def test_max_area_descending():
    """Test with descending heights."""
    height = [5, 4, 3, 2, 1]
    assert max_area(height) == 6  # Between lines at indices 0 and 4
    
def test_max_area_same_height():
    """Test with all lines of same height."""
    height = [4, 4, 4, 4]
    assert max_area(height) == 12  # Between first and last line
    
def test_max_area_minimum():
    """Test minimum possible area."""
    height = [1, 1]
    assert max_area(height) == 1
    
def test_max_area_single_tall():
    """Test with one tall line."""
    height = [1, 1, 10, 1, 1]
    assert max_area(height) == 4  # Between indices 0 and 4