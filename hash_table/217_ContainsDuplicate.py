# Contains Duplicate
# Time: O(nlogn) upper bounded by sorting. O(n) to traverse list
# Space: O(1)
# Topics: Array, Hash Table, Sorting
# Difficulty: Easy
# Notes: can do in O(n) time with O(n) space with a hash table

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
            
        return False


from collections import defaultdict

class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        val_count = defaultdict(lambda: 0)
        
        for num in nums:
            val_count[num] += 1
            if val_count[num] >= 2:
                return True
            
        return False
