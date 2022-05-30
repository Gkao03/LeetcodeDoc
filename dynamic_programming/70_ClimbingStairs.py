# Climbing Stairs
# Time: O(n). Pseudo linear where n is the numeric value of the input
# Space: O(1)
# Topics: Math, Dynamic Programming, Memoization
# Difficulty: Easy
# Notes: This is basically fibonacci counting.

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # n is at least 3
        prev_2steps = 1
        prev_1step = 2
        
        step_num = 3
        
        while step_num <= n:
            curr_ways = prev_2steps + prev_1step
            prev_2steps = prev_1step
            prev_1step = curr_ways
            
            step_num += 1
            
        return curr_ways
