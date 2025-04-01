import pytest
from src.leetcode.graph.number_of_islands import num_islands

def test_basic_case():
    """Test basic case with multiple islands."""
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    assert num_islands(grid) == 3

def test_single_island():
    """Test with a single large island."""
    grid = [
        ["1","1","1"],
        ["1","1","1"],
        ["1","1","1"]
    ]
    assert num_islands(grid) == 1

def test_no_islands():
    """Test with no islands (all water)."""
    grid = [
        ["0","0","0"],
        ["0","0","0"],
        ["0","0","0"]
    ]
    assert num_islands(grid) == 0

def test_empty_grid():
    """Test with empty grid."""
    grid = []
    assert num_islands(grid) == 0

def test_single_row():
    """Test with single row grid."""
    grid = [["1","0","1","0","1"]]
    assert num_islands(grid) == 3

def test_single_column():
    """Test with single column grid."""
    grid = [["1"],["0"],["1"],["1"]]
    assert num_islands(grid) == 2

def test_diagonal_islands():
    """Test with islands connected diagonally (should count as separate)."""
    grid = [
        ["1","0","1"],
        ["0","0","0"],
        ["1","0","1"]
    ]
    assert num_islands(grid) == 4

def test_complex_shape():
    """Test with islands of complex shapes."""
    grid = [
        ["1","1","0","0","0"],
        ["1","0","0","0","0"],
        ["1","1","1","0","0"],
        ["0","0","0","0","1"]
    ]
    assert num_islands(grid) == 2

def test_border_islands():
    """Test with islands on the grid borders."""
    grid = [
        ["1","0","0","1","0"],
        ["0","0","0","0","0"],
        ["0","0","0","0","0"],
        ["1","0","0","1","0"]
    ]
    assert num_islands(grid) == 4

def test_single_cell():
    """Test with a single cell grid."""
    grid = [["1"]]
    assert num_islands(grid) == 1