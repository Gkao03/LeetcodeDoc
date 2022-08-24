# Word Search
# Time: O(mn * 3^s). where m,n are the sizes of the board and s is length of the string
# Space: O(mn). O(mn) comes from creating a "visited" matrix. can turn to O(s) if reuse the given board to track visitation
# Topics: Array, Backtracking, Matrix
# Difficulty: Medium
# Notes: 3^s in the runtime comes from having 3 possible options at every cell since we cannot visit previous cells.
# Important - do not create any deepcopies in python since this operation takes a lot of time and will result in
# time limit exceeded.

from typing import List

class Solution:
    def find(self, i, j, next_word_idx, visited, is_found):
        if is_found is True:
            return True
        
        if next_word_idx >= len(self.word):
            return True
        
        directions = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        for adj_i, adj_j in directions:
            if adj_i >= 0 and adj_i < self.m and adj_j >= 0 and adj_j < self.n:
                if not visited[adj_i][adj_j] and self.board[adj_i][adj_j] == self.word[next_word_idx]:
                    # copy_visited = copy.deepcopy(visited)
                    visited[adj_i][adj_j] = True
                    is_found = is_found or self.find(adj_i, adj_j, next_word_idx + 1, visited, is_found)
                    visited[adj_i][adj_j] = False  # reset state
                    
                    if is_found is True:
                        return True
        
        return False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        self.m, self.n = len(board), len(board[0])
        visited = [[False] * self.n for _ in range(self.m)]
        
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if self.find(i, j, 1, visited, False) is True:
                        return True
                    
                    visited[i][j] = False  # reset state

        return False
