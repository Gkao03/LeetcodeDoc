# Subsets
# Time: O(2^n). There will be 2^n subsets.
# Space: O(n * 2^n). Copy operation takes n space.
# Topics: Array, Backtracking, Bit Manipulation
# Difficulty: Medium

import copy
from typing import List

class Solution:
    def helper(self, arr, nums, output):
        output.append(arr)
        
        for i, num in enumerate(nums):
            arr_copy = copy.deepcopy(arr)
            arr_copy.append(num)
            self.helper(arr_copy, nums[i+1:], output)
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        self.helper([], nums, output)
        return output
