# Single Number
# Time: O(n)
# Space: O(1)
# Topics: Array, Bit Manipulation
# Difficulty: Easy
# Notes: the key idea here is that a number xor with itself will be 0. Since all other nums
# show up in pairs, the resulting xor will be the one num that only shows up once.

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        curr_xor = 0
        
        for num in nums:
            curr_xor = curr_xor ^ num
            
        return curr_xor
