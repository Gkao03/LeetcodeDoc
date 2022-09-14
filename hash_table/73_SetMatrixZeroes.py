# Set Matrix Zeroes
# Time: O(mn)
# Space: O(1)
# Topics: Array, Hash Table, Matrix
# Difficulty: Medium
# Notes: use the topmost row and leftmost column to
# keep track of which rows and columns need to be 
# zeroed out at the end.

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        
        # initialize topmost row and leftmost column
        fill_top = False
        for j in range(n):
            if matrix[0][j] == 0:
                fill_top = True
                break
                
        fill_left = False
        for i in range(m):
            if matrix[i][0] == 0:
                fill_left = True
                break
        
        # find 0 elements and store 0's in topmost row and lefmost col
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0], matrix[0][j] = 0, 0
                    
        # set rows and columns to 0 based on topmost row and leftmost col
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
                    
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
                    
        # fill topmost row or leftmost col based on booleans
        if fill_top is True:
            for j in range(n):
                matrix[0][j] = 0
                
        if fill_left is True:
            for i in range(m):
                matrix[i][0] = 0
