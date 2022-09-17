# Find Minimum in Rotated Sorted Array
# Time: O(logn)
# Space: O(1)
# Topics: Array, Binary Search
# Difficulty: Medium

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] > nums[0]:
            return nums[0]
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            if nums[mid] < nums[left]:
                right = mid
            else:
                left = mid
                
        return nums[0]
