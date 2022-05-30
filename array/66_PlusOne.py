# Plus One
# Time: O(n)
# Space: O(1)
# Topics: Array, Math
# Difficulty: Easy

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        
        overflow = False
        
        for i in range(len(digits) - 1, -1, -1):
            if overflow:
                digits[i] += 1
                overflow = False
                
            if digits[i] == 10:
                digits[i] = 0
                overflow = True
                
        if overflow:
            digits = [1] + digits
            
        return digits
