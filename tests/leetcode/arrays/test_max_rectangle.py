import pytest
from src.leetcode.arrays.max_rectangle import maximal_rectangle

def test_basic_case():
    """Test basic case from problem description."""
    matrix = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
    assert maximal_rectangle(matrix) == 6

def test_empty_matrix():
    """Test with empty matrix."""
    assert maximal_rectangle([]) == 0
    assert maximal_rectangle([[]]) == 0

def test_single_cell():
    """Test with single cell matrix."""
    assert maximal_rectangle([["1"]]) == 1
    assert maximal_rectangle([["0"]]) == 0

def test_all_ones():
    """Test with matrix of all ones."""
    matrix = [
        ["1","1","1"],
        ["1","1","1"],
        ["1","1","1"]
    ]
    assert maximal_rectangle(matrix) == 9

def test_all_zeros():
    """Test with matrix of all zeros."""
    matrix = [
        ["0","0","0"],
        ["0","0","0"],
        ["0","0","0"]
    ]
    assert maximal_rectangle(matrix) == 0

def test_single_row():
    """Test with single row matrix."""
    matrix = [["1","1","0","1","1","1"]]
    assert maximal_rectangle(matrix) == 3

def test_single_column():
    """Test with single column matrix."""
    matrix = [["1"],["1"],["0"],["1"]]
    assert maximal_rectangle(matrix) == 2

def test_alternating_pattern():
    """Test with alternating pattern of ones and zeros."""
    matrix = [
        ["1","0","1"],
        ["0","1","0"],
        ["1","0","1"]
    ]
    assert maximal_rectangle(matrix) == 1

def test_multiple_rectangles():
    """Test with multiple possible rectangles."""
    matrix = [
        ["1","1","1","1"],
        ["1","1","1","1"],
        ["0","0","1","1"]
    ]
    assert maximal_rectangle(matrix) == 8

def test_complex_shape():
    """Test with more complex shape."""
    matrix = [
        ["1","0","1","1","1"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["0","1","1","1","0"]
    ]
    assert maximal_rectangle(matrix) == 9