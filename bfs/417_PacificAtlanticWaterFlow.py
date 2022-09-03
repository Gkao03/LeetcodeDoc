# Pacific Atlantic Water Flow
# Time: O(mn)
# Space: O(mn)
# Topics: Array, Depth-First Search, Breadth-First Search, Matrix
# Difficulty: Medium

from typing import List

class Solution:
    def dfs(self, heights, sea, i, j, prev_height):
        if i < 0 or j < 0 or i >= len(heights) or j >= len(heights[0]):  # out of bounds
            return
        
        if heights[i][j] < prev_height:  # cannot flow
            return
        
        if sea[i][j] is True:  # don't need to check again
            return
        
        sea[i][j] = True
        self.dfs(heights, sea, i - 1, j, heights[i][j])
        self.dfs(heights, sea, i + 1, j, heights[i][j])
        self.dfs(heights, sea, i, j - 1, heights[i][j])
        self.dfs(heights, sea, i, j + 1, heights[i][j])
        
        return
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    self.dfs(heights, pacific, i, j, 0)
                if i == m - 1 or j == n - 1:
                    self.dfs(heights, atlantic, i, j, 0)
                    
        output = [[r, c] for r in range(m) for c in range(n) if pacific[r][c] is True and atlantic[r][c] is True]
        
        return output
