# Maximum Subarray
# Time: O(n)
# Space: O(1)
# Topics: Array, Divide and Conquer, Dynamic Programming
# Difficulty: Easy
# Notes: Kadane's Algorithm -> O(n). This can also be done with divide and conquer but in O(nlogn) time.

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # nums will have at least 2 elements
        max_so_far = nums[0]  # dp tracker
        max_global = nums[0]
        
        for i in range(1, len(nums)):
            curr_val = nums[i]
            max_combined = curr_val + max_so_far
            
            max_so_far = max(curr_val, max_combined)
            
            if max_so_far > max_global:
                max_global = max_so_far
                
        return max_global
