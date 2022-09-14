# Search a 2D Matrix
# Time: O(log(mn))
# Space: O(1)
# Topics: Array, Binary Search, Matrix
# Difficulty: Medium
# Notes: this implementation uses binary search on the matrix as
# if it was simulated as a flattened array.

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1
        
        while low <= high:
            mid = (low + high) // 2
            mid_i = mid // n
            mid_j = mid % n
            
            if matrix[mid_i][mid_j] == target:
                return True
            elif matrix[mid_i][mid_j] < target:  # binary search right side
                low = mid + 1
            else:  #  matrix[mid_i][mid_j] > target
                high = mid - 1
                
        return False
