# Longest Valid Parentheses
# Time: O(n)
# Space: O(1)
# Topics: String, Dynamic Programming, Stack
# Difficulty: Hard
# Notes: can also do with stack but with O(n) space.
# For O(1) space solution, we need to traverse both directions
# in case one set of parentheses goes on too long, in which
# case only traversing one direction may not pick up the other
# count updates.

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right = 0, 0
        answer = 0
        
        # traverse left to right
        for i in range(len(s)):
            char = s[i]
            if char == '(':
                left += 1
            else:  # char == ')'
                right += 1
                
            if left == right:
                answer = max(answer, left + right)
            elif right > left:
                left, right = 0, 0
        
        # traverse right to left
        left, right = 0, 0
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            if char == '(':
                left += 1
            else:  # char == ')'
                right += 1
                
            if left == right:
                answer = max(answer, left + right)
            elif left > right:  # flipped since going right to left
                left, right = 0, 0
                
        return answer
