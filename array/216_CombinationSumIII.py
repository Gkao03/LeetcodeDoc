# Combination Sum III
# Time: O(9 choose k)
# Space: O(k) stack space (not counting output solution). O(k + k * # of answers)
# Topics: Array, Backtracking
# Difficulty: Medium

from typing import List
import copy

class Solution:
    def helper(self, k, n, start_i, curr_output):
        # base case: did not meet k requirement
        if n == 0 and k != 0:
            return

        # base case: found a solution
        if n == 0 and k == 0:
            self.output.append(copy.deepcopy(curr_output))
            return

        for i in range(start_i, 10):
            if n - i >= 0:
                curr_output.append(i)
                self.helper(k - 1, n - i, i + 1, curr_output)
                curr_output.pop()
            elif n - i < 0:
                break

        return

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # only digits 1 through 9 are used
        self.output = []
        self.helper(k, n, 1, [])

        return self.output
