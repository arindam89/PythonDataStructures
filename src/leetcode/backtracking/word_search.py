# LeetCode 79: Word Search
# https://leetcode.com/problems/word-search/
#
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once.
#
# Approach:
# - Use backtracking to explore all possible paths in the grid.
# - At each step, check if the current cell matches the current character of the word.
# - Mark the cell as visited and recurse for its neighbors.
# - Backtrack by unmarking the cell after exploring all paths.

def exist(board, word):
    def backtrack(r, c, index):
        if index == len(word):
            # All characters matched
            return True
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != word[index]:
            # Out of bounds or character mismatch
            return False

        # Mark the cell as visited
        temp = board[r][c]
        board[r][c] = '#'

        # Explore all possible directions
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if backtrack(r + dr, c + dc, index + 1):
                return True

        # Backtrack by unmarking the cell
        board[r][c] = temp
        return False

    for i in range(len(board)):
        for j in range(len(board[0])):
            if backtrack(i, j, 0):
                return True
    return False