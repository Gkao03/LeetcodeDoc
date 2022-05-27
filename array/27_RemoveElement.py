# Remove Element
# Time: O(n)
# Space: O(1)
# Topics: Array, Two Pointers
# Difficulty: Easy

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        
        while idx < len(nums):
            if nums[idx] == val:
                del nums[idx]
            else:
                idx += 1
                
        return len(nums)