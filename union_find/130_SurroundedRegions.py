# Surrounded Regions
# Time: O(mn)
# Space: O(mn)
# Topics: Array, Depth-First Search, Breadth-First Search, Union Find, Matrix
# Difficulty: Medium

from typing import List

class Solution:
    def dfs_cant_flip(self, i, j, board, cant_flip):
        cant_flip[i][j] = True

        adj_dirs = [[i + di, j + dj] for di, dj in self.dirs if 0 <= i + di < self.m and 0 <= j + dj < self.n and not cant_flip[i + di][j + dj]]

        for ni, nj in adj_dirs:
            self.dfs_cant_flip(ni, nj, board, cant_flip)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.m, self.n = len(board), len(board[0])
        self.dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        cant_flip = [[True if board[i][j] == 'X' else False for j in range(self.n)] for i in range(self.m)]
        
        # check left/right borders
        for i in range(self.m):
            if board[i][0] == 'O' and not cant_flip[i][0]:
                self.dfs_cant_flip(i, 0, board, cant_flip)
            
            if board[i][self.n - 1] == 'O' and not cant_flip[i][self.n - 1]:
                self.dfs_cant_flip(i, self.n - 1, board, cant_flip)

        # check top/bot borders
        for j in range(self.n):
            if board[0][j] == 'O' and not cant_flip[0][j]:
                self.dfs_cant_flip(0, j, board, cant_flip)
            
            if board[self.m - 1][j] == 'O' and not cant_flip[self.m - 1][j]:
                self.dfs_cant_flip(self.m - 1, j, board, cant_flip)

        # flip any remaining 'O' that can be flipped
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == 'O' and not cant_flip[i][j]:
                    board[i][j] = 'X'
