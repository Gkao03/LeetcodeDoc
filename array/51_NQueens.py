# N-Queens
# Time: O(n!)
# Space: O(n^2). O(n) stack space and for each recursive call, O(n) space is used to store string
# Topics: Array, Backtracking
# Difficulty: Hard

from typing import List
import copy

class Solution:
    def is_valid_Q_position(self, row_idx, col_idx, curr_output):
        # check column
        for row in curr_output:
            if row[col_idx] == 'Q':
                return False
            
        # check upper left diagonal
        i = row_idx - 1
        j = col_idx - 1
        while i >= 0 and j >= 0:
            if curr_output[i][j] == 'Q':
                return False
            
            i -= 1
            j -= 1
            
        # check upper right diagonal
        i = row_idx - 1
        j = col_idx + 1
        while i >= 0 and j < self.n:
            if curr_output[i][j] == 'Q':
                return False
            
            i -= 1
            j += 1
            
        return True
    
    def solve(self, row_idx, curr_output):
        if len(curr_output) == self.n:
            solution = copy.deepcopy(curr_output)
            self.output.append(solution)
            return
        
        row = ['.' for _ in range(self.n)]
        
        for col_idx in range(self.n):
            if self.is_valid_Q_position(row_idx, col_idx, curr_output):
                row[col_idx] = 'Q'
                curr_output.append("".join(row))
                self.solve(row_idx + 1, curr_output)
                
                # reset
                curr_output.pop()
                row[col_idx] = '.'
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.output = []
        self.solve(0, [])
        
        return self.output
