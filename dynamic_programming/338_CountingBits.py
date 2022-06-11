# Counting Bits
# Time: O(n) pseudo linear
# Space: O(n) pseudo linear
# Topics: Dynamic Programming, Bit Manipulation
# Difficulty: Easy

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        
        # n is at least 2
        num_bits = [0, 1] + [0] * (n - 1)
        next_power = 2
        dp_idx = 0
        
        i = 2
        while i <= n:
            if i == 2 ** next_power:
                dp_idx = 0
                next_power += 1
                
            num_bits[i] = num_bits[dp_idx] + 1
            i += 1
            dp_idx += 1
            
        return num_bits
