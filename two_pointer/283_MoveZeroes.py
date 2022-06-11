# Move Zeros
# Time: O(n)
# Space: O(1)
# Topics: Array, Two Pointers
# Difficulty: Easy

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonzero_idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nonzero_idx] = nums[i]
                nonzero_idx += 1
                
        # all non zero elements have been moved to the front. 0 out remaining elements
        for i in range(nonzero_idx, len(nums)):
            nums[i] = 0
