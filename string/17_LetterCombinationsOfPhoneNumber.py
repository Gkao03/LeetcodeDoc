# Letter Combinations of a Phone Number
# Time: O(4^n). worst case each digit has 4 characters associated with it
# Space: O(4^n)
# Topics: Hash Table, String, Backtracking
# Difficulty: Medium

import copy
from typing import List

class Solution:
    def helper(self, digits, digits_idx, curr_str):
        if digits_idx >= len(digits):
            self.output.append(curr_str)
            return
        
        curr_digit = digits[digits_idx]
        characters = self.mapping[curr_digit]
        
        for char in characters:
            copy_str = copy.deepcopy(curr_str)
            copy_str += char
            self.helper(digits, digits_idx + 1, copy_str)
            
        
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        self.mapping = {'2': "abc",
                        '3': "def",
                        '4': "ghi",
                        '5': "jkl",
                        '6': "mno",
                        '7': "pqrs",
                        '8': "tuv",
                        '9': "wxyz"}
        
        self.output = []
        self.helper(digits, 0, "")
        
        return self.output
