# Largest Rectangle in Histogram
# Time: O(n)
# Space: O(n)
# Topics: Array, Stack, Monotonic Stack
# Difficulty: Hard
# Notes: https://www.youtube.com/watch?v=zx5Sw9130L0

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # (index, height)
        
        for i, h in enumerate(heights):
            start = i
            while len(stack) > 0 and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))
            
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
            
        return max_area
