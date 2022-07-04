# Evaluate Reverse Polish Notation
# Time: O(n)
# Space: O(n)
# Topics: Array, Math, Stack
# Difficulty: Medium

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # given RPN guaranteed to be valid. No division by 0 either.
        stack = []
        operands = ['+', '-', '*', '/']
        
        for token in tokens:
            if token in operands:
                val1 = stack.pop()
                val2 = stack.pop()
                
                if token == '+':
                    result = val1 + val2
                elif token == '-':
                    result = val2 - val1
                elif token == '*':
                    result = val1 * val2
                elif token == '/':
                    result = int(val2 / val1)  # should truncate towards 0
                    
                stack.append(result)
                    
            else:  # a numerical value
                stack.append(int(token))
                
        return stack[0]
