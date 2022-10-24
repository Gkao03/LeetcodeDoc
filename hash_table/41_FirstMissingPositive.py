# First Missing Positive
# Time: O(n)
# Space: O(1)
# Topics: Array, Hash Table
# Difficulty: Hard
# Notes: we do not care about negatives or duplicates. Use the input array to
# store the integers in the correct index position.

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            num = nums[i]
            while num > 0 and num - 1 < len(nums) and nums[num - 1] != num:
                temp_num = nums[num - 1]
                nums[num - 1] = num
                num = temp_num
                
            i += 1
            
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
            
        return len(nums) + 1
