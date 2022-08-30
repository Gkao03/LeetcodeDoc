# House Robber
# Time: O(n)
# Space: O(1)
# Topics: Array, Dynamic Programming
# Difficulty: Medium

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        # nums will have at least 3 elements
        # store the previous 2 house values and use it for dp.
        # at each house index, the greatest money to obtain up to that house (from left to right)
        # will be the max(prevprev_house + current_value, prev_house)
        prevprev_house = nums[0]
        prev_house = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            curr_house = max(prevprev_house + nums[i], prev_house)
            prevprev_house = prev_house
            prev_house = curr_house
            
        return curr_house
