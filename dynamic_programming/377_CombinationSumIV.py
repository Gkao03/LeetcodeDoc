# Combination Sum IV
# Time: Pseudo O(n * target). n is length of nums, target is the target value.
# Space: O(target)
# Topics: Array, Dynamic Programming
# Difficulty: Medium
# Notes: the index in the dp array represents the number of ways to reach that
# value. sum up all number of ways based on remainder for each num in nums.
# build DP table bottom up.

from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1  # initialize. 1 way to get a value of 0
        
        for curr_target in range(1, target + 1):
            for num in nums:
                remainder = curr_target - num
                
                if remainder >= 0:
                    dp[curr_target] += dp[remainder]
                    
        return dp[-1]
