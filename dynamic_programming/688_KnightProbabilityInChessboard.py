# Knight Probability in Chessboard
# Time: O(n^2 * k). n is side length of board. k is number of moves.
# Space: O(n^2) to keep dp table
# Topics: Dynamic Programming
# Difficulty: Medium

class Solution:
    def get_possible_cells(self, n, row, col):
        moveset1 = [-1, 1]
        moveset2 = [-2, 2]

        cells = []
        cells.extend([(row + i, col + j) for i in moveset1 for j in moveset2 if 0 <= row + i < n and 0 <= col + j < n])
        cells.extend([(row + i, col + j) for i in moveset2 for j in moveset1 if 0 <= row + i < n and 0 <= col + j < n])
        return cells

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # k is at least 1. initialize dp table
        curr_dp_table = [[1] * n for _ in range(n)]

        for _ in range(k):  # O(k)
            next_dp_table = [[0] * n for _ in range(n)]  # init blank next dp table

            for i in range(n):  # O(n)
                for j in range(n):  # O(n)
                    possible_cells = self.get_possible_cells(n, i, j)
                    probabilities = [curr_dp_table[row][col] for row, col in possible_cells]
                    next_dp_table[i][j] = (1 / 8) * sum(probabilities)

            curr_dp_table = next_dp_table

        return curr_dp_table[row][column]
