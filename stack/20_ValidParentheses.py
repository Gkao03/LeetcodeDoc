# Valid Parentheses
# Time: O(n)
# Space: O(n)
# Topics: String, Stack
# Difficulty: Easy

class Solution:
    pmap = {')': '(',
            '}': '{',
            ']': '['}
    
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                try:
                    popped = stack.pop()
                    
                    if self.pmap[char] != popped:
                        return False
                except:
                    print("except")
                    return False
                
        if len(stack) != 0:
            return False
        
        return True
