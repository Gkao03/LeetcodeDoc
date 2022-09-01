# Maximum Product Subarray
# Time: O(n)
# Space: O(1)
# Topics: Array, Dynamic Programming
# Difficulty: Medium
# Notes: see also "Maximum Subarray" problem. Similar DP.

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_pos_so_far = nums[0]
        min_neg_so_far = nums[0]
        max_global = max_pos_so_far
        
        for i in range(1, len(nums)):
            num = nums[i]
            
            if num < 0:
                max_pos_so_far, min_neg_so_far = max(num, num * min_neg_so_far), min(num, num * max_pos_so_far)
            else:
                max_pos_so_far, min_neg_so_far = max(num, num * max_pos_so_far), min(num, num * min_neg_so_far)
                
            max_global = max(max_global, max_pos_so_far)
            
        return max_global
