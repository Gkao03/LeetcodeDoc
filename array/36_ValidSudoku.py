# Valid Sudoku
# Time: O(1)
# Space: O(1)
# Topics: Array, Hash Table, Matrix
# Difficulty: Medium
# Notes: time and space are technically O(1) since input is always 9x9

from typing import List

class Solution:
    def valid_cell(self, board, start_i, start_j):
        checked = [False] * 9
        for i in range(start_i, start_i + 3):
            for j in range(start_j, start_j + 3):
                if board[i][j] != '.' and checked[int(board[i][j]) - 1] is True:
                    return False
                if board[i][j] != '.':
                    checked[int(board[i][j]) - 1] = True
                
        return True
    
    def valid_row(self, board, row_i):
        checked = [False] * 9
        for j in range(9):
            if board[row_i][j] != '.' and checked[int(board[row_i][j]) - 1] is True:
                return False
            if board[row_i][j] != '.':
                checked[int(board[row_i][j]) - 1] = True
            
        return True
    
    def valid_col(self, board, col_j):
        checked = [False] * 9
        for i in range(9):
            if board[i][col_j] != '.' and checked[int(board[i][col_j]) - 1] is True:
                return False
            if board[i][col_j] != '.':
                checked[int(board[i][col_j]) - 1] = True
            
        return True
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check cells
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                if not self.valid_cell(board, i, j):
                    return False
                
        # check rows
        for i in range(9):
            if not self.valid_row(board, i):
                return False
            
        # check columns
        for j in range(9):
            if not self.valid_col(board, j):
                return False
            
        return True
