# Longest Increasing Path in a Matrix
# Time: O(mn)
# Space: O(mn)
# Topics: Array, Dynamic Programming, Depth-First Search, Breadth-First Search, Graph, Topological Sort, Memoization, Matrix
# Difficulty: Hard

from typing import List

class Solution:
    def get_valid_adj(self, curr_i, curr_j):
        adjacents = []
        
        if curr_i - 1 >= 0:
            adjacents.append((curr_i - 1, curr_j))
            
        if curr_i + 1 < self.n:
            adjacents.append((curr_i + 1, curr_j))
            
        if curr_j - 1 >= 0:
            adjacents.append((curr_i, curr_j - 1))
            
        if curr_j + 1 < self.m:
            adjacents.append((curr_i, curr_j + 1))
            
        return adjacents
    
    def dfs(self, curr_i, curr_j, visited):
        visited[curr_i][curr_j] = True
        
        adjacents = self.get_valid_adj(curr_i, curr_j)
        for adj_i, adj_j in adjacents:
            if not self.global_visited[adj_i][adj_j] and not visited[adj_i][adj_j]:
                if self.matrix[adj_i][adj_j] > self.matrix[curr_i][curr_j]:
                    self.dfs(adj_i, adj_j, visited)
        
        # get values and update dp
        values = [self.dp_table[i][j] + 1 for i, j in adjacents if self.matrix[i][j] > self.matrix[curr_i][curr_j]]
        values.append(self.dp_table[curr_i][curr_j])
        self.dp_table[curr_i][curr_j] = max(values)
        
        # update visited matrices
        visited[curr_i][curr_j] = False
        self.global_visited[curr_i][curr_j] = True
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.n, self.m = len(matrix), len(matrix[0])
        self.matrix = matrix
        self.dp_table = [[1] * self.m for _ in range(self.n)]
        self.global_visited = [[False] * self.m for _ in range(self.n)]
        visited = [[False] * self.m for _ in range(self.n)]
        longest_path = 1
        
        for i in range(self.n):
            for j in range(self.m):
                if not self.global_visited[i][j]:
                    self.dfs(i, j, visited)
                    longest_path = max(longest_path, self.dp_table[i][j])
                    
        return longest_path
