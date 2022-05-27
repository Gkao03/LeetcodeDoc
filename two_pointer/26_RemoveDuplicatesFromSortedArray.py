# Remove Duplicates from Sorted Array
# Time: O(n)
# Space: O(1)
# Topics: Array, Two Pointers
# Difficulty: Easy

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        idx = 0
        while idx < len(nums) - 1:
            val1 = nums[idx]
            val2 = nums[idx + 1]
            
            if val1 == val2:
                del nums[idx + 1]
            else:
                idx += 1
                
        return len(nums)
