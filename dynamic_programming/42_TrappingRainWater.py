# Trapping Rain Water
# Time: O(n)
# Space: O(1)
# Topics: Array, Two Pointers, Dynamic Programming, Stack, Monotonic Stack
# Difficulty: Hard

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1:
            return 0
        
        left = 0
        right = len(height) - 1
        max_left_height = height[0]
        max_right_height = height[-1]
        water_trapped = 0
        
        while left < right:
            if height[right] >= height[left]:  # there is wall on right side that can trap water on left
                max_left_height = max(max_left_height, height[left])

                if height[left] < max_left_height:
                    water_trapped += max_left_height - height[left]
                left += 1
            else:  # there is a wall on the left side than can trap water on the right
                max_right_height = max(max_right_height, height[right])

                if height[right] < max_right_height:
                    water_trapped += max_right_height - height[right]
                right -= 1
        
        return water_trapped
