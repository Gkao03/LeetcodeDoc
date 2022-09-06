# Decode String
# Time: O(n). n is length of the string.
# Space: O(10^5)
# Topics: String, Stack, Recursion
# Difficulty: Medium
# Notes: while the stack space used is O(n). The length of the output
# string is variable depending on the values of k in the input string.
# The test cases are generated so that the lenggth of the output will
# never exceed 10^5, so the output string will never take more than
# O(10^5) space. Input strings are always valid -> no extra white
# spaces and square brackets are well formed. The decoded string will
# not contain any digits (digits are only for k in input string).

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char != ']':
                stack.append(char)
            else:  # char == ']'
                # strings are immutable so regular concatenation of n characters
                # takes O(n^2) time. Use a list and join at end for O(n) time
                curr_string_list = []
                while stack[-1] != '[':
                    popped = stack.pop()
                    curr_string_list.append(popped)
                stack.pop()  # pop the '['
                
                # get k
                k_list = []
                while len(stack) > 0 and stack[-1].isdigit():
                    k_list.append(stack.pop())
                    
                k_list.reverse()
                k = int("".join(k_list))
                
                curr_string_list.reverse()
                curr_string_list = curr_string_list * k
                stack.append("".join(curr_string_list))
                
        result = "".join(stack)
        return result
