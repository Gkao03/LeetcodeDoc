# Number 1 Bits
# Time: O(logn) pseudo logarithmic
# Space: O(1)
# Topics: Bit Manipulation
# Difficulty: Easy

class Solution:
    def hammingWeight(self, n: int) -> int:
        num_1bits = 0
        
        while n != 0:
            if n & 1 == 1:
                num_1bits += 1
            n = n >> 1
            
        return num_1bits
