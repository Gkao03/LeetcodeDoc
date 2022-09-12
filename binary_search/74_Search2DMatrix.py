# Search a 2D Matrix
# Time: O(log(mn))
# Space: O(1)
# Topics: Array, Binary Search, Matrix
# Difficulty: Medium
# Notes: this implementation uses O(m) space to get the column array,
# however it can be trivially converted to O(1) space by writing
# custome binary search based on row indices.

from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        col = [matrix[i][0] for i in range(m)]
        
        row_idx = bisect_right(col, target)
        if row_idx == 0:
            return False
        
        col_idx = bisect_left(matrix[row_idx - 1], target)
        if col_idx == n:
            return False
        
        if matrix[row_idx - 1][col_idx] == target:
            return True
        
        return False
