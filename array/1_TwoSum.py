# Two Sum
# Time: O(n)
# Space: O(n)
# Topics: Array, Hash Table
# Difficulty: Easy

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        
        for i, val in enumerate(nums):
            opp = target - val
            
            if opp in m:
                return [m[opp], i]
            else:
                m[val] = i
