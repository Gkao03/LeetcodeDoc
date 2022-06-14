# Squares of a Sorted Array
# Time: O(n)
# Space: O(n)
# Topics: Array, Two Pointers, Sorting
# Difficulty: Easy

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # nums guaranteed to have at least 1 element
        result = [0] * len(nums)
        result_ptr = len(nums) - 1
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[result_ptr] = nums[left] ** 2
                left += 1
            else:
                result[result_ptr] = nums[right] ** 2
                right -= 1
            
            result_ptr -= 1
            
        return result
