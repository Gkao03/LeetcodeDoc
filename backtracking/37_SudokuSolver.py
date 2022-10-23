# Sudoku Solver
# Time: O(9^m). m is number of blanks in grid.
# Space: O(m) stack space.
# Topics: Array, Backtracking, Matrix
# Difficulty: Hard
# Notes: exactly one solution exists for each input board.

from typing import List

class Solution:
    def is_valid(self, board, row, col, digit):
        cell_row = 3 * (row // 3)
        cell_col = 3 * (col // 3)
        str_digit = str(digit)
        
        for i in range(9):
            if board[i][col] == str_digit or board[row][i] == str_digit or board[cell_row + i // 3][cell_col + i % 3] == str_digit:
                return False
            
        return True
    
    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for digit in range(1, 10):
                        if self.is_valid(board, i, j, digit):
                            board[i][j] = str(digit)
                            
                            if self.solve(board):
                                return True
                            
                            board[i][j] = '.'  # reset
                    return False
                
        return True
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)
