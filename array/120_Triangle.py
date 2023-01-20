# Triangle
# Time: O(n^2) where n is number of rows in triangle. Or O(N) where N is number of nodes in triangle.
# Space: O(n) where n is number of rows in triangle.
# Topics: Array, Dynamic Programming
# Diffulty: Medium
# Notes: keep a dp table of the previous row to build dp of current row. dp at current row
# will be the minimum valid previous dp + current val. Take minimum of current row at end.

from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        curr_dp = [triangle[0][0]]

        for i in range(1, len(triangle)):
            curr_row = triangle[i]
            next_dp = []

            for j, next_val in enumerate(curr_row):
                # need to check j and j - 1
                val1 = curr_dp[j] if j < len(curr_dp) else float("inf")
                val2 = curr_dp[j - 1] if j - 1 >= 0 else float("inf")

                min_val = min(val1, val2) + next_val
                next_dp.append(min_val)

            curr_dp = next_dp
        
        min_sum = min(curr_dp)
        return min_sum
