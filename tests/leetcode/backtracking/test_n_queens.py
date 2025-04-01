import pytest
from src.leetcode.backtracking.n_queens import solve_n_queens

def test_n_queens_1():
    """Test with 1x1 board."""
    result = solve_n_queens(1)
    assert result == [["Q"]]

def test_n_queens_4():
    """Test with 4x4 board."""
    result = solve_n_queens(4)
    expected = [
        [".Q..", "...Q", "Q...", "..Q."],
        ["..Q.", "Q...", "...Q", ".Q.."]
    ]
    assert len(result) == 2
    assert all(solution in expected for solution in result)
    
def test_n_queens_verify_solution():
    """Test that solutions are valid (no queens threaten each other)."""
    n = 5
    solutions = solve_n_queens(n)
    
    def is_valid_solution(board):
        # Convert string representation to queen positions
        queens = []
        for i, row in enumerate(board):
            queens.append((i, row.index('Q')))
            
        # Check each pair of queens
        for i, (r1, c1) in enumerate(queens):
            for r2, c2 in queens[i + 1:]:
                # Check if queens threaten each other
                if (r1 == r2 or  # Same row
                    c1 == c2 or  # Same column
                    abs(r1 - r2) == abs(c1 - c2)):  # Same diagonal
                    return False
        return True
    
    assert all(is_valid_solution(solution) for solution in solutions)
    
def test_n_queens_count_solutions():
    """Test the number of solutions for different board sizes."""
    # Known number of solutions for different n
    solution_counts = {
        1: 1,
        2: 0,
        3: 0,
        4: 2,
        5: 10,
        6: 4,
        7: 40,
        8: 92
    }
    
    for n, expected_count in solution_counts.items():
        assert len(solve_n_queens(n)) == expected_count
        
def test_n_queens_board_format():
    """Test that the board format is correct."""
    n = 4
    solutions = solve_n_queens(n)
    
    for solution in solutions:
        # Check board dimensions
        assert len(solution) == n
        assert all(len(row) == n for row in solution)
        
        # Check that each row has exactly one queen
        assert all(row.count('Q') == 1 for row in solution)
        
        # Check that only valid characters are used
        assert all(all(c in '.Q' for c in row) for row in solution)