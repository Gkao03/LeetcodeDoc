# Partition Equal Subset Sum
# Time: O(sum * n) - Pseudopolynomial
# Space: O(sum * n). Can reduce to O(sum) since you only need 2 columns at a time of DP table
# Topics: Array, Dynamic Programming
# Difficulty: Medium
# Notes: similar to knapsack problem. Build DP table bottom up

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        
        if sum(nums) % 2 == 1:
            return False
        
        target = sum(nums) // 2
        
        dp_table = [[False] * (len(nums) + 1) for _ in range(target + 1)]
        # initialize base cases of dp table
        for j in range(len(nums) + 1):
            dp_table[0][j] = True
            
        # build up dp table bottom up
        for j in range(1, len(nums) + 1):
            curr_int = nums[j - 1]
            
            for i in range(target, -1, -1):
                if dp_table[i][j] is False:  # copy from previous column (but don't overwrite if already True)
                    dp_table[i][j] = dp_table[i][j - 1]
                
                if dp_table[i][j] is True and i + curr_int <= target:
                    dp_table[i + curr_int][j] = True
                      
        return dp_table[-1][-1]
