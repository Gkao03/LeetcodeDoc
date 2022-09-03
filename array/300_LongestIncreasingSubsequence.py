# Longest Increasing Subsequence
# Time: O(nlogn)
# Space: O(n)
# Topics: Array, Binary Search, Dynamic Programming
# Difficulty: Medium
# Notes: use binary search to find the greatest element
# less than current element.

from typing import List
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        optimal = [nums[0]]
        
        for i in range(1, len(nums)):
            num = nums[i]
            idx = bisect_left(optimal, num)
            
            if idx >= len(optimal):
                optimal.append(num)
            else:
                optimal[idx] = num
        
        return len(optimal)
