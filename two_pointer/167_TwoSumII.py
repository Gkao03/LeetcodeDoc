# Two Sum II - Input Array is Sorted
# Time: O(n)
# Space: O(1)
# Topics: Array, Two Pointers, Binary Search
# Difficulty: Medium

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:  # target found, break and return
                break

        return [left + 1, right + 1]
