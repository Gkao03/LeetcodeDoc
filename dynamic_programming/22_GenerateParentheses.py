# Generate Parentheses
# Time: O(2^n)
# Space: O(2^n) to store output. O(n) only considering stack space (not output space)
# Topics: String, Dynamic Programming, Backtracking
# Difficulty: Medium

from typing import List

class Solution:
    def helper(self, left_count, right_count, curr_string, output):
        if left_count == 0 and right_count == 0:
            output.append("".join(curr_string))
            return
            
        if left_count > 0:
            curr_string.append('(')
            self.helper(left_count - 1, right_count, curr_string, output)
            curr_string.pop()
            
        if left_count < right_count:
            curr_string.append(')')
            self.helper(left_count, right_count - 1, curr_string, output)
            curr_string.pop()
            
        return
    
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        self.helper(n, n, [], output)
        
        return output
