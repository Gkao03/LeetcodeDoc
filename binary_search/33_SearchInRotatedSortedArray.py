# Search in Rotated Sorted Array
# Time: O(logn)
# Space: O(1)
# Topics: Array, Binary Search
# Difficulty: Medium
# Notes: Constraint requires to run in O(logn) time

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums guaranteed to have distinct values
        left = 0
        right = len(nums) - 1
        
        pivot_idx = 0  # initialize to no pivot (normal sorted array)
        while left <= right:  # find the pivot index
            if nums[left] < nums[right]:  # no rotation
                pivot_idx = left
                break
            if left == right:
                pivot_idx = left
                break
            if left + 1 == right:
                pivot_idx = right
                break
            
            mid = (left + right) // 2
            if nums[mid] == target:  # maybe we can get lucky and return early
                return mid
            
            if nums[mid] < nums[left]:
                right = mid
            else:
                left = mid
                
        nums = nums[pivot_idx:] + nums[:pivot_idx]
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return (mid + pivot_idx) % len(nums)
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1
