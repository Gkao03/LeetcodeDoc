# 3Sum Closest
# Time: O(n^2)
# Space: O(1)
# Topics: Array, Two Pointers, Sorting
# Difficulty: Medium

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # O(nlogn) sort
        closest = float("inf")
        
        for i in range(0, len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                
                if abs(curr_sum - target) < abs(closest - target):
                    closest = curr_sum
                
                if curr_sum < target:
                    left = left + 1
                elif curr_sum > target:
                    right = right - 1
                else:  # curr_sum == target
                    return target
                
        return closest
