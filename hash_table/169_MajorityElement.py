# Majority Element
# Time: O(n)
# Space: O(1)
# Topics: Array, Hash Table, Divide and Conquer, Sorting, Counting
# Difficulty: Easy
# Notes: you can use hash table trivially to store counts but will use O(n) space

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # constraint: majority element is guaranteed to exist
        
        maj_index = 0
        count = 1
        
        for i, val in enumerate(nums):
            if val == nums[maj_index]:
                count += 1
            else:
                count -= 1
                
            if count == 0:
                maj_index = i
                count = 1
                
        return nums[maj_index]
