# Basic Calculator II
# Time: O(n)
# Space: O(n)
# Topics: Math, String, Stack
# Difficulty: Medium

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        
        s_idx = 0
        while s_idx < len(s):
            char = s[s_idx]
            if char == ' ':  # skip if space
                s_idx += 1
                continue
            
            if char == '*' or char == '/':
                num1 = int(stack.pop())
                
                while s_idx < len(s) and not s[s_idx].isdigit():
                    s_idx += 1
                    
                num2 = []
                while s_idx < len(s) and s[s_idx].isdigit():
                    num2.append(s[s_idx])
                    s_idx += 1
                num2 = int("".join(num2))

                if char == '*':
                    temp = num1 * num2
                else:  # char == '/'
                    temp = int(num1 / num2)
                stack.append(temp)
            elif char.isdigit():
                digits = []
                while s_idx < len(s) and s[s_idx].isdigit():
                    digits.append(s[s_idx])
                    s_idx += 1
                    
                stack.append(int("".join(digits)))
            else:  # is '+' or '-'
                stack.append(char)
                s_idx += 1
                
        while len(stack) > 1:
            num1 = stack.pop()
            operator = stack.pop()
            num2 = stack.pop()
            
            next_is_neg = False if len(stack) == 0 or stack[-1] == '+' else True
            if next_is_neg:  # must flip operator '+' -> '-' and '-' -> '+'
                operator = '+' if operator == '-' else '-'
                
            if operator == '+':
                temp = num2 + num1
            else:  # operator == '-'
                temp = num2 - num1
                
            stack.append(temp)
            
        return stack[-1]
