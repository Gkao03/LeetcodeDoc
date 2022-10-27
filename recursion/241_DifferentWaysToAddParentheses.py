# Different Ways to Add Parentheses
# Time: O(n*2^k). k is number of operators. n is length of string
# Space: O(n) stack space.
# Topics: Math, String, Dynamic Programming, Recursion, Memoization
# Difficulty: Medium
# Notes: can also do DP way. Runtime and space would depend on the catalan
# number C(k), where k is the number of operators.

from typing import List
import re

class Solution:
    def helper(self, exp):
        if len(exp) == 1:
            return [int(exp[0])]
        
        output = []
        
        for i, ele in enumerate(exp):
            if ele in self.operators:
                vals_left = self.helper(exp[:i])
                vals_right = self.helper(exp[i+1:])
                
                for vall in vals_left:
                    for valr in vals_right:
                        if ele == '-':
                            output.append(vall - valr)
                        elif ele == '+':
                            output.append(vall + valr)
                        elif ele == '*':
                            output.append(vall * valr)
                            
        return output
    
    def diffWaysToCompute(self, expression: str) -> List[int]:
        self.operators = {'+', '-', '*'}
        exp_list = re.split(r'(\D)', expression)
        output = []
        
        for i, ele in enumerate(exp_list):
            if ele in self.operators:
                vals_left = self.helper(exp_list[:i])
                vals_right = self.helper(exp_list[i+1:])
                
                for vall in vals_left:
                    for valr in vals_right:
                        if ele == '-':
                            output.append(vall - valr)
                        elif ele == '+':
                            output.append(vall + valr)
                        elif ele == '*':
                            output.append(vall * valr)
                            
        if len(output) == 0:
            output.append(eval(expression))
        
        return output
