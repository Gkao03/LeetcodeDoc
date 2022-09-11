# Kth Largest Element in an Array
# Time: O(n) average. O(n^2) worst case
# Space: O(logn) stack space
# Topics: Array, Divide and Conquer, Sorting, Heap, Quickselect
# Difficulty: Medium
# Notes: this is similar to quicksort except we only recurse 
# on the half of the array that we know contains the kth 
# largest element (instead of both halves).
# The "median of medians" approach can be used to guarantee
# O(n) time worst case.

from typing import List

class Solution:
    def quickselect(self, nums, target_idx, left_idx, right_idx):
        pivot_num = nums[right_idx]
        pivot_idx = left_idx
        curr_idx = left_idx
        
        while curr_idx <= right_idx - 1:
            curr_num = nums[curr_idx]
            if curr_num <= pivot_num:
                nums[curr_idx], nums[pivot_idx] = nums[pivot_idx], nums[curr_idx]
                curr_idx += 1
                pivot_idx += 1
            else:
                curr_idx += 1
                
        # swap pivot idx with right idx
        nums[pivot_idx], nums[right_idx] = nums[right_idx], nums[pivot_idx]
        if pivot_idx == target_idx:
            return nums[pivot_idx]
        elif pivot_idx < target_idx:  # search right
            result = self.quickselect(nums, target_idx, pivot_idx + 1, right_idx)
        else:  # search left
            result = self.quickselect(nums, target_idx, left_idx, pivot_idx - 1)
            
        return result
        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kth_largest = self.quickselect(nums, len(nums) - k, 0, len(nums) - 1)
        return kth_largest
