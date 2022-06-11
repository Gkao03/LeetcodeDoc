# Missing Number
# Time: O(n)
# Space: O(1)
# Topics: Array, Hash Table, Math, Bit Manipulation, Sorting
# Difficulty: Easy

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        target_sum = (n * (n + 1)) // 2
        actual_sum = sum(nums)
        missing_num = target_sum - actual_sum
        return missing_num
