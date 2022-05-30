# Search Insert Position
# Time: O(logn) - binary search
# Space: O(1)
# Topics: Array, Binary Search
# Difficulty: Easy

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target > nums[0]:
                return 1
            else:
                return 0
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
            
        # now right < left
        return left
