# Next Permutation
# Time: O(n)
# Space: O(1)
# Topics: Array, Two Pointers
# Difficulty: Medium

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        
        # find longest contiguous decreasing array from the end
        left_idx = len(nums) - 1  # start at end
        
        while left_idx - 1 >= 0:
            if nums[left_idx - 1] >= nums[left_idx]:
                left_idx -= 1
            else:
                break
        
        if left_idx == 0:
            nums.reverse()
            return
        
        # find first element from end that is greater than nums[left_idx - 1]
        right_idx = len(nums) - 1
        val = nums[left_idx - 1]
        
        while left_idx <= right_idx:
            if nums[right_idx] > val:
                swap_idx = right_idx
                break
            right_idx -= 1
            
        # swap left_idx - 1 and swap_idx
        nums[left_idx - 1], nums[swap_idx] = nums[swap_idx], nums[left_idx - 1]
        
        # now reverse the remaining list
        right_idx = len(nums) - 1
        while left_idx < right_idx:
            nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]
            left_idx += 1
            right_idx -= 1
