# Global and Local Inversions
# Time: O(n)
# Space: O(1)
# Topics: Array, Math
# Difficulty: Medium
# Notes: A local inversion is also a global inversion but a global inversion
# is not necessarily a local inversion. Using this fact we can keep track
# of the maximum value so far that is done checking and compare it with the
# 2nd value in our window of size 2 to check if a global inversion (that is
# not a local inversion) exists.

from typing import List

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        max_so_far = float("-inf")

        for i in range(len(nums) - 1):
            num1 = nums[i]
            num2 = nums[i + 1]

            if num2 < max_so_far:
                return False

            max_so_far = max(max_so_far, num1)

        return True
    

# Global and Local Inversions
# Time: O(n)
# Space: O(1)
# Topics: Array, Math
# Difficulty: Medium
# Notes: Imagine you start backwards with a sorted array. For the
# number of global inversion = local inversions, you can only swap
# adjacent pairs of values. Since all integers are in range [0, n-1],
# we just have to check the value - index should be <= 1, or else we
# return False.

class Solution2:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        for i, num in enumerate(nums):
            if abs(num - i) > 1:
                return False

        return True
