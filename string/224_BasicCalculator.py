# Basic Calculator
# Time: O(n). n is length of string s.
# Space: O(n)
# Topics: Math, String, Stack, Recursion
# Difficulty: Hard

class Solution:
    def calculate(self, s: str) -> int:
        # s expression guaranteed to be valid
        stack = []
        
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
                
            if s[i].isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                
                stack.append(s[start:i])
            elif s[i] != ')':
                stack.append(s[i])
                i += 1
            else:  # s[i] == ')'
                if len(stack) >= 3 and stack[-3] == '(' and stack[-2] == '-':  # edge case if (-num)
                    num = int(stack.pop())
                    stack.pop()  # remove the negation
                    stack.append(-num)
                
                while stack[-2] != '(':
                    num2 = int(stack.pop())
                    operator = stack.pop()
                    num1 = int(stack.pop())
                    
                    is_negated = True if len(stack) > 0 and stack[-1] == '-' else False
                    if is_negated:
                        res = num1 - num2 if operator == '+' else num1 + num2
                    else:
                        res = num1 + num2 if operator == '+' else num1 - num2
                    
                    stack.append(res)
                    
                temp = stack.pop()
                stack.pop()  # remove the '('
                stack.append(temp)
                i += 1
        
        # no more parentheses
        stack_idx = 0
        summ = 0
        if stack[stack_idx] == '-':
            stack_idx += 1
            summ -= int(stack[stack_idx])
        else:
            summ += int(stack[stack_idx])
            
        stack_idx += 1
            
        while stack_idx < len(stack):
            operator = stack[stack_idx]
            stack_idx += 1
            
            num = int(stack[stack_idx])
            summ = summ + num if operator == '+' else summ - num
            stack_idx += 1
            
        return summ
