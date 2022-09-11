# Rotate Image
# Time: O(n^2). input matrix is n x n
# Space: O(1)
# Topics: Array, Math, Matrix
# Difficulty: Medium

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range((n + 1) // 2):
            for j in range(n // 2 if n % 2 == 1 else (n + 1) // 2):  # edge case if n is even or odd
                temp = matrix[i][j]
                curr_i, curr_j = i, j
                for _ in range(4):
                    next_i, next_j = curr_j, n - 1 - curr_i
                    matrix[next_i][next_j], temp = temp, matrix[next_i][next_j]
                    curr_i, curr_j = next_i, next_j
