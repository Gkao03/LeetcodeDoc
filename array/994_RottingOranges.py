# Rotting Oranges
# Time: O(mn). Time to BFS
# Space: O(mn). For storing queue and unvisited set
# Topics: Array, Breadth-First Search, Matrix
# Difficulty: Medium
# Notes: BFS must be used instead of DFS since the minute marker matters

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rotten_queue = deque()  # tuple (i, j, minute marker of rotting)
        unvisited_oranges = set()  # acts as unvisited set
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:  # rotten orange
                    rotten_queue.append((i, j, 0))
                if grid[i][j] == 1:  # fresh orange
                    unvisited_oranges.add((i, j))
                    
        max_minute_no_fresh_oranges = 0
        
        while len(rotten_queue) > 0:
            curr_i, curr_j, curr_min_marker = rotten_queue.popleft()
            max_minute_no_fresh_oranges = max(max_minute_no_fresh_oranges, curr_min_marker)
            
            adj_list = []
            adj_list.append((max(0, curr_i - 1), curr_j))  # top cell
            adj_list.append((curr_i, min(n - 1, curr_j + 1)))  # right cell
            adj_list.append((min(m - 1, curr_i + 1), curr_j))  # bottom cell
            adj_list.append((curr_i, max(0, curr_j - 1)))  # left cell
            
            for adj_i, adj_j in adj_list:
                if (adj_i, adj_j) in unvisited_oranges:
                    rotten_queue.append((adj_i, adj_j, curr_min_marker + 1))
                    unvisited_oranges.remove((adj_i, adj_j))
                    
        if len(unvisited_oranges) > 0:
            return -1
        return max_minute_no_fresh_oranges
