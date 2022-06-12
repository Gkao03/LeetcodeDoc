# Reverse Bits
# Time: O(1). always loops 32 times for a 32 bit int
# Space: O(1)
# Topics: Divide and Conquer, Bit Manipulation
# Difficulty: Easy

class Solution:
    def reverseBits(self, n: int) -> int:  # input is 32 bit int
        rev_num = 0
        
        for i in range(32):
            power = 31 - i
            curr_bit = (n >> i) & 1
            rev_num += (2 ** power) * curr_bit
            
        return rev_num
