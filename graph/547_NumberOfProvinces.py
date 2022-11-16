# Number of Provinces
# Time: O(n^2)
# Space: O(n) stack space and to keep track of visited points
# Topics: Depth-First Search, Breadth-First Search, Union Find, Graph
# Difficulty: Medium

from typing import List

class Solution:
    def dfs(self, row_idx):
        self.global_visited[row_idx] = True
        
        for col_idx, val in enumerate(self.is_connected[row_idx]):
            if val == 1 and not self.global_visited[col_idx]:
                self.dfs(col_idx)
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.is_connected = isConnected
        
        answer = 0
        self.global_visited = [False] * len(isConnected)
        
        for row_idx in range(len(isConnected)):
            if not self.global_visited[row_idx]:
                self.dfs(row_idx)
                answer += 1
            
        return answer
