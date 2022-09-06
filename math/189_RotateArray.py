# Rotate Array
# Time: O(n)
# Space: O(1)
# Topics: Array, Math, Two Pointers
# Difficulty: Medium

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        start_idx = 0
        curr_idx = 0
        
        for _ in range(n):
            if curr_idx == start_idx:
                start_idx = (start_idx + 1) % n
                curr_idx = (curr_idx + 1) % n
                
                temp_num = nums[(curr_idx + k) % n]
                nums[(curr_idx + k) % n] = nums[curr_idx]
                curr_idx = (curr_idx + k) % n
                continue
            
            nums[(curr_idx + k) % n], temp_num = temp_num, nums[(curr_idx + k) % n]
            curr_idx = (curr_idx + k) % n
