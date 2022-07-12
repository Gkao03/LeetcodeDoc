# Number of Islands
# Time: O(mn)
# Space: O(mn)
# Topics: Array, Depth-First Search, Breadth-First Search, Union Find, Matrix
# Difficulty: Medium

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        num_islands = 0
        all_ones = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    all_ones.add((i, j))
                    
        while len(all_ones) != 0:
            dfs_stack = []
            init_i, init_j = all_ones.pop()
            dfs_stack.append((init_i, init_j))  # pop removes random element from set
            visited[init_i][init_j] = True
            
            while len(dfs_stack) != 0:
                curr_i, curr_j = dfs_stack.pop()
                top_i, top_j = max(0, curr_i - 1), curr_j
                left_i, left_j = curr_i, max(0, curr_j - 1)
                bot_i, bot_j = min(m - 1, curr_i + 1), curr_j
                right_i, right_j = curr_i, min(n - 1, curr_j + 1)
                
                if (not visited[top_i][top_j]) and grid[top_i][top_j] == "1":
                    visited[top_i][top_j] = True
                    dfs_stack.append((top_i, top_j))
                    if (top_i, top_j) in all_ones:
                        all_ones.remove((top_i, top_j))
                if (not visited[left_i][left_j]) and grid[left_i][left_j] == "1":
                    visited[left_i][left_j] = True
                    dfs_stack.append((left_i, left_j))
                    if (left_i, left_j) in all_ones:
                        all_ones.remove((left_i, left_j))
                if (not visited[bot_i][bot_j]) and grid[bot_i][bot_j] == "1":
                    visited[bot_i][bot_j] = True
                    dfs_stack.append((bot_i, bot_j))
                    if (bot_i, bot_j) in all_ones:
                        all_ones.remove((bot_i, bot_j))
                if (not visited[right_i][right_j]) and grid[right_i][right_j] == "1":
                    visited[right_i][right_j] = True
                    dfs_stack.append((right_i, right_j))
                    if (right_i, right_j) in all_ones:
                        all_ones.remove((right_i, right_j))
                        
            num_islands += 1
            
        return num_islands
