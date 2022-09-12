# Maximal Square
# Time: O(mn)
# Space: O(mn)
# Topics: Array, Dynamic Programming, Matrix
# Difficulty: Medium
# Notes: this approach builds the dp table bottom up and checks if
# the sizes of the 3 adjacent cells to the left, upper, and upper left.
# The space can be reduced to O(n) since we do not need to keep track of
# every single row of the dp table (only need to keep 2 rows at a time).

from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp_table = [[0] * (n + 1) for _ in range(m + 1)]
        answer = 0
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp_table[i][j] = min(dp_table[i - 1][j], dp_table[i][j - 1], dp_table[i - 1][j - 1]) + 1
                    answer = max(answer, dp_table[i][j])
                
        return answer ** 2


# Maximal Square
# Time: O(mn)
# Space: O(mn)
# Topics: Array, Dynamic Programming, Matrix
# Difficulty: Medium
# Notes: this approach utilizes submatrix sum to be able
# to calculate areas in constant time after preprocessing.

class Solution2:
    def get_sum(self, top_left, bot_right):
        tl_i, tl_j = top_left
        br_i, br_j = bot_right
        
        left_i, left_j = br_i, tl_j - 1
        up_i, up_j = tl_i - 1, br_j
        upleft_i, upleft_j = tl_i - 1, tl_j - 1
        
        left_sum = self.dp_sum[left_i][left_j] if left_j >= 0 else 0
        up_sum = self.dp_sum[up_i][up_j] if up_i >= 0 else 0
        upleft_sum = self.dp_sum[upleft_i][upleft_j] if upleft_i >= 0 and upleft_j >= 0 else 0
        all_sum = self.dp_sum[br_i][br_j]
        
        result_sum = all_sum - left_sum - up_sum + upleft_sum
        return result_sum
    
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        self.dp_sum = [[0]  * n for _ in range(m)]
        
        # init dp table
        for i in range(m):
            for j in range(n):
                left_i, left_j = i, j - 1
                up_i, up_j = i - 1, j
                upleft_i, upleft_j = i - 1, j - 1
                
                left_sum = self.dp_sum[left_i][left_j] if left_j >= 0 else 0
                up_sum = self.dp_sum[up_i][up_j] if up_i >= 0 else 0
                upleft_sum = self.dp_sum[upleft_i][upleft_j] if upleft_i >= 0 and upleft_j >= 0 else 0
                self.dp_sum[i][j] = left_sum + up_sum - upleft_sum + int(matrix[i][j])
                
        answer = 0
        side_len = 0  # use to calculate target area
        top_left = (-1, 0)
        bot_right = (0, 0)
        
        while bot_right[0] < m:
            top_left = (top_left[0] + 1, 0)
            bot_right = (top_left[0] + side_len, top_left[1] + side_len)
            while bot_right[0] < m and bot_right[1] < n:
                curr_area = self.get_sum(top_left, bot_right)
                if curr_area == (side_len + 1) ** 2:
                    answer = (side_len + 1) ** 2
                    side_len += 1
                else:
                    top_left = (top_left[0], top_left[1] + 1)
                bot_right = (top_left[0] + side_len, top_left[1] + side_len)
                
        return answer
