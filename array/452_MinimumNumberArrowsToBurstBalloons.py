# Minimum Number of Arrows to Burst Balloons
# Time: O(nlogn)
# Space: O(1)
# Topics: Array, Greedy, Sorting
# Difficulty: Medium

from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])  # O(nlogn)

        num_arrows = 0
        x_arrow = float("-inf")

        for x_start, x_end in points:
            if not x_start <= x_arrow <= x_end:
                num_arrows += 1
                x_arrow = x_end
            
        return num_arrows
