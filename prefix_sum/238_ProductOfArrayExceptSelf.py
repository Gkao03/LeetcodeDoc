# Product of Array Except Self
# Time: O(n)
# Space: O(1) not counting the "answer" array. O(n) counting the "answer" array
# Topics: Array, Prefix Sum
# Difficulty: Medium
# Notes: The problem requires O(n) time without using division operation

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        
        running_product = 1
        for i in range(len(nums)):
            running_product *= nums[i]
            
            if i + 1 < len(nums):
                answer[i + 1] *= running_product
                
        running_rev_product = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= running_rev_product
                
            running_rev_product *= nums[i]
            
        return answer
