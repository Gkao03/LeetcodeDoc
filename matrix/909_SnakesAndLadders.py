# Snakes and Ladders
# Time: O(n^2). n is the side length of the board
# Space: O(n^2)
# Topics: Array, Breadth-First Search, Matrix
# Difficulty: Medium

from typing import List
from collections import deque

class Solution:
    def get_idx_from_label(self, n, val):
        num = val - 1

        rows_shift = num // n
        cols_shift = num % n

        i = n - 1 - rows_shift
        j = n - 1 - cols_shift if rows_shift % 2 == 1 else cols_shift

        return i, j

    def get_label_from_idx(self, n, i, j):
        row_val = n - 1 - i
        label = n * row_val if row_val % 2 == 0 else n * (row_val + 1)
        label = label + j + 1 if row_val % 2 == 0 else label - j
        return label

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        num_moves = 1
        queue = deque([(n - 1, 0)])

        # set a visited matrix
        visited = [[False] * n for _ in range(n)]

        while len(queue) > 0:
            next_queue = deque()

            while len(queue) > 0:
                i, j = queue.popleft()
                visited[i][j] = True
                curr_label = self.get_label_from_idx(n, i, j)

                for die_roll in range(1, 7):
                    next_label = curr_label + die_roll

                    if next_label == n ** 2:
                        return num_moves

                    if next_label < n ** 2:
                        next_i, next_j = self.get_idx_from_label(n, next_label)
                        
                        # go down/up snake/ladder
                        if board[next_i][next_j] != -1:
                            # first check if new location is the end
                            if board[next_i][next_j] == n ** 2:
                                return num_moves

                            next_i, next_j = self.get_idx_from_label(n, board[next_i][next_j])

                        if not visited[next_i][next_j]:
                            next_queue.append((next_i, next_j))

            queue = next_queue
            num_moves += 1

        return -1
