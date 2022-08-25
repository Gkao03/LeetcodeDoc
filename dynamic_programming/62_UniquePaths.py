# Unique Paths
# Time: O(m + n). Pseudo linear time to calculate factorial based on m and n
# Space: O(1)
# Topics: Math, Dynamic Programming, Combinatorics
# Difficulty: Medium
# Notes: Can also do DP with O(mn) time and O(n) space (less optimal than combinatorics)

import math

class Solution:
    def num_splits(self, k1, k2):
        f = math.factorial
        return f(k1 + k2) // f(k1) // f(k2)
    
    def uniquePaths(self, m: int, n: int) -> int:
        return self.num_splits(m - 1, n - 1)
