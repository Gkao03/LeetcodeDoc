# Permutations II
# Time: O(n * n!). O(n) to iterate dict. O(n!) function calls.
# Space: O(n!) to store solution. O(n) stack and dict space not counting solution space.
# Topics: Array, Backtracking
# Difficulty: Medium

import copy
from typing import List
from collections import defaultdict

class Solution:
    def dfs(self, counts, num_left, curr_answer):
        if num_left == 0:
            self.answer.append(copy.deepcopy(curr_answer))
            return

        for key in counts:
            if counts[key] == 0:
                continue

            curr_answer.append(key)
            counts[key] -= 1

            self.dfs(counts, num_left - 1, curr_answer)
            curr_answer.pop()
            counts[key] += 1

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counts = defaultdict(lambda: 0)
        for num in nums:
            counts[num] += 1
        
        self.answer = []  # store all answers here

        for key in counts:
            curr_answer = [key]
            counts[key] -= 1

            self.dfs(counts, len(nums) - 1, curr_answer)
            counts[key] += 1

        return self.answer
