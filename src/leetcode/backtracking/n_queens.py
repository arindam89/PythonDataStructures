"""
LeetCode 51: N-Queens
https://leetcode.com/problems/n-queens/

The n-queens puzzle is the problem of placing n queens on an n x n chessboard
such that no two queens threaten each other. Given an integer n, return all
distinct solutions to the n-queens puzzle. You may return the answer in any order.

A queen can move horizontally, vertically, and diagonally on the chess board.

Time Complexity: O(n!)
Space Complexity: O(n^2) for board storage
"""

from typing import List

def solve_n_queens(n: int) -> List[List[str]]:
    """
    Find all distinct solutions to the n-queens puzzle.
    
    Args:
        n: Size of the board (n x n)
        
    Returns:
        List of all valid board configurations
    """
    def create_board() -> List[str]:
        """Convert current state to board representation."""
        return [''.join('Q' if j == queens[i] else '.' 
                       for j in range(n)) for i in range(n)]
    
    def is_safe(row: int, col: int) -> bool:
        """Check if a queen can be placed at given position."""
        # Check previous rows
        for prev_row in range(row):
            prev_col = queens[prev_row]
            
            # Check vertical and diagonal attacks
            if prev_col == col or \
               abs(prev_col - col) == abs(prev_row - row):
                return False
        return True
    
    def backtrack(row: int) -> None:
        """Place queens row by row using backtracking."""
        if row == n:
            # Found a valid solution
            result.append(create_board())
            return
            
        # Try placing queen in each column of current row
        for col in range(n):
            if is_safe(row, col):
                queens[row] = col
                backtrack(row + 1)
                queens[row] = -1  # Backtrack
    
    result = []
    # queens[i] represents the column position of queen in row i
    queens = [-1] * n
    backtrack(0)
    return result