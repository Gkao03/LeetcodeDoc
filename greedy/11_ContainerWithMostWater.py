# Container With Most Water
# Time: O(n)
# Space: O(1)
# Topics: Array, Two Pointers, Greedy
# Difficulty: Medium
# Notes: start at maximum width two pointers. 
# At each iteration, increment the pointer with the lower height

from typing import List

class Solution:
    def get_area(self, height, lidx, ridx):
        if lidx >= ridx:
            return 0
        return min(height[lidx], height[ridx]) * (ridx - lidx)
    
    def maxArea(self, height: List[int]) -> int:
        max_area = self.get_area(height, 0, len(height) - 1)
        
        left_idx = 0
        right_idx = len(height) - 1
        
        while left_idx < right_idx:
            left_height, right_height = height[left_idx], height[right_idx]
            
            if left_height <= right_height:
                left_idx += 1
            else:
                right_idx -= 1
                
            max_area = max(max_area, self.get_area(height, left_idx, right_idx))
        
        return max_area
