# Jump Game
# Time: O(n)
# Space: O(1)
# Topics: Array, Dynamic Programming, Greedy
# Difficulty: Medium

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_can_reach_idx = 0
        
        for i in range(len(nums)):
            if max_can_reach_idx < i:
                return False
            
            jump_dist = nums[i]
            max_can_reach_idx = max(max_can_reach_idx, i + jump_dist)
            
        return True
