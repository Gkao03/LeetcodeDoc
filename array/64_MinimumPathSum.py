# Minimum Path Sum
# Time: O(mn)
# Space: O(1)
# Topics: Array, Dynamic Programming, Matrix
# Difficulty: Medium
# Notes: use input matrix to store dp table to get constant space.

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # all values in grid are non negative. can only move down or right
        for j in range(1, len(grid[0])):
            grid[0][j] += grid[0][j - 1]
            
        for i in range(1, len(grid)):
            grid[i][0] += grid[i - 1][0]
            
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        
        return grid[-1][-1]
