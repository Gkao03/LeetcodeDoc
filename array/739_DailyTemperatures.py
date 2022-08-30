# Daily Temperatures
# Time: O(n)
# Space: O(n)
# Topics: Array, Stack, Monotonic Stack
# Difficulty: Medium
# Notes: the idea is to keep a stack that indexes temperatures that are decreasing monotonically.

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        idx = 0
        stack = []
        
        while idx < len(temperatures) - 1:
            stack.append(idx)
            temp_idx = idx + 1
            while temp_idx < len(temperatures) - 1 and temperatures[temp_idx] <= temperatures[stack[-1]]:
                stack.append(temp_idx)
                temp_idx += 1
                
            while len(stack) != 0:
                top_idx = stack[-1]  # peek
                if temperatures[temp_idx] > temperatures[top_idx]:
                    answer[top_idx] = temp_idx - top_idx
                    stack.pop()
                else:
                    break
                    
            idx = temp_idx
            
        # final check - empty anything in the stack
        while len(stack) != 0:
            top_idx = stack[-1]  # peek
            if temperatures[idx] > temperatures[top_idx]:
                answer[top_idx] = idx - top_idx
                stack.pop()
            else:
                break
                
        return answer
