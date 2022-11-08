# Shifting Letters
# Time: O(n)
# Space: O(n) including output string. O(1) not counting output string
# Topics: Array, String
# Difficulty: Medium
# Notes: use a suffix sum (similar to reversed prefix sum)

from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        for i in range(len(shifts) - 2, -1, -1):
            shifts[i] += shifts[i + 1]
            
        output_str = []
        
        for shift, char in zip(shifts, s):
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            output_str.append(new_char)
            
        return "".join(output_str)
